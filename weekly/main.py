


import requests
import os
import datetime

# datetime.datetime.now().strftime("%W.%Y.%m.%d")

# 判断今天是周几
if datetime.datetime.now().weekday() == 0:
    # print("今天是周一")
    datestr = datetime.datetime.now().strftime("%W.%Y.%m.%d") + ".md"
else:
    # print(datetime.datetime.now().weekday())
    # print("今天不是周一")
    datestr = (datetime.datetime.now() - datetime.timedelta(days=datetime.datetime.now().weekday())).strftime("%W.%Y.%m.%d") + ".md"



# 获取环境变量 URL + WW.YYYY.MM.DD
url = str(os.environ["URL"]  + datestr)
print(url)

# 发送请求 并保存为md文件
with open("weekly.md", "w", encoding="utf-8") as f:
    f.write(requests.get(url).text)
