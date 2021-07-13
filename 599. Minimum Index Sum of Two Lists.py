def findRestaurant(list1, list2):
    distance = 10**20
    dict = {}
    indexes = []
    a, b = set(list1), set(list2)
    x = (a.intersection(b))
    for i in x:
        dict[i] = list1.index(i) + list2.index(i)
    for i in dict.values():
        if i < distance:
            distance = i
    for i in dict.items():
        if i[1] == distance:
            indexes.append(i[0])
    return indexes

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Shogun","KFC","Burger King"]
print(findRestaurant(list1, list2))