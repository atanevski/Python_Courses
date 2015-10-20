# -*- coding: utf-8 -*-
# Таблица на трети корени Задача 2 (2 / 4)
# Да се креира таблица на трети корени така што решението ќе биде речник во кој клуч е целиот број а вредност ќе биде
# неговиот трет корен. Клучевите на речникот треба да бидат само природни броеви чиј трети корен е природен број помеѓу m и n.
# Потоа за прочитан влез од стандардниот влез да се испечати неговиот трет корен доколку припаѓа на таблицата со корени
# (речникот) или да се испечати дека нема податоци. Потоа треба да се претвори добиениот речник во листа од торки во облик
# (kluc, vrednost), истата да се сортира и испечати.

if __name__ == "__main__":
    m = input()
    n = input()
    x = input()

    powDict = {}

    for i in range(int(m), int(n) + 1):
        rule = pow(i, 3)
        powDict[rule] = i

    checkDict = powDict.get(int(x))

    if str(checkDict) != "None":
        print(checkDict)
    else:
        print("nema podatoci")

    DictToArray = []

    for item in powDict.items():
        DictToArray.append(item)
    DictToArray.sort()
    print(DictToArray)
