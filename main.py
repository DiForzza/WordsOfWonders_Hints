from itertools import permutations
min_letters = 3
string = str(input("Введите строку: ")).lower()
permutations_list = [''.join(p) for p in permutations(string, min_letters)]
for i in range(min_letters, len(string)+1):
    permutations_list = permutations_list + [''.join(p) for p in permutations(string, i)]
permutations_list = set(permutations_list)
permutations_list = sorted(permutations_list, key=len)

dicfile = open('russian.txt', 'r')
file_contents = dicfile.read()
new_file_contents = file_contents.split("\n")
print(permutations_list)
for line in new_file_contents:
    for permut in permutations_list:
        if permut == line:
            print(f"Слово {permut} есть в Русском словаре")
            break
dicfile.close()