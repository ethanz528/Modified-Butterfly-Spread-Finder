import functions as fun

refreshToken = None
accessToken = None
apiServer = None
tokenType = None

def generateAccessToken(requestToken):
    global refreshToken
    refreshToken = requestToken
    try:
        accessTokenRequest = fun.getRequestFromURL("https://login.questrade.com/oauth2/token?grant_type=refresh_token&refresh_token=" + requestToken);
        accessTokenContent = fun.getContent(accessTokenRequest)
        global accessToken, apiServer, tokenType
        accessToken = accessTokenContent["access_token"]
        apiServer = accessTokenContent["api_server"]
        tokenType = accessTokenContent["token_type"]
        fun.baseURL = apiServer
        fun.headers = {"Authorization": tokenType + " " + accessToken}
    except (fun.e.BadRequestException, fun.e.ApiException) as exception:
        exception.printError()