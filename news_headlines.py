from bs4 import BeautifulSoup
import requests

# Format: [headline, link]

class News_Headlines:
  def __init__(self):
    self.tech = 'https://techcrunch.com/'
    self.business = 'https://www.reuters.com/finance'
    self.political = 'https://time.com/section/politics/'
    self.US_CA = 'https://www.bbc.com/news/world/us_and_canada'
    self.ME = 'https://www.bbc.com/news/world/middle_east'
    self.EU = 'https://www.bbc.com/news/world/europe'
    self.UK = 'https://www.bbc.com/news/uk'
    self.Asia = 'https://www.bbc.com/news/world/asia'
    self.India = 'https://www.bbc.com/news/world/asia/india'
    self.world = 'https://www.bbc.com/news/world'

  def tech_news(self):
    r = requests.get(self.tech)
    r = r.text
    s = BeautifulSoup(r, 'html.parser')
    s = s.find_all(class_ = 'post-block__title__link')
    s = s[6]
    return [s.text.strip(), s['href']]

  def business_news(self):
    r = requests.get(self.business)
    r = r.text
    s = BeautifulSoup(r, 'html.parser')
    s = s.find_all(class_ = 'story-content')
    s = s[0]
    headline = s.find(class_ = 'story-title')
    headline = headline.text.strip()
    link = s.find('a')  
    link = link['href'].strip()
    link = 'https://www.reuters.com' + link
    return [headline, link]

  def political_news(self):
    r = requests.get(self.political)
    r = r.text
    s = BeautifulSoup(r, 'html.parser')
    s = s.find(class_ = 'headline heading-3 heading-content margin-8-bottom media-heading')
    headline = s.text.strip()
    link = s.find('a')['href'].strip()
    link = 'https://time.com' + link
    return [headline, link]

  def US_CA_news(self):
    r = requests.get(self.US_CA)
    r = r.text
    s = BeautifulSoup(r, 'html.parser')
    s = s.find(class_ = 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor')
    headline = s.text.strip()
    link = s['href']
    link = 'https://www.bbc.com' + link
    return [headline, link]

  def ME_news(self):
    r = requests.get(self.ME)
    r = r.text
    s = BeautifulSoup(r, 'html.parser')
    s = s.find(class_ = 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor')
    headline = s.text.strip()
    link = s['href']
    link = 'https://www.bbc.com' + link
    return [headline, link]

  def EU_news(self):
    r = requests.get(self.EU)
    r = r.text
    s = BeautifulSoup(r, 'html.parser')
    s = s.find(class_ = 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor')
    headline = s.text.strip()
    link = s['href']
    link = 'https://www.bbc.com' + link
    return [headline, link]

  def UK_news(self):
    r = requests.get(self.UK)
    r = r.text
    s = BeautifulSoup(r, 'html.parser')
    s = s.find(class_ = 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor')
    headline = s.text.strip()
    link = s['href']
    link = 'https://www.bbc.com' + link
    return [headline, link]

  def Asia_news(self):
    r = requests.get(self.Asia)
    r = r.text
    s = BeautifulSoup(r, 'html.parser')
    s = s.find(class_ = 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor')
    headline = s.text.strip()
    link = s['href']
    link = 'https://www.bbc.com' + link
    return [headline, link]

  def India_news(self):
    r = requests.get(self.India)
    r = r.text
    s = BeautifulSoup(r, 'html.parser')
    s = s.find(class_ = 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor')
    headline = s.text.strip()
    link = s['href']
    link = 'https://www.bbc.com' + link
    return [headline, link]

  def world_news(self):
    r = requests.get(self.world)
    r = r.text
    s = BeautifulSoup(r, 'html.parser')
    s = s.find(class_ = 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold gs-u-mt+ nw-o-link-split__anchor')
    headline = s.text.strip()
    link = s['href']
    link = 'https://www.bbc.com' + link
    return [headline, link]