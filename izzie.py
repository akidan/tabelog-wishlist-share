#-*-coding:utf-8-*- 
import sys
import time
import requests
import bs4

user1 = "001474438" # yue
user2 = "002747445" # izzie
went_page_user1 = 13
wish_page_user1 = 7
went_page_user2 = 7
wish_page_user2 = 14

def write_file(list, filename):
    filename = "/Users/Zhiyue/Workspaces/tabelog-wishlist-share/"+filename+".txt"
    print (filename)
    f = open(filename,"w")
    for i in list:
        f.write(i.encode('utf-8')+"\n")
    f.close()

# URL example
# https://tabelog.com/rvwr/ userID /rvwlst/0/0/ pageNo /?bookmark_type= 1: went 2:wish

tabelog = "https://tabelog.com/rvwr/"
went_user1 = []
wish_user1 = []
went_user2 = []
wish_user2 = []
went_user1_url = []
wish_user1_url = []
went_user2_url = []
wish_user2_url = []

went_same = []
wish_same = []
a_went_b_wish = []
a_wish_b_went = []

for i in range (1, int(went_page_user1+1)):
    url = tabelog + user1 + "/rvwlst/0/0/" + str(i) + "/?review_content_exist=0&bookmark_type=1"
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    result = soup.find_all("a", class_="rvw-item__rst-name")
    for res in result:
        went_user1.append(res.text+"\t"+res.get('href'))

#for i in range (1, int(wish_page_user1+1)):
#    url = tabelog + user1 + "/rvwlst/0/0/" + str(i) + "/?review_content_exist=0&bookmark_type=2"
#    response = requests.get(url)
#    soup = bs4.BeautifulSoup(response.text, "html.parser")
#    result = soup.find_all("a", class_="simple-rvw__rst-name-target")
#    print(result)
#    for res in result:
#        wish_user1.append(res.text+"\t"+res.get('href'))

for i in range (1, int(went_page_user2+1)):
    url = tabelog + user2 + "/rvwlst/0/0/" + str(i) + "/?review_content_exist=0&bookmark_type=1"
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    result = soup.find_all("a", class_="rvw-item__rst-name")
    for res in result:
        went_user2.append(res.text+"\t"+res.get('href'))

for i in range (1, int(wish_page_user2+1)):
    url = tabelog + user2 + "/rvwlst/0/0/" + str(i) + "/?review_content_exist=0&bookmark_type=2"
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    result = soup.find_all("h3")
    for res in result:
        wish_user2.append(res.text)

def print_file(list):
    print("###")
    for i in list:
        print(i.encode("utf-8"))

went_user1 = sorted(went_user1); #print_file(went_user1); #write_file(went_user1,"went_user1");
#wish_user1 = sorted(wish_user1); #print_file(wish_user1); #write_file(wish_user1,"wish_user1");
went_user2 = sorted(went_user2); #print_file(went_user2); #write_file(went_user2,"went_user2");
for i in went_user1:
    if i in went_user2:
        went_same.append(i)
print_file(went_same);
#wish_user2 = sorted(wish_user2); #print_file(wish_user2); #write_file(wish_user2,"wish_user2");

