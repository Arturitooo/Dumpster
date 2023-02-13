def BuyMe(prefix, what = 'something nice'):
    print(prefix, what)


BuyMe('Please buy me', 'a new car')
BuyMe(what = 'Please buy me', prefix = 'a new car')
BuyMe("Please")

#homework https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14288614#overview

def show_progress(how_many, character = "*"):
    print(character*how_many)

show_progress(10)
show_progress(15)
show_progress(30)
 
show_progress(10, '-')
show_progress(15, '+')

def BuyMe(prefix = 'Please buy me', what = "something nice", *args, **kwargs):
    #variable args provides user possibility to input more variables than predicted - it's a tuplet // name is random - the star matters
    #**kwargs allows us to provide new variable with key word (KEY WORD ARGUMENTS - **kwargs)
    print(prefix, what)
    print(args)
    print(kwargs)

BuyMe('Please buy me', 'a new car', 'a dog', 'a cat', shop = "nike", location = "New York")

products = ['milk','bread','flakes']
parameters = {"price":'low', 'time':'now'}

BuyMe("buy","me", *products, **parameters)
#if you want the function to treat something as args or kwargs, you have to provide suitable number of starts before variable name

#another homework xd https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14289212#overview

def calculate_paint(efficency_ltr_per_m2, *args):
    total_area = sum(args)
    paint = total_area * efficency_ltr_per_m2
    return print(f"To paint it, you need to use:", paint, "lilters of paint")

calculate_paint(2,15,7,14)

def calculate_paint2(efficency_ltr_per_m2, *args):
    total_area = sum(args)  
    paint = total_area * efficency_ltr_per_m2
    return print(f"To paint it, you need to use:", paint, "lilters of paint")

rooms = [15,7,14]

calculate_paint2(2, *rooms)

#tasknr2

def log_it(*args):
    path = r"C:\Users\Art\Documents\GitHub\learning\pythonSemiAdvanced\functions\logs.txt"
    with open(path, "w") as f:
 
        for line in args:
            f.write(line)
            f.write(' ')
 
        f.write("\n")

log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')