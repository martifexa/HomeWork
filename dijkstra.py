import math
N = int(input("Введите количество точек: "))
print('Введите матрицу смежности: ')
lst = []
dict_of_m = {}
for _ in range(N):
    elem = input(). split(' ')
    elem = list(map(lambda x: int(x), elem))
    lst.append(elem)

s = 1
end = N

for i in range(1, N+1):
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

print(dict_of_m[end])