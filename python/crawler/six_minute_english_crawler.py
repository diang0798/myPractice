from bs4 import BeautifulSoup
import requests
import urllib.request
import os
import re


def get_sourses():
    url = "http://www.bbc.co.uk/learningenglish/english/features/6-minute-english"
    source_code = requests.get(url)
    html_text = source_code.text
    soup = BeautifulSoup(html_text, 'html.parser')
    i = 1
    for link in soup.findAll(href=re.compile("ep-")):
        if link.string != None:
            href = "http://www.bbc.co.uk" + link.get('href')
            title = link.string
            print(href)
            print(title)
            get_single_item_data(href, i)
            i += 1


def get_single_item_data(item_url, i):
    source_code = requests.get(item_url)
    html_text = source_code.text
    soup = BeautifulSoup(html_text, 'html.parser')
    file_path = 'E:\\6minEnglish\\' + str(i)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    for item_name in soup.findAll('a', {'class': 'download bbcle-download-extension-pdf'}):
        # file_path = r'E:\6minEnglish'
        # os.makedirs("E:\\6minEnglish\\" + str(i))
        #dir_name = os.path.join(r"E:\\6minEnglish\\" + str(i), str(i) + '.pdf')
        # file_path = create_project_dir(r"E:\6minEnglish")
        urllib.request.urlretrieve(item_name.get('href'), file_path +'\\' + str(i)+'.pdf')
        print(item_name.get('href'))
        print(str(i)+'.pdf')
    for item_name in soup.findAll('a', {'class': 'download bbcle-download-extension-mp3'}):
        # file_path = r"E:\6minEnglish + '\str(title)'"
        # create_project_dir("E:\\6minEnglish\\" + title)
        #dir_name = os.path.join(r'E:\6minEnglish' + str(j), str(j) + '.pdf')
        urllib.request.urlretrieve(item_name.get('href'), file_path +'\\' + str(i)+'.mp3')
        # print(str(i) + '.mp3')
        print(item_name.get('href'))
        print(str(i) + '.mp3')


get_sourses()
