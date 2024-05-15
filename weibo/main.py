# 解析weiborss https://rsshub.app/weibo/user/3641314261
import json
import time
import feedparser
import requests
# json 格式参考
# {
#   "tweets": [
#     {
#       "_id": "4994557286028029",
#       "mblogid": "NDFRKpiah",
#       "created_at": "2024-01-26 22:18:34",
#       "geo": null,
#       "ip_location": "发布于 浙江",
#       "reposts_count": 0,
#       "comments_count": 0,
#       "attitudes_count": 0,
#       "source": "微博极速版",
#       "content": "今天年终吃饭，博后喝醉了，送回家。<br />喝醉的人真跟死猪一样<br />真就躺地上一动不动的<br />最后靠小推车+5个人给送回家去。<br />半路还有个师弟也吐了<br />图片有，但不发了 ​​​\n    <div id=\"0xea76724e\" class=\"justified-gallery\">\n        \n    </div>\n    ",
#       "pic_urls": [],
#       "pic_num": 0,
#       "isLongText": false,
#       "url": "https://weibo.com/3641314261/NDFRKpiah",
#       "crawl_time": 1706343223
#     },
#   ],
#   "user": {
#     "_id": "3641314261",
#     "avatar_hd": "https://tvax4.sinaimg.cn/crop.0.0.512.512.1024/d90a0bd5ly8hdlh518e73j20e80e8q3b.jpg?KID=imgbed,tva&Expires=1706440446&ssig=RrNsmZdGpb",
#     "nick_name": "积分中中定理",
#     "verified": false,
#     "description": "一杯茶，一包烟，一道积分算一天",
#     "followers_count": 147,
#     "friends_count": 246,
#     "statuses_count": 464,
#     "gender": "m",
#     "location": "浙江 杭州",
#     "mbrank": 1,
#     "mbtype": 2,
#     "birthday": "2000-04-14",
#     "created_at": "2013-10-04 07:21:22",
#     "desc_text": "",
#     "ip_location": "IP属地：浙江",
#     "sunshine_credit": "信用较好",
#     "label_desc": [
#       "视频累计播放量62"
#     ],
#     "education": {
#       "school": "浙江工业大学"
#     },
#     "crawl_time": 1706429648
#   }
# }

data = requests.get('https://rsshub.app/weibo/user/3641314261')
rss_data = feedparser.parse(data.text)



# print(rss_data.channel[0])  # 获取微博昵称
# 获取微博内容
print(rss_data.entries.__len__())

# 结果json
result = []
tweets = []
user = {
    "nick_name": rss_data.feed.title.replace('的微博', ''),
}

for entry in rss_data.entries:
    # print(entry)
    # 将内容转换为json内的
    tweets.append(
        {

            "created_at": time.strftime("%Y-%m-%d %H:%M", entry.published_parsed),
            "reposts_count": 0,
            "comments_count": 0,
            "attitudes_count": 0,
            "content": entry.title,
            "url": '1'#entry.link,
        }
    )

result.append({
    "tweets": tweets,
    "user": user
})

# print(json.dumps(result, ensure_ascii=False))
# save to file
with open('weibo.json', 'w', encoding='utf-8') as f:
    json.dump(result[0], f, ensure_ascii=False)