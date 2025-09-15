# https://etutor2.itsa.org.tw/mod/topics/view.php?id=43057

dictionary = {
    "dog": "狗",
    "cat": "貓",
    "duck": "鴨",
    "cow": "牛",
    "fox": "狐"
}

word = input()
for k, v in dictionary.items():
    if word == k:
        print(v)
        break
    if word == v:
        print(k)
        break
