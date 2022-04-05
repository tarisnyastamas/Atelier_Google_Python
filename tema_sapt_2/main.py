my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]


my_list_asc = sorted(my_list)

my_list_desc = sorted(my_list, reverse=True)

list_3 = list()

for i in my_list:
    if i % 3 == 0:
        list_3.append(i)


#just some comment
if __name__ == '__main__':
    print("Original list: ")
    print(my_list)
    print("List in ascending form: ")
    print(my_list_asc)
    print("List in descending form: ")
    print(my_list_desc)
    print("Even index numbers: ")
    print(my_list[::2])
    print("Odd index numbers: ")
    print(my_list[1::2])
    print("Numbers from list divisible by 3: ")
    print(list_3)