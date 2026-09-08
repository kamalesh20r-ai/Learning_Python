def count_char(text,ch):
    if len(text) == 0 :
        return 0
    if ch == text[0] :
        return 1+count_char(text[1:],ch)
    return count_char(text[1:],ch)
count=count_char("banana","a")
print("Count of a in banana :",count)
    