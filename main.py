def get_intSum(list1) -> int:
    a = 0
    for i in list1:
        a += i
    return a


abc = (input("input int numbers with spaces "))
list = []
for a in [int(i) for i in abc.split(' ')]:
    list.append(a)


print(get_intSum(list), "big sausages out here")