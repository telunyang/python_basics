'''
pip install pillow
'''

from PIL import Image, ImageDraw, ImageFont

# 將彩色圖片轉成灰階
def to_gray(input_path, output_path):
    img = Image.open(input_path)
    gray = img.convert("L")
    gray.save(output_path)
    print(f"已存檔灰階圖片：{output_path}")

# 加上浮水印
def add_watermark(input_path, output_path, text, font_path, font_size=60, color_rgb=(255, 255, 255), alpha=128, angle=0):
    # 讀入原圖並轉成 RGBA
    img = Image.open(input_path).convert("RGBA")

    # 建立一個和原圖一樣大的透明圖層，專門放水印
    txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)

    # 字型
    font = ImageFont.truetype(font_path, font_size)

    # 算文字大小，先畫在中間（之後整層一起 rotate）
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    # 文字位置（中間）
    x = (img.width - text_w) // 2
    y = (img.height - text_h) // 2 # 如果希望往下偏移，可以改這裡，例如 + 100

    # 組合 RGBA 顏色
    r, g, b = color_rgb
    fill_color = (r, g, b, alpha)

    # 在 txt_layer 上畫文字
    draw.text((x, y), text, font=font, fill=fill_color)

    # 如果要旋轉，就把整個文字圖層轉一下
    if angle != 0:
        # 先把水印圖層旋轉 (expand=1 讓它變大，不會被裁掉)
        rotated = txt_layer.rotate(angle, expand=1)

        # 建一個跟原圖一樣大的透明圖層來承接旋轉後的水印
        new_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))

        # 把旋轉後的水印，貼到中央
        offset_x = (img.width - rotated.width) // 2
        offset_y = (img.height - rotated.height) // 2

        # 用 alpha 貼上去
        new_layer.paste(rotated, (offset_x, offset_y), rotated)
        txt_layer = new_layer

    # 合成原圖 + 水印圖層
    out = Image.alpha_composite(img, txt_layer).convert("RGB")
    out.save(output_path)
    print(f"已存檔浮水印圖片：{output_path}")


if __name__ == "__main__":
    # 準備圖片
    original_image_path = "original_image.png"
    
    # 1. 先轉灰階的輸出檔名
    output_gray_image_path = "original_image_gray.png"
    
    # 2. 再加水印的輸出檔名
    output_gray_watermark_image_path = "original_image_gray_watermark.png"

    # 3. 先把圖片轉成灰階
    to_gray(original_image_path, output_gray_image_path)

    # 4. 再對灰階圖加「旋轉水印」
    add_watermark(
        input_path=output_gray_image_path, # 輸入檔名
        output_path=output_gray_watermark_image_path, # 輸出檔名
        text="測試浮水印", # 浮水印文字
        font_path="C:/Windows/Fonts/msjh.ttc", # 字型路徑
        font_size=60, # 字型大小
        color_rgb=(255, 0, 0), # 例如：紅色
        alpha=150, # 透明度，最大值是 255，值越大越不透明
        angle=35 # 旋轉 35 度 (正負值都可以)
    )
