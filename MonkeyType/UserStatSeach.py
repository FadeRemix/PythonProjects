import requests

idorname = input("Input UID or Username: ")

userstats = requests.get(f"https://api.monkeytype.com/users/{idorname}/profile", headers={'Authorization': 'YOUR OWN KEY'})

a = userstats.json()

def Output(a):
    Strings = f"""
Message: {a['message']}

Data:
    Name: {a['data']['name']}
    Added at: {a['data']['addedAt']}
    
    Typing Stats:
        Completed Tests: {a['data']['typingStats']['completedTests']}
        Started Tests: {a['data']['typingStats']['startedTests']}
        Time Typing: {a['data']['typingStats']['timeTyping']}
    
    Personal Bests (Time):
        15s Test: 
            Timestamp: {a['data']['personalBests']['time']['15'][0]['timestamp']}
            WPM: {a['data']['personalBests']['time']['15'][0]['wpm']}
            Accuracy: {a['data']['personalBests']['time']['15'][0]['acc']}c
            Consistency: {a['data']['personalBests']['time']['15'][0]['consistency']}
            Punctuation: {a['data']['personalBests']['time']['15'][0]['punctuation']}
        
        30s Test: 
            First Test:
                WPM: {a['data']['personalBests']['time']['30'][0]['wpm']}
                Accuracy: {a['data']['personalBests']['time']['30'][0]['acc']}
                Consistency: {a['data']['personalBests']['time']['30'][0]['consistency']}
                Timestamp: {a['data']['personalBests']['time']['30'][0]['timestamp']}
            Second Test:
                WPM: {a['data']['personalBests']['time']['30'][1]['wpm']}
                Accuracy: {a['data']['personalBests']['time']['30'][1]['acc']}
                Consistency: {a['data']['personalBests']['time']['30'][1]['consistency']}
                Timestamp: {a['data']['personalBests']['time']['30'][1]['timestamp']}

        60s Test:
            WPM: {a['data']['personalBests']['time']['60'][0]['wpm']}
            Accuracy: {a['data']['personalBests']['time']['60'][0]['acc']}
            Consistency: {a['data']['personalBests']['time']['60'][0]['consistency']}
            Timestamp: {a['data']['personalBests']['time']['60'][0]['timestamp']}
        
        120s Test:
            WPM: {a['data']['personalBests']['time']['120'][0]['wpm']}
            Accuracy: {a['data']['personalBests']['time']['120'][0]['acc']}
            Consistency: {a['data']['personalBests']['time']['120'][0]['consistency']}
            Timestamp: {a['data']['personalBests']['time']['120'][0]['timestamp']}
    
    Personal Bests (Words):
        10 Words Test:
            WPM: {a['data']['personalBests']['words']['10'][0]['wpm']}
            Accuracy: {a['data']['personalBests']['words']['10'][0]['acc']}
            Consistency: {a['data']['personalBests']['words']['10'][0]['consistency']}
        
        25 Words Test:
            WPM: {a['data']['personalBests']['words']['25'][0]['wpm']}
            Accuracy: {a['data']['personalBests']['words']['25'][0]['acc']}
            Consistency: {a['data']['personalBests']['words']['25'][0]['consistency']}
        
        50 Words Test:
            First Test:
                WPM: {a['data']['personalBests']['words']['50'][0]['wpm']}
                Accuracy: {a['data']['personalBests']['words']['50'][0]['acc']}
                Consistency: {a['data']['personalBests']['words']['50'][0]['consistency']}
            Second Test:
                WPM: {a['data']['personalBests']['words']['50'][1]['wpm']}
                Accuracy: {a['data']['personalBests']['words']['50'][1]['acc']}
                Consistency: {a['data']['personalBests']['words']['50'][1]['consistency']}
        
        100 Words Test:
            WPM: {a['data']['personalBests']['words']['100'][0]['wpm']}
            Accuracy: {a['data']['personalBests']['words']['100'][0]['acc']}
            Consistency: {a['data']['personalBests']['words']['100'][0]['consistency']}
    
    Experience Points: {a['data']['xp']}       
"""
    print(Strings)
    
Output(a)
