# -*- coding: utf-8 -*-
# Таблица на квадрати, кубови и корени Задача 3 (1 / 2)
# Да се направи таблица на степени, кубови и квадратни корени на броевите од m до n, така што резултатот
# ќе се чува во речник на кој клучот е самиот број, а вредноста е торка од облик (квадрат, куб, корен).
# Пр:
#
# {1:(1,1,1), 2:(4,8,1.1412), …}
#
# Потоа да се искористи речникот така што за прочитан број од стандардниот влез ќе ја испечати торката
# која е соодветна на бројот или да испечати “nema podatoci” доколку прочитаниот
# број е надвор од интервалот. Речникот кој е добиен во зависност од прочитаните m и n да се конвертира
# во листа од торки од облик (kluc, vrednost), истата да се сортира и испечати.

if __name__ == "__main__":
    m = input()
    n = input()
    x = input()

    Dictionary = {}
    for i in range(int(m), int(n) + 1):
        Dictionary[i] = (i ** 2, i ** 3, i ** 0.5)

    check = Dictionary.get(int(x))

    if str(check) != 'None':
        print(check)
    else:
        print("nema podatoci")

    DictToArrayy = []
    for item in Dictionary.items():
        DictToArrayy.append(item)
    DictToArrayy.sort()
    print(DictToArrayy)
