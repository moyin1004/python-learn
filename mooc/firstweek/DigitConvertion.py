"""
num = input()
for temp in num:
    if temp == 0:
        print("零", end = "")
    elif temp == '1':
        print("一", end = "")
    elif temp == '2':
        print("二", end = "")
    elif temp == '3':
        print("三", end = "")
    elif temp == '4':
        print("四", end = "")
    elif temp == '5':
        print("五", end = "")
    elif temp == '6':
        print("六", end = "")
    elif temp == '7':
        print("七", end = "")
    elif temp == '8':
        print("八", end = "")
    else:
        print("九", end = "")
"""

template = "零一二三四五六七八九"

s = input()
for c in s:
print(template[eval(c)], end="")
