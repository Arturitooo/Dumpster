listA = list(range(6))
listB = list(range(6))

print(listA, listB)

product = []

for a in listA:
    for b in listB:
        product.append((a,b))

print(product)
print('-'*50)
listC = list(range(6))
listD = list(range(6))

product2 = [(c,d) for c in listC for d in listD]
print(product2)
print('-'*50)
product2 = [(c,d) for c in listC for d in listD if c % 2 == 1 and d % 2 == 0]
print(product2)

product3 = {c:d for c in listC for d in listD if c % 2 == 1 and d % 2 == 0}
print(product3)

#homework 

print("Homework")

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

connections = [(start, stop) for start in ports for stop in ports]
print(connections)
print(len(connections))

connections2 = [(start, stop) for start in ports for stop in ports if start != stop]
print(connections2)
print(len(connections2))

connections2 = [(start, stop) for start in ports for stop in ports if start < stop]
print(connections2)
print(len(connections2))