from news_headlines import News_Headlines
import time
import datetime

hour = int(datetime.time().strftime('%H'))
hour -= 5

news = News_Headlines()
tech = news.tech_news()
business = news.business_news()
political = news.political_news()
US_CA = news.US_CA_news()
ME = news.ME_news()
EU = news.EU_news()
UK = news.UK_news()
Asia = news.Asia_news()
India = news.India_news()
world = news.world_news()

while True:
    time.sleep(60)
    if hour == 0:
        tech = news.tech_news()
        business = news.business_news()
        political = news.political_news()
        US_CA = news.US_CA_news()
        ME = news.ME_news()
        EU = news.EU_news()
        UK = news.UK_news()
        Asia = news.Asia_news()
        India = news.India_news()
        world = news.world_news()
    elif hour == 6:
        tech = news.tech_news()
        business = news.business_news()
        political = news.political_news()
        US_CA = news.US_CA_news()
        ME = news.ME_news()
        EU = news.EU_news()
        UK = news.UK_news()
        Asia = news.Asia_news()
        India = news.India_news()
        world = news.world_news()
    elif hour == 12:
        tech = news.tech_news()
        business = news.business_news()
        political = news.political_news()
        US_CA = news.US_CA_news()
        ME = news.ME_news()
        EU = news.EU_news()
        UK = news.UK_news()
        Asia = news.Asia_news()
        India = news.India_news()
        world = news.world_news()
    elif hour == 18:
        tech = news.tech_news()
        business = news.business_news()
        political = news.political_news()
        US_CA = news.US_CA_news()
        ME = news.ME_news()
        EU = news.EU_news()
        UK = news.UK_news()
        Asia = news.Asia_news()
        India = news.India_news()
        world = news.world_news()
    else:
        pass