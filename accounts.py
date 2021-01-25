import functions as fun

accounts = None
userId = None
activities = None
orders = None
executions = None
balances = None
positions = None

def loadAll():
    loadAccounts()
    loadActivities()
    loadOrders()
    loadExecutions()
    loadBalances()
    loadPositions()

def loadAccounts():
    try:
        request = fun.getRequest("v1/accounts")
        content = fun.getContent(request)
        global accounts, userId
        accounts = content["accounts"]
        userId = content["userId"]
    except (fun.e.BadRequestException, fun.e.ApiException) as exception:
        exception.printError()

def loadActivities():
    return
    global activities
    activities = {}
    try:
        for account in accounts:
            request = fun.getRequest("v1/accounts/" + account["number"] + "/activities")
            content = fun.getContent(request)
            activities[account["number"]] = content["activities"]
    except (fun.e.BadRequestException, fun.e.ApiException) as exception:
        exception.printError()

def loadOrders():
    global orders
    orders = {}
    try:
        for account in accounts:
            request = fun.getRequest("v1/accounts/" + account["number"] + "/orders")
            content = fun.getContent(request)
            orders[account["number"]] = content["orders"]
    except (fun.e.BadRequestException, fun.e.ApiException) as exception:
        exception.printError()

def loadExecutions():
    global executions
    executions = {}
    try:
        for account in accounts:
            request = fun.getRequest("v1/accounts/" + account["number"] + "/executions")
            content = fun.getContent(request)
            executions[account["number"]] = content["executions"]
    except (fun.e.BadRequestException, fun.e.ApiException) as exception:
        exception.printError()

def loadBalances():
    global balances
    balances = {}
    try:
        for account in accounts:
            request = fun.getRequest("v1/accounts/" + account["number"] + "/balances")
            content = fun.getContent(request)
            balances[account["number"]] = content
    except (fun.e.BadRequestException, fun.e.ApiException) as exception:
        exception.printError()

def loadPositions():
    global positions
    positions = {}
    try:
        for account in accounts:
            request = fun.getRequest("v1/accounts/" + account["number"] + "/positions")
            content = fun.getContent(request)
            positions[account["number"]] = content["positions"]
    except (fun.e.BadRequestException, fun.e.ApiException) as exception:
        exception.printError()