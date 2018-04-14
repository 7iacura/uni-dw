from bs4 import BeautifulSoup
import requests
from pprint import pprint

# import mysql.connector

# cnx = mysql.connector.connect(user='root', password='',
#                               host='localhost',
#                               database='datawarehouse')
# query = ('select * from myguests')
#
# cursor = cnx.cursor()
# result = cursor.execute(query)
# pprint ("result:",result)
#
# cnx.close()
# exit(0)
# year = 2018
# month= 2
# day = 11

url = "https://www.wunderground.com/history/airport/KNYC/"+str(year)+"/"+str(month)+"/"+str(day)+"/DailyHistory.html?req_city=New+York&req_state=NY&req_statename=New+York"
resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')

rows = soup.find(id='obsTable').find_all('tr')
data = []
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
pprint(data)