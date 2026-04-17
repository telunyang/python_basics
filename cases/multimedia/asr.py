'''
# 網址
https://huggingface.co/MediaTek-Research/Breeze-ASR-25

# 安裝套件
# 1) 先裝 FFmpeg（供 torchaudio / torchcodec 使用）
conda install -c conda-forge "ffmpeg<8"

# 2) 用官方 CPU index 安裝 PyTorch 2.8.0 + 對應套件（注意 +cpu 後綴）
pip install -U pip
pip install "torch==2.8.0+cpu" "torchvision==0.23.0+cpu" "torchaudio==2.8.0+cpu" --index-url https://download.pytorch.org/whl/cpu

# 3) TorchCodec 與 torch 2.8 相容的版本（0.7）
pip install "torchcodec==0.7.0"

# 4) 其他工具（回到預設 PyPI，不要帶 --index-url）
pip install -U "transformers>=4.43,<5" "datasets[audio]" "accelerate"
'''

import torchaudio
import torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration, AutomaticSpeechRecognitionPipeline
import pprint
import time

# 計時開始
time_start = time.time()

# 讀取音訊檔案
audio_path = "./BxFuEcDGroM.wav"
waveform, sample_rate = torchaudio.load(audio_path)          

# 檔案前處理。主要是轉成單聲道，並且取樣率改成 16kHz
if waveform.shape[0] > 1:
    waveform = waveform.mean(dim=0)                         
waveform = waveform.squeeze().numpy()                        

if sample_rate != 16_000:
    resampler = torchaudio.transforms.Resample(sample_rate, 16_000)
    waveform = resampler(torch.tensor(waveform)).numpy()
    sample_rate = 16_000

# 讀取模型與處理器
processor = WhisperProcessor.from_pretrained("MediaTek-Research/Breeze-ASR-25")
model = WhisperForConditionalGeneration.from_pretrained("MediaTek-Research/Breeze-ASR-25").to("cpu").eval() # 有 GPU 的話改成 .to("cuda")

# 設定模型的語言與任務
asr_pipeline = AutomaticSpeechRecognitionPipeline(
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    chunk_length_s=0
)

# 執行語音辨識
output = asr_pipeline(waveform, return_timestamps=True)  
pprint.pprint(output)

# 計時結束
time_end = time.time()

print("總共花費時間：%.2f 秒" % (time_end - time_start))