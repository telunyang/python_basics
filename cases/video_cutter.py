'''
執行環境: Windows 10

套件安裝
$ pip install wget

用法
$ wget.download(下載來源網路連結, 存放路徑)


參考網頁
[1] How to download portion of video with youtube-dl command?
https://unix.stackexchange.com/questions/230481/how-to-download-portion-of-video-with-youtube-dl-command
[2] FFmpeg: Seeking
https://trac.ffmpeg.org/wiki/Seeking
[3] Python 使用 zipfile 模組壓縮、解壓縮 ZIP 檔案教學與範例
https://officeguide.cc/python-zipfile-module-compression-decompression-tutorial-examples/
[4] 下載 yt-dlp (Linux 和 MacOS 版本，要設定「chmod +x yt-dlp」，MacOS 也要改成 yt-dlp)
- GitHub: https://github.com/yt-dlp/yt-dlp
  - Windows: https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe
  - Linux: https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp
  - MacOS: https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_macos
[5] 下載 ffmpeg binary
- 網站: https://ffmpeg.org/download.html
  - Windows: https://www.gyan.dev/ffmpeg/builds/
  - Linux: https://ffmpeg.org/download.html#build-linux
  - MacOS: https://ffmpeg.org/download.html#build-mac



測試指令:

- 下載影片
  - Windows 10: ./yt-dlp.exe https://www.youtube.com/watch?v=t0igPuDjYUE -f "b[ext=mp4]" -o "%(id)s.%(ext)s"
  - MacOS: ./yt-dlp "https://www.youtube.com/watch?v=t0igPuDjYUE" -f "b[ext=mp4]" -o "%(id)s.%(ext)s"

- 切割影片 方式1 (設定持續時間，意思是從 ss 開始往後多少時間，速度快)
  - Windows 10: ./ffmpeg/bin/ffmpeg.exe -ss 00:02:43.000 -i t0igPuDjYUE.mp4 -t 00:00:24.000 -y -c copy output.mp4
  - MacOS: ./ffmpeg -ss 00:02:43.000 -i t0igPuDjYUE.mp4 -t 00:00:24.000 -y -c copy output.mp4

- 切割影片 方式2 (準確指定結束時間，就是真的從 ss 看到 to，速度慢)
  - Windows 10:./ffmpeg/bin/ffmpeg.exe -i t0igPuDjYUE.mp4 -ss 00:02:39.5 -to 00:03:06 -y -c copy output.mp4
  - MacOS: ./ffmpeg -i t0igPuDjYUE.mp4 -ss 00:02:39.5 -to 00:03:06 -y -c copy output.mp4

可能延伸應用:
[1] [nodejs] Youtube Video Downloader, Splitter and Converter (ubuntu, nodejs, socketio, ffmpeg)
https://youtu.be/2whO3-DBXkw
'''

import subprocess, os, wget, zipfile



'''
下載工具
'''
# 下載 ffmpeg
if not os.path.exists('./ffmpeg.zip'):
    print('[下載 ffmpeg]')
    wget.download(
        'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip', 
        './ffmpeg.zip'
    )

    # 對 ffmpeg 解壓縮 至 指定路徑
    with zipfile.ZipFile('./ffmpeg.zip', 'r') as zf:
        # 解壓縮
        print('[解壓縮 zip]')
        zf.extractall(path='./')

        # 更改資料夾名稱
        os.rename(zf.namelist()[0], './ffmpeg')

# 下載 yt-dlp
if not os.path.exists('./ffmpeg/bin/yt-dlp.exe'):
    print('[下載 yt-dlp]')
    wget.download(
        'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe', 
        './ffmpeg/bin/yt-dlp.exe'
    )



'''
下載影片
'''
# 設定 YouTube 影片 id 和 video 連結
video_id = 't0igPuDjYUE'
video_url = f'https://www.youtube.com/watch?v={video_id}'

# 判斷影片是否已經下載
if not os.path.exists(f'./{video_id}.mp4'):
    # 設定下載影片指令
    cmd = [
        './ffmpeg/bin/yt-dlp.exe',
        video_url,
        '-f', 'w[ext=mp4]', 
        '-o', './%(id)s.%(ext)s'
    ]

    # 執行指令，並取得輸出訊息
    print("[下載影片]")
    std_output = subprocess.run(cmd)
    if std_output.returncode == 0:
        print(f'成功')
    else:
        print(f'失敗')



'''
影像剪輯
'''
# 選擇方式 1 或 2 (會影響執行程式的指令選擇)
choice = 1

# 定義剪輯指令
if choice == 1: # 切割影片 方式1 (設定持續時間，意思是從 ss 開始往後多少時間，速度快)
    cmd = [
        './ffmpeg/bin/ffmpeg.exe',
        '-ss', '00:02:43.000', 
        '-i', f'./{video_id}.mp4', 
        '-t', '00:00:24.000', 
        '-y', 
        '-c', 'copy', 
        './output.mp4'
    ]
elif choice == 2: # 切割影片 方式2 (準確指定結束時間，就是真的從 ss 看到 to，速度慢)
    cmd = [
        './ffmpeg/bin/ffmpeg.exe', 
        '-i', f'./{video_id}.mp4', 
        '-ss', '00:02:39.5', 
        '-to', '00:03:06',
        '-y', 
        '-c', 'copy', 
        './output.mp4'
    ]

# 執行指令
print("[切割影片]")
std_output = subprocess.run(cmd)
if std_output.returncode == 0:
    print(f'成功')
else:
    print(f'失敗')