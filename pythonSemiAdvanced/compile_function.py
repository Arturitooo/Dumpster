import time
source = "reportLine += 1"

reportLine = 0

start = time.time()

for i in range(10000):
    exec(source)

stop = time.time()
time_not_compiled = stop-start

start = time.time()
sourceCompiled = compile(source, "internal variable source", "exec")
for i in range(10000):
    exec(sourceCompiled)
stop = time.time()
time_compiled = stop - start

print(time_not_compiled)
print(time_compiled)
print(reportLine)

import math

formulas_list = ["abs(x**3 - x**0.5)","abs(math.sin(x) * x**2)"]
argument_list = []
for i in range (1000000):
    argument_list.append(i/10)

