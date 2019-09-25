def main():
    number = input("データを入力してください(スペース区切り) > ")
    number_list = number.split()
    total = 0
    max_v = 0
    min_v = int(number_list[0])

    for number in number_list:

        int_num = int(number)
        total += int_num
        if max_v < int_num:
            max_v = int_num
        if min_v > int_num:
            min_v = min_v
    print(f"合計値 : {total}")
    print(f"最大値 : {max_v}")
    print(f"最小値 : {min_v}")
    print(f"平均値 : {total//len(number_list)}")


if __name__ == '__main__':
    main()