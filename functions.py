import requests
import json
import exceptions as e

baseURL = None
headers = None

def getRequestFromURL(requestURL):
    response = requests.get(requestURL)
    if response.content == str.encode("Bad Request"):
        raise e.BadRequestException()
    return response

def getRequest(request):
    global baseURL, headers
    response = requests.get(baseURL + request, headers = headers)
    if response.content == str.encode("Bad Request"):
        raise e.BadRequestException()
    return response

def getPostRequest(request, data):
    global baseURL, headers
    response = requests.post(baseURL + request, headers = headers, data = json.dumps(data))
    if response.content == str.encode("Bad Request"):
        raise e.BadRequestException()
    return response

def getRequestContent(request):
    global baseURL, headers
    response = requests.get(baseURL + request, headers = headers)
    if response.content == str.encode("Bad Request"):
        raise e.BadRequestException()
    content = response.json()
    if "code" in content and "message" in content:
        raise e.ApiException(content["code"], content["message"])
    return content

def getContent(response):
    content = response.json()
    if "code" in content and "message" in content:
        raise e.ApiException(content["code"], content["message"])
    return content

def saveCredentials():
    global baseURL, headers
    if baseURL and headers and "Authorization" in headers:
        file = open("credentials.txt", "w")
        file.write(baseURL + "\n" + headers["Authorization"])
        file.close()
        print("Credentials saved successfully")
    else:
        print("Error with credentials")

def loadCredentials():
    file = open("credentials.txt", "r")
    global baseURL, headers
    baseURL = file.readline()[:-1]
    headers = {}
    headers["Authorization"] = file.readline()