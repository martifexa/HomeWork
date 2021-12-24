import math

N = int(input("Введите количество точек: "))
print('Введите матрицу смежности: ')
lst = []
dict_of_m = {}
for _ in range(N):
    elem = input().split(' ')
    elem = list(map(lambda x: int(x), elem))
    lst.append(elem)

s = 1
end = N

for i in range(1, N + 1):
    if i == s:
        dict_of_m[i] = 0
    else:
        dict_of_m[i] = math.inf
m = s
lst_m = [s]
# print(dict_of_m)
while len(lst_m) < N:
    next_metka = []
    for j in range(len(lst)):
        if lst[m - 1][j] != 0:
            if lst[m - 1][j] + dict_of_m[m] < dict_of_m[j + 1]:
                dict_of_m[j + 1] = lst[m - 1][j] + dict_of_m[m]
    for key in dict_of_m.keys():
        if key not in lst_m:
            next_metka.append((key, dict_of_m[key]))
    next_metka.sort(key=lambda x: x[1])
    m = next_metka[0][0]
    lst_m.append(m)

way = []
for i in range(N):
    for j in range(len(lst[i])):
        if lst[i][j]:
            way.append([i + 1, j + 1])

for elem in way:
    for i in range(len(way)):
        if elem[0] == start and elem != way[i] and elem[-1] == way[i][0]:
            item = elem.copy()
            item.extend(way[i])
            for a in range(1, len(item) + 1):
                if item[a] == item[a - 1]:
                    item.remove(item[a])
                    break
            way.append(item)

way = [elem for elem in w if elem[0] == start and elem[-1] == finish]
ways_count = list(map(lambda x: x, copy.deepcopy(ways)))

for i in range(len(ways_count)):
    a = i
    sum_r = 0
    for j in ways_count[i]:
        sum_r += lst[a][j - 1]
        a = j - 1
    ways_count[i] = sum_r

way_index = ways_count.index(metka_dct[finish])
right_way = ' - '.join(list(map(str, ways[way_index])))

print(dict_of_m[end])
print(right_way)