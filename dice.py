import random


def main():
    surface = int(input("サイコロの面の数は？ : "))
    trial = int(input("何回振りますか？ : "))
    result = []
    for i in range(0, trial):
        result.append(random.randrange(surface) + 1)
    print(result)


if __name__ == '__main__':
    main()