import requests


# requests.get('https://tvax4.sinaimg.cn/large/d90a0bd5gy1hpp8mnl9amj20u01uon4u.jpg')

# save img 
with open('1.jpg', 'wb') as f:
    f.write(requests.get('https://tvax4.sinaimg.cn/large/d90a0bd5gy1hpp8mnl9amj20u01uon4u.jpg').content)