import urllib.request
import wikipedia

def checkInternet():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False
    
def checkOnWikipedia(query):
    query = query.lower()
    query = query.replace("what is", "")
    query = query.replace("what is a", "")
    query = query.replace("who is", "")
    query = query.replace("tell me about", "")
    query = query.replace("do you know about", "")
    query = query.replace("do you know who is", "")
    query = query.replace("do you know about what is", "")
    query = query.replace("meaning of", "")
    query = query.replace("what is the meaning of", "")
    
    query = query.strip()

    try:
        result = wikipedia.summary(query, sentences=2)
        return str(result) 
    
    except: 
        return "Searched data not found!"
    
# checkOnWikipedia("who is pakistan")
