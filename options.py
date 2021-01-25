import search as sea
import datetime

def getOptionSymbol(symbol):
    return getOptionId(sea.findSymbol(symbol)["symbols"][0]["symbolId"])

def getOptionId(symbolId):
    try:
        request = sea.fun.getRequest("v1/symbols/" + str(symbolId) + "/options")
        content = sea.fun.getContent(request)
        return content
    except (sea.fun.e.BadRequestException, sea.fun.e.ApiException) as exception:
        exception.printError()

def getOptionsInfo(optionIds):
    try:
        optionQuotes = []
        for i in range(0, len(optionIds) // 100 + 1):
            request = sea.fun.getPostRequest("v1/markets/quotes/options", {"optionIds": optionIds[100 * i: 100 * (i + 1)]})
            content = sea.fun.getContent(request)
            optionQuotes += content["optionQuotes"]
        return optionQuotes
    except (sea.fun.e.BadRequestException, sea.fun.e.ApiException) as exception:
        exception.printError()

def getOptionInfoWithinDOE(lowerBound, upperBound, symbol):
    currentDateTime = datetime.datetime.fromisoformat(sea.fun.getRequestContent("v1/time")["time"])
    lowerBound = currentDateTime + datetime.timedelta(days = lowerBound)
    upperBound = currentDateTime + datetime.timedelta(days = upperBound)
    symbolId = sea.findSymbol(symbol)
    symbolId = symbolId["symbols"][0]["symbolId"]
    optionChain = getOptionId(symbolId)
    optionChain = [option for option in optionChain["optionChain"] if lowerBound <= datetime.datetime.fromisoformat(option["expiryDate"]) <= upperBound]
    optionInfo = {}
    optionIds = []
    for option in optionChain:
        optionInfo[option["expiryDate"]] = {"strikes": [], "Call": {}, "Put": {}}
        for strikePrice in option["chainPerRoot"][0]["chainPerStrikePrice"]:
            optionInfo[option["expiryDate"]]["strikes"].append(strikePrice["strikePrice"])
            optionIds.append(strikePrice["callSymbolId"])
            optionIds.append(strikePrice["putSymbolId"])
    optionQuotes = getOptionsInfo(optionIds)
    i = 0
    for option in optionInfo:
        for strikePrice in optionInfo[option]["strikes"]:
            call = optionInfo[option]["Call"]
            call[strikePrice] = optionQuotes[i]
            call[strikePrice]["strikePrice"] = strikePrice
            call[strikePrice]["optionType"] = "Call"
            call[strikePrice]["expiry"] = datetime.datetime.fromisoformat(option)
            call[strikePrice]["DTE"] = (call[strikePrice]["expiry"] - currentDateTime).days
            put = optionInfo[option]["Put"]
            put[strikePrice] = optionQuotes[i + 1]
            put[strikePrice]["strikePrice"] = strikePrice
            put[strikePrice]["optionType"] = "Put"
            put[strikePrice]["expiry"] = datetime.datetime.fromisoformat(option)
            put[strikePrice]["DTE"] = (put[strikePrice]["expiry"] - currentDateTime).days
            i += 2
    return optionInfo