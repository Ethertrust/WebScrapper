from lxml import html
import requests
from bs4 import BeautifulSoup

titlesl = []
originaltitlesl = []

for x in range(1, 468):
    makeapage = 'http://www.animespirit.ru/page/' + str(x) + '.html'
    page = requests.get(makeapage)
    soup = BeautifulSoup(page.text, "lxml")
    #print (page.json())
    tree = html.fromstring(page.content)

    #for y in range(2, 12):
        #//*[@id="dle-content"]/div[2]/div/h2/a
        #//*[@id="dle-content"]/div[11]/div/h2/a
        #//*[@id="dle-content"]/div[2]/div/h2/a
        #//*[@id="dle-content"]/div[11]/div/h2/a
        #//*[@id="dle-content"]/div[2]/center/table/tbody/tr[2]/td/b[1]/h3
        #//*[@id="dle-content"]/div[11]/center/table/tbody/tr[2]/td/b[1]/h3

        #makeatitle = '//*[@id="dle-content"]/div[' + str(y) + ']/div/h2/a/text()'
        #This will create a list of buyers:
        #titles = tree.xpath(makeatitle)
        #for title in titles:
        #    print('--->' + title)
        #    titlesl.append(title)
    #This will create a list of prices
    divs = soup.find(id = "dle-content")
    originaltitledivs = divs.find_all("div", {"class": "content-block"})

    for ordiv in originaltitledivs:
        originaltitle = ordiv.find_all('h3')

        if not originaltitle:
            title = ordiv.find_all('h2')[0].find('a').get_text()
            titlesl.append(title)
            print('-------------')
            print(title + '---> ortitle: ' + str(originaltitle))

        for ortitle in originaltitle:
            img = ortitle.find('img')
            if img != None:
                originaltitle = img.get('title')
            else:
                originaltitle = ortitle.get_text()
            originaltitlesl.append(originaltitle)
            print(originaltitle)
    #originaltitletables = originaltitledivs.find_all('table')
    #titledivs = originaltitledivs.find_all('h2')
    #for row in titledivs:
    #    title = row.find('a').get_text()
    #    print('------')
    #    print(title)
    #    titlesl.append(title)

    #originaltitlerows = originaltitledivs.find_all('h3')
    #for row in originaltitlerows:
    #    img = row.find('img')
    #    if img != None:
    #        originaltitle = img.get('title')
    #    else:
    #        originaltitle = row.get_text()
    #    print('-----------------------------')
    #    print(originaltitle)
    #    originaltitlesl.append(originaltitle)
f = open('F:\AnimeSpiritList.txt', 'w', encoding='utf-8')
c = 0
for index in titlesl:
    f.write(str(c+1) + '. ' + index + '; ' + originaltitlesl[c] + '\n')
    c += 1
f.close()

#import urllib

#urllib.urlretrieve("http://www.digimouth.com/news/media/2011/09/google-logo.jpg", "local-filename.jpg")