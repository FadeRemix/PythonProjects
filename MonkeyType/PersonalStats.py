import requests

userstats = requests.get("https://api.monkeytype.com/users/stats", headers={'Authorization': 'YOUR OWN KEY'})

userstatsJSON = userstats.json()


def UserStatsFunc(userstatsJSON):
    output = f"""
Message: {userstatsJSON['message']}
    
Data:
ID: {userstatsJSON['data']['_id']}
Completed Tests: {userstatsJSON['data']['completedTests']}
Started Tests: {userstatsJSON['data']['startedTests']}
Time Spent Typing: {userstatsJSON['data']['timeTyping']} seconds
    """
    print(output)


UserStatsFunc(userstatsJSON)
