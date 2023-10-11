import requests
import csv
import pandas as pd

url = "https://data.nhi.gov.tw/resource/mask/maskdata.csv"

header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Whale/3.22.205.26 Safari/537.36"}

html = requests.get(url,headers=header)

# print(html.text)

# prefix
prefix = "臺中"

decode_content = html.content.decode("utf-8")

csv_data = csv.reader(decode_content.splitlines(),delimiter=',')

original_list = list(csv_data)

pd_csv_data = pd.DataFrame(original_list)

pd_csv_data.head()



# # start load csv
# with open(url) as CSVfile:
#     csv_data = csv.reader(CSVfile)

