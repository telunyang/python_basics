'''
建立一個將 mp3 轉換成 wav 的腳本

安裝 wget
pip install wget
'''
import os
import zipfile
import wget
import subprocess

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

    # 更改 yt-dlp 權限，讓它可以執行
    # os.chmod('./ffmpeg/bin/yt-dlp', 0o755)

# 使用 yt-dlp 下載 YouTube 影片並轉換成 mp3，並以 youtube id 作為主檔名
def download_youtube_as_mp3(youtube_url):
    # 確認 ffmpeg/bin/yt-dlp 存在
    if not os.path.exists('./ffmpeg/bin/yt-dlp.exe'):
        raise FileNotFoundError('yt-dlp not found, please check the path.')

    # 使用 yt-dlp 下載 YouTube 影片並轉換成 mp3
    command = [
        './ffmpeg/bin/yt-dlp.exe',
        '-x', '--audio-format', 'mp3',
        '--audio-quality', '0',  # 最佳音質
        '-o', '%(id)s.%(ext)s',  # 以 youtube id 作為主檔名
        youtube_url
    ]
    out = subprocess.run(command, check=True)

    return out.returncode

# 將 mp3 轉換成 wav
def mp3_to_wav(mp3_path, wav_path):
    # 確認 ffmpeg/bin/ffmpeg 存在
    if not os.path.exists('./ffmpeg/bin/ffmpeg.exe'):
        raise FileNotFoundError('ffmpeg not found, please check the path.')

    # 使用 ffmpeg 將 mp3 轉換成 wav
    command = [
        './ffmpeg/bin/ffmpeg.exe',
        '-i', mp3_path,
        '-ar', '16000',  # 設定取樣率為 16kHz
        '-ac', '1',      # 設定聲道數為單聲道
        wav_path
    ]
    out = subprocess.run(command, check=True)

    return out.returncode
    
if __name__ == '__main__':
    # youtube url
    id = 'BxFuEcDGroM'
    youtube_url = 'https://www.youtube.com/watch?v=' + id
    code = download_youtube_as_mp3(youtube_url)

    # 測試 mp3_to_wav 函式
    if code == 0:
        source = id + '.mp3'
        target = id + '.wav'
        return_code = mp3_to_wav(source, target)
        if return_code == 0:
            print(f'Converted {source} to {target} successfully.')
        else:
            print(f'Failed to convert {source} to {target}.')