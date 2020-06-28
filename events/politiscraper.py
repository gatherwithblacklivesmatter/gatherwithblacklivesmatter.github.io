from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('politiscraped.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['success'])

source = requests.get('https://www.hollywoodinsider.com/black-lives-matter-protests-live-updates/').text
soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('div',class_='et_pb_text_inner'):
    #print(article.prettify())
    #for para in article.find_all('p'):
        #if(para.text[0] == '1' or para.text[0] == '2' or para.text[0] == '3' or para.text[0] == '4' or para.text[0] == '5' or para.text[0] == '6' or para.text[0] == '7' or para.text[0] == '8' or para.text[0] == '9'):
            #print(para.text)
            #print()
    for listItem in article.find_all('li'):
        print(listItem.text)
        print()

        csv_writer.writerow([listItem.text])

csv_file.close()
