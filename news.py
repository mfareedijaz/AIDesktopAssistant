# importing requests package
import requests	 
from output_data import display_output
from internet import checkInternet

def getLatestNews():
    if (checkInternet()):
        query_params = {
	    "source": "bbc-news",
	    "sortBy": "top",
	    "apiKey": "e918fbc4c39544808e91173bcbf10e42"
        }
        main_url = " https://newsapi.org/v1/articles"
        # fetching data in json format
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()

        # getting all articles in a string article
        article = open_bbc_page["articles"]

        # empty list which will 
        # contain all trending news
        results = []
        
        for ar in article:
            results.append(ar["title"])
            
        for i in range(len(results)):
            
            # printing all trending news
            display_output(str(i + 1) + " " + results[i])

        return "So these were the top news from today"
    else:
        return "Please check your internet connection!"