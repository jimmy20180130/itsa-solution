# https://etutor2.itsa.org.tw/mod/topics/view.php?id=43060

type = input()

match(type):
    case '1':
        # 空心三角
        for i in range(5):
            print(' ' * (4 - i) + '*' + ' ' * (2 * i - 1) * (i != 0) * (i != 4) + '*' * (i != 0) * (i != 4) + '*' * 8 * (i == 4))
    case '2':
        # 正三角
        for i in range(5):
            # 後面不用加空格，加了的話會 WA
            print(' ' * (4 - i) + '*' * (2 * i + 1))
    case '3':
        # 倒三角
        for i in range(5):
            # 後面不用加空格，加了的話會 WA
            print(' ' * i + '*' * (9 - 2 * i))