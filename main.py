def get_intSum(list1) -> int:
    a = 0
    for i in list1:
        a += i
    return a


abc = (input("input int numbers with spaces "))
list = []
for int(i) in abc.split(','):
    list.append(i)


print(get_intSum(list), "Big sausage out there")