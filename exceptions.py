class Error(Exception):
    pass

class BadRequestException(Error):
    def printError(self):
        print("Bad Request Error")

class ApiException(Error):
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def printError(self):
        print("API Error")
        print("Code: " + str(self.code))
        print("Message: " + self.message)