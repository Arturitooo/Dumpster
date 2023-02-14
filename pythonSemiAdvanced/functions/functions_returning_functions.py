#option_nr1
def Calculate(kind = '+', *args):
    result = 0 
    if kind == '+':
        for a in args:
            result += a
    elif kind == "-":
        for a in args:
            result -= a
    return result

#option_nr2
def CreateFunction(kind = "+"):
    source = '''
def f(*args):
    result = 0 
    for arg in args:
        result {}= arg
    return result
'''.format(kind)
    exec(source, globals())
    return f
        
    
f_add = CreateFunction("+")
print(f_add(1,2,3))
f_subs = CreateFunction("-")
print(f_subs(10,20,30))

from datetime import datetime
 
def time_span_m(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 60)[0]
 
def time_span_h(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 3600)[0]
 
def time_span_d(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, 86400)[0]

start = datetime(2019, 1, 1, 0, 0, 0)  
end  = datetime.now()

print('minutes')
print(time_span_m(start, end))
print('hours')
print(time_span_h(start, end))
print('days')
print(time_span_d(start, end))


def Create_function(span='m'):
    if span == 'm':
        sec = 60
    elif span == 'h':
        sec = 3600
    elif span =='d':
        sec = 86400
    source = '''
def f(start, end):
    duration = (end - start)
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s,{})[0]
'''.format(sec)
    exec(source, globals())
    return f


print("Created functions")
f_minutes = Create_function('m')
f_hours = Create_function('h')
f_days = Create_function('d')
 
print(f_minutes(start, end))
print(f_hours(start, end))
print(f_days(start, end))