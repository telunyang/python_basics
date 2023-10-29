# 匯入模組
from argparse import ArgumentParser

# 建立 AugumentParser 物件
parser = ArgumentParser()

# 加入參數與說明 (例如: -D 和 --dividend 都是參數名稱)
parser.add_argument("-D", "--dividend", help="設定被除數", default=100, type=int)
parser.add_argument("-d", "--divisor", help="設定除數", default=3, type=int)
parser.add_argument("--msg", help="輸出說明文字", default="取得3的倍數", type=str)

# 取得使用者資料 (來自指令參數)
args = parser.parse_args()
'''
註1:
要撰寫 parser.parse_args()，
執行指令「python 10-2.py --help」才有效

註2:
執行指令「python 10-2.py -D 100 -d 3 --msg 輸出1到100之間3的倍數」時，
-D 的資料，要用 args.dividend 去取值，
-d 的資料，要用 args.divisor 去取值，
--msg 的資料，因為沒有設定縮寫名稱，需要直接使用 args.msg
'''
# 需要先提示使用方式的，可以設定 parser.print_help()
parser.print_help()

# 輸出使用者資料
print(args.dividend, args.divisor, args.msg)

# 簡單範例
print("=" * 50)
print(f"輸出訊息: {args.msg}")
for i in range(1, args.dividend):
    if i % args.divisor == 0:
        print(i, end=" ")