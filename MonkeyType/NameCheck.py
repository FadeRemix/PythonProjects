import requests

name = input("Input Username: ")

data = requests.get(f"https://api.monkeytype.com/users/checkName/{name}", headers={'Authorization': 'YOUR OWN KEY'})

datajson = data.json()
datatext = data.text

def AvailableName(datajson):
    Strings = f"""
Message: {datajson['message']}
"""
    print(Strings)

def UnavailableName(datajson):
    Strings = f"""
Message: {datajson['message']}

Data:
    Name: {name}
    User ID:{datajson['data']['uid']}
"""
    print(Strings)

def BadInput(datajson):
# Join the list items from 'validationErrors' into a formatted string
    validation_errors = '\n    '.join(datajson['validationErrors'])
    
    Strings = f"""
Message: {datajson['message']}

Error:
    {validation_errors}
"""
    print(Strings)

def RunCode():
    try:
        status = data.status_code

        if status == 200:
            AvailableName(datajson)
        
        if status == 422:
            BadInput(datajson)

        if status == 409:
            UnavailableName(datajson)

    except requests.exceptions.RequestException as e:
        # Handle possible errors (e.g., connection error, timeout)
        print(f"An error occurred: {e}")

RunCode()
