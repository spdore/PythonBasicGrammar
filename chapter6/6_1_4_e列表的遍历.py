my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_while = []
my_list_for = []

index = 0

while index < len(my_list):
    if (my_list[index] % 2) == 0:
        my_list_while.append(my_list[index])
    index += 1

for element in my_list:
    if (element % 2) == 0:
        my_list_for.append(element)

print(f"通过while循环，从列表{my_list}中取出偶数，组成新列表：{my_list_while}")
print(f"通过for循环，从列表{my_list}中取出偶数，组成新列表：{my_list_for}")