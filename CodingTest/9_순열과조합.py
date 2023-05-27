from itertools import permutations, combinations

arr = [ i for i in range(5)]

#순열 P
for i in permutations(arr , 4):
    print(i)

#조합 C
result = []
for i in combinations(arr, 2):
    result.append(i)
print(len(result))

