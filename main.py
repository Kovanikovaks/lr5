def zad1():
    lis = [1, 2, 4, 6, 7]
    print(lis)
    a = int(input('введите любое число'))
    if a in lis:
        print("ура,вы угадали")
    else:
        print("вы не угадали")

zad1()

def zad2():
    lis2 = [1, 2, 4, 6, 7, 3, 5, 8, 4]
    pov =[]
    for b in lis2:
        count = 0
        for x in lis2:
            if x == b:
                count += 1
        pov.append(count)

    pov1 = set()
    index = 0
    while index < len(lis2):
        if pov[index] != 1:
            pov1.add(lis2[index])
        index += 1

    print(pov1)

zad2()
def zad3():
    lis3 = ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс',)
    week = int(input("введите количество выходных"))
    print('выходные', lis3[week + 1:])
    print('рабочие дни', lis3[:week + 1])

zad3()

def zad4():
    fam1 = ['иванов', 'сидоров', 'петров']
    fam2 = ['кузнецов', 'грачев', 'скворцов']
    foot = (fam1[0], fam2[1], fam2[2])
    print(*fam1)
    print(*fam2)
    print(*foot)
    print(len(foot))
    foot = tuple(sorted(foot))
  print(foot)
    if 'иванов' in foot:
        print("иванов есть в команде")

zad4()


