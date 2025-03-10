my_list = [21, 25, 21, 23, 22, 20]
my_list.append(31)
print(f"{my_list}")

my_list2 = [29, 33, 30]
my_list.extend(my_list2)
print(f"{my_list}")

pop = my_list.pop(0)
print(f"{pop}\t{my_list}")

pop = my_list.pop(-1)
print(f"{pop}\t{my_list}")

index = my_list.index(31)
print(f"{index}\t{my_list}")