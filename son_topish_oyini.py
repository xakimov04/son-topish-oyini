from random import randint

def kompyuter():
    count = 0
    count2 = 0
    print("Kompyuter o'ylagan sonni topishga harakat qiling.\n")

    komp_nums = randint(1, 100)

    while True:
        try:
            num = int(input("Son kiriting: "))
        except ValueError:
            print("Iltimos son kiriting!")
            continue

        count += 1

        if num > komp_nums:
            print("Kichikroq son kiriting.\n")
        elif num < komp_nums:
            print("Kattaroq son kiriting.\n")
        else:
            print(f"Siz kompyuter o'ylagan sonni {count} urunishda topdingiz.\n")
            break

    print("Endi siz son o'ylaysiz kompyuter topishga harakat qiladi.\n")

    x, y = 1, 100

    while True:
        a = randint(x, y)
        print(f"Siz o'ylagan son {a} mi.")
        b = input("ishora bering (+; -; t): ")
        count2 += 1

        if b == "t":
            print(f"Kopmyuter siz o'ylagan sonni {count2} urunishda topdi.\n")
            break
        elif b == "+":
            x = a + 1
        elif b == "-":
            y = a - 1

    if count == count2:
        print(f"Durrang bo'ldi: {count}:{count2}",end="\n\n")
    elif count > count2:
        print(f"Kopmyuter yutdi: {count}:{count2}",end="\n\n")
    elif count < count2:
        print(f"Siz yutdingiz: {count}:{count2}",end="\n\n")

    num3 = input("Yana o'ynashni hohlaysizmi (start=1, stop=0): ")
    if num3 == "1":
        kompyuter()
    elif num3 == "0":
        print("THE END!")

kompyuter()
