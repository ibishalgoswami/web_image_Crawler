#Web image Crawler.
from bs4 import BeautifulSoup
import requests
import os

url="https://www.pexels.com/pt-br/"
res=requests.get(url)
Html_content=res.content
soup=BeautifulSoup(Html_content,'html.parser')

os.mkdir('my_photos') #Creating new dir named my_photos.
all_imgs=soup.select('img[src^="https://images.pexels.com/photos"]') #using regex selecting the particular images.
img_con=[]
for i in all_imgs:
    if i.get('data-big-src')!=None:
        img_con.append(i.get('data-big-src'))
remove_duplicates=set(img_con)
for j,img_data in enumerate(remove_duplicates):
    img_data=requests.get(img_data).content
    with open('my_photos/'+str(j+1)+'.jpg','wb') as fh:
        fh.write(img_data)