# break
'''
說明
當偵測到字母 t 時，就會強制結束迴圈
'''
for char in 'content':
    if char == 't':
        break
    print(char, end="")



# continue
'''
說明
當偵測到字母 t 時，
會跳過本次迴圈剩下的程式碼 print(char)，
但不會結束迴圈，仍然會進入下一圈繼續執行
'''
for char in 'content':
    if char == 't':
        continue
    print(char, end="")



# pass
'''
說明
當偵測到字母 t 時，會忽略該條件，繼續像正常迴圈一樣運行程序

備註
有時候寫 pass，是為了將某塊或某行列入 to-do
'''
for char in 'content':
    if char == 't':
        pass
    print(char, end="")