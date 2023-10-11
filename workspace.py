import requests

url = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=7a7e006b-ec19-47ad-8fc8-6640a7a72f8a&rid=f401c58d-f9e2-41e4-91b5-cd0ac7a901e5"

html = requests.get(url)

html.encoding = "big5"

# html.encoding = "utf-8-big"

print(html.text)
# input("return")