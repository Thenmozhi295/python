from requests_html import HTMLSession
import pandas as pd
urls = ['https://www.amazon.com/Gender-Dimensions-Disaster-Management-Guide/dp/1853396079/ref=sr_1_1?dchild=1&keywords=gender+dimensions+in+disaster+management&qid=1634795366&sr=8-1']
       # https://www.amazon.com/Gender-Dimensions-Disaster-Management-Guide/dp/1853396079/ref=sr_1_1?dchild=1&keywords=Gender+Dimensions+in+Disaster+Management%3AA+Guide+for+South+Asia&qid=1634798391&sr=8-1
def getDetails(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    try:
        product = {
            'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
            'author': r.html.xpath('//*[@id="bylineInfo"]', first=True).text,
            'publisher': r.html.xpath('//*[@id="detailBullets_feature_div"]/ul/li[1]/span/span[2]', first=True).text
        }
        print(product)
    except:
        product = {
            'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
            'author': 'item unavailable',
            'publisher': 'publisher unavailable'
        }
        print(product)
    return product

bookdetails = []
for url in urls:
    bookdetails.append(getDetails(url))

print(len(bookdetails))

pricesdf = pd.DataFrame(bookdetails)
pricesdf.to_excel('scrap.xlsx', index=False)