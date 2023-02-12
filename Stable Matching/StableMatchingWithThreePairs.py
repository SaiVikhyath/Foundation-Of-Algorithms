# Author: Sai Vikhyath Kudhroli
# Date: 13 October, 2022


"""
Given n men and n women and the preferences of each man and woman, 
Gale-Shapley's stable matching algorithm finds a perfect matching without any unstable pairs.
"""


from collections import defaultdict


def readInput():
    preferenceListXavier = ["Amy", "Bertha", "Clare"]
    preferenceListYancey = ["Bertha", "Amy", "Clare"]
    preferenceListZeus = ["Amy", "Bertha", "Clare"]
    preferenceListAmy = ["Yancey", "Xavier", "Zeus"]
    preferenceListBertha = ["Xavier", "Yancey", "Zeus"]
    preferenceListClare = ["Xavier", "Yancey", "Zeus"]
    return preferenceListAmy, preferenceListBertha, preferenceListClare, preferenceListXavier, preferenceListYancey, preferenceListZeus


def initializeDataStructures():
    # freeMen = ["Xavier", "Yancey", "Zeus"]
    # freeMen = ["Zeus", "Yancey", "Xavier"]
    # freeMen = ["Zeus", "Xavier", "Yancey"]
    freeMen = ["Xavier", "Zeus", "Yancey"]
    wifeOf = dict()
    husbandOf = dict()
    count = defaultdict()
    for i in freeMen:
        count[i] = 0
    return freeMen, wifeOf, husbandOf, count


def galeShapley(preferenceListAmy, preferenceListBertha, preferenceListClare, preferenceListXavier, preferenceListYancey, preferenceListZeus, freeMen, wifeOf, husbandOf, count):
    # print(freeMen, count, [True if i == 3 else False for i in count.values()])
    while(freeMen != [] and all([True if i != 3 else False for i in count.values()])):
        # print("IN GS")
        man = freeMen[0]
        if man == "Xavier":
            woman = preferenceListXavier[count[man]]
            # preferenceListXavier.pop(0)
        if man == "Yancey":
            woman = preferenceListYancey[count[man]]
            # preferenceListYancey.pop(0)
        if man == "Zeus":
            woman = preferenceListZeus[count[man]]
            # preferenceListZeus.pop(0)
        count[man] += 1
        print("\n\n")
        print("Free Men: ", freeMen)
        print(man + " proposing to " + woman)
        print("Husbands of: ", husbandOf)
        print("Wives of: ", wifeOf)
        if woman not in husbandOf:
            husbandOf[woman] = man
            wifeOf[man] = woman
            freeMen.remove(man)
            print("Engaged for first time")
        elif woman == "Amy" and preferenceListAmy[preferenceListAmy.index(husbandOf[woman])] > preferenceListAmy[preferenceListAmy.index(man)]:
            freeMen.append(preferenceListAmy[preferenceListAmy.index(husbandOf[woman])])
            husbandOf[woman] = man
            wifeOf[man] = woman
            freeMen.remove(man)
            print("Dicthed and Engaged")
        elif woman == "Bertha" and preferenceListBertha[preferenceListBertha.index(husbandOf[woman])] > preferenceListBertha[preferenceListBertha.index(man)]:
            freeMen.append(preferenceListBertha[preferenceListBertha.index(husbandOf[woman])])
            husbandOf[woman] = man
            wifeOf[man] = woman
            freeMen.remove(man)
            print("Dicthed and Engaged")
        elif woman == "Clare" and preferenceListClare[preferenceListClare.index(husbandOf[woman])] > preferenceListClare[preferenceListClare.index(man)]:
            freeMen.append(preferenceListClare[preferenceListClare.index(husbandOf[woman])])
            husbandOf[woman] = man
            wifeOf[man] = woman
            freeMen.remove(man)
            print("Dicthed and Engaged")
        else:
            print("Rejected")
            continue
            
    print("\n\n\nStable Matching: ", husbandOf)
    print("\n\n")


if __name__ == "__main__":
    preferenceListAmy, preferenceListBertha, preferenceListClare, preferenceListXavier, preferenceListYancey, preferenceListZeus = readInput()
    freeMen, wifeOf, husbandOf, count = initializeDataStructures()
    galeShapley(preferenceListAmy, preferenceListBertha, preferenceListClare, preferenceListXavier, preferenceListYancey, preferenceListZeus, freeMen, wifeOf, husbandOf, count)