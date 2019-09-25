def main():
    row = int(input("行列を入力してください : "))
    column = int(input("列数を入力してください : "))
    for i in range(1, row+1):
        for j in range(1, column+1):
            ans = '{:3}'.format(i*j)
            print(f'{i} × {j} = {ans} |', end="")
        print("")


if __name__ == '__main__':
    main()