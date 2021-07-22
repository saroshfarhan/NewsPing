from newsapi import NewsApiClient
import json
import twilioSMS
import time

api = NewsApiClient(api_key='YOUR_NEWS_API_KEY')


def getNews():
    topHeadlineBusiness = api.get_top_headlines(
        country='in', category='business')

    prettyResponse = json.dumps(topHeadlineBusiness, indent=4)

    # print(prettyResponse)
    return topHeadlineBusiness


def parseNews():
    headlines = getNews()
    # title = ""
    # desc = ""
    # url = ""
    for i in range(5):
        title = headlines["articles"][i]["title"]
        desc = headlines["articles"][i]["description"]
        url = headlines["articles"][i]["url"]
        twilioSMS.sendMessage(title, desc, url)
        time.sleep(6)


if __name__ == '__main__':
    parseNews()
