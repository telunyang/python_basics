'''
YouTube 下載工具:
- 由於這類工具遊走灰色地帶，所以有時候會不穩。
- 之後會跟大家介紹 youtube-dl 或 yt-dlp 這類工具，直接下載執行檔，透過指令來取得多媒體。


參考資料: 
[1] pytube (pip 套件版本)
https://pytube.io/en/latest/index.html
[2] 下載 Youtube 影片 ( mp4、mp3、字幕 )
https://steam.oxxostudio.tw/category/python/example/youtube-download.html


首先，我們到終端機 (Terminal) 輸入下列指令，然後按下 Enter 安裝套件
pip install -U pytube
'''

# 匯入套件
from pytube import YouTube
from pprint import pprint # Pretty-Print

'''
建立 pytube 物件

下列功能可以參考: https://pytube.io/en/latest/api.html
'''
yt = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

# 物件屬性
print(f'影片標題: {yt.title}')
print(f'影片長度(秒): {yt.length}')
print(f'影片作者: {yt.author}')
print(f'影片作者頻道網址: {yt.channel_url}')
print(f'影片縮圖網址: {yt.thumbnail_url}')
print(f'影片觀看數: {yt.views}')


'''
簡單說明
- yt.streams 是 StreamQuery 物件
- yt.streams.filter().get_highest_resolution() 指定高畫質
- yt.streams.filter().get_by_resolution('360p') 指定解析度
'''

# 支援哪些格式 (直接印出 yt.streams 也可以)
pprint(yt.streams.all())

# 高畫質
print('下載 高畫質 的影音檔...')
yt.streams.filter().get_highest_resolution().download(filename='Never_Gonna_Give_You_Up.mp4')
print('下載完成')

# 360p
print('下載 360p 的影音檔...')
yt.streams.filter().get_by_resolution('360p').download(filename='Never_Gonna_Give_You_Up_360p.mp4')
print('下載完成')