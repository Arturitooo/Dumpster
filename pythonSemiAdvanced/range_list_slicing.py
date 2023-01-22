for i in range(10,0,-1):
    print(i)

print("Decreasing numbers from 10 to 1")

for i in range(10):
    print(i)
print("Decreasing numbers from 0 to 9")

print("is it range?")
lista = range(10)
print(lista, type(lista))

print(f"\nis it list?")
lista = list(range(10))
print(lista, type(lista))

#this operation is called "slicing"
print(f"\nis the list withour last 2 elements?")
print(lista[:-2])

print(f"\nis the list reverted, without last element?")
print(lista[-1:0:-1])

print(f"\nis the list reverted, with last element?")
print(lista[-1::-1])

list2 = lista
print(lista, id(lista))
print(list2, id(list2))
print("As you can see, it's the same variable with just different name, if you would add some value to one variable, it would also appear in the other one\n")

list3 = lista.copy()
print(lista, id(lista))
print(list3, id(list3))
print("As you can see, it's different variable now. You can easily add new element to one of the lists")