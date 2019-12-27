import sys
import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/The_Seven_Deadly_Sins:_Wrath_of_the_Gods')
#source = requests.get('https://en.wikipedia.org/wiki/The_Seven_Deadly_Sins:_Wrath_of_the_Gods').text

#URL = requests.get('https://www.scotiaonline.scotiabank.com/online/views/edoc/creditDocuments.bns?tabId=creditDocs&acctId=N3A627486').text
#headers ={"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
#soup = requests.get(source, headers=headers)
res = requests.get('https://en.wikipedia.org/wiki/The_Seven_Deadly_Sins:_Wrath_of_the_Gods')
res.raise_for_status()
wiki = bs4.BeautifulSoup(res.text,'html.parser')

My_table= wiki.find('table',{'class':'wikitable'})

rows= My_table.findAll('tr')



episodeNumber=1
for i in rows:
    line =i.getText()[:1]
    if(line in ['1','2','3','4','5','6','7','8','9']):
        if (episodeNumber<10):
          
            if(episodeNumber == int(i.getText()[:1])):
                print(i.getText())
                print()
                episodeNumber = episodeNumber +1

        else:
            if(episodeNumber == int(i.getText()[:2])):
                print(i.getText())
                print()
                episodeNumber = episodeNumber +1


def find_date(string):
    years= ['2019','2020']