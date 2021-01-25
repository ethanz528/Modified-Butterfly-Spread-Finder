import functions as fun
import options as opt
import datetime
import copy

riskFreeInterestRate = 0.93

def getBreakEvenPrice(option):
    if option["optionType"] == "Call":
        return option["strikePrice"] + option["askPrice"]
    else:
        return option["strikePrice"] - option["askPrice"]

def findPoP(symbol, strike, dte):
    return

def longCallButterfly():
    return

def shortCallButterfly():
    return

def longPutButterfly():
    return

def shortPutButterfly():
    return

def ironButterfly():
    return

def reverseIronButterfly():
    return

def modifiedButterfly(symbol, type, lowerDTE, upperDTE, lowerPoP, upperPoP, lowerDownsideProtection, upperDownsideProtection, lowerPLMR, upperPLMR):
    symbolId = opt.sea.findSymbol(symbol)["symbols"][0]["symbolId"]
    options = opt.getOptionInfoWithinDOE(lowerDTE, upperDTE, symbol)
    currentDateTime = datetime.datetime.fromisoformat(opt.sea.fun.getRequestContent("v1/time")["time"])
    modifiedButterflies = {}
    for option in options:
        modifiedButterflies[option] = []
        for strike in options[option]["Put"]:
            if lowerPoP <= 3 * (options[option]["Put"][strike]["delta"] + 1) <= upperPoP:
                modifiedButterflies[option].append({"symbol": symbol,
                                                    "symbolId": symbolId,
                                                    "type": type,
                                                    "expiryDate": option,
                                                    "DTE": (datetime.datetime.fromisoformat(option) - currentDateTime).days,
                                                    "lowerStrike": None,
                                                    "middleStrike": options[option]["Put"][strike],
                                                    "upperStrike": None,
                                                    "PoP": 3 * (options[option]["Put"][strike]["delta"] + 1),
                                                    "entry": None,
                                                    "maxRisk": None,
                                                    "PLMR": None,
                                                    "maxProfit": None})
    for option in modifiedButterflies:
        for modifiedButterfly in modifiedButterflies[option]:
            middleStrike = modifiedButterfly["middleStrike"]["strikePrice"]
            middlePrice = modifiedButterfly["middleStrike"]["lastTradePrice"]
            for lowerStrike in options[option]["strikes"]:
                for upperStrike in options[option]["strikes"]:
                    if lowerStrike < middleStrike < upperStrike:
                        lowerPrice = options[option]["Put"][lowerStrike]["lastTradePrice"]
                        upperPrice = options[option]["Put"][upperStrike]["lastTradePrice"]
                        entry = -1 * upperPrice + 3 * middlePrice - 2 * lowerPrice
                        maxRisk = 1 * upperStrike - 3 * middleStrike + 2 * lowerStrike + entry
                        PLMR = entry / maxRisk
                        if lowerPLMR <= PLMR <= upperPLMR:
                            newMB = copy.deepcopy(modifiedButterfly)
                            newMB["lowerStrike"] = options[option]["Put"][lowerStrike]
                            newMB["upperStrike"] = options[option]["Put"][upperStrike]
                            newMB["entry"] = entry
                            newMB["maxRisk"] = maxRisk
                            modifiedButterflies[option].append(newMB)
    return