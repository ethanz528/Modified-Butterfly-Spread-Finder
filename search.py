import functions as fun

searchHistory = []
MAX_SEARCH_HISTORY = 10

def findSymbol(prefix):
    try:
        request = fun.getRequest("v1/symbols/search?prefix=" + prefix)
        content = fun.getContent(request)
        global searchHistory
        if len(searchHistory) > 0 and content["symbols"][0] == searchHistory[0]:
            pass
        elif content["symbols"][0] in searchHistory:
            searchHistory.remove(content["symbols"][0])
            searchHistory.insert(0, content["symbols"][0])
        else:
            searchHistory.insert(0, content["symbols"][0])
            if len(searchHistory) > MAX_SEARCH_HISTORY:
                searchHistory.pop()
        return content
    except (fun.e.BadRequestException, fun.e.ApiException) as exception:
        exception.printError()

def findSymbolPrice(prefix):
    id = findSymbol(prefix)["symbols"][0]["symbolId"]
    request = fun.getRequest("v1/markets/quotes/" + str(id))
    content = fun.getContent(request)
    content = content["quotes"][0]
    return content["lastTradePrice"]

