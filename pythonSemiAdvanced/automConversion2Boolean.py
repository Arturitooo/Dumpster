#automatic conversion to logic type

#The if works fine if there are some letters in the string, it doesnt only if the string is empty, however it should be just boolean ofc
#true works fine and false doesnt work
#"true" works fine "false" works fine
#1 works fine, 0 doesnt work
#[1,2,3] works fine, [] doesnt work, [0,0,0] works fine

isOk = []
print('Variable isOk: ',isOk, type(isOk))

if isOk:
    print('True')

#homework for today: https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/lecture/14208740#overview

def DisplayOptions(options):
    for i in range(len(options)):
        print("{} - {}".format(i+1, options[i]))
 
    choice = input('Select option above or press enter to exit: ')
    return choice
    
 
choice='x'
options = ['load data', 'export data', 'analyze & predict']
 
while choice:
 
    choice = DisplayOptions(options)
 
    #executed only if something was entered
    if choice:
        try:
            choice_num = int(choice)-1
            if choice_num >=0 and choice_num < len(options):
                print("you have selected {} - {}".format(choice_num+1, options[choice_num]))
            else:
                print("choose a value from a list or press enter")
        except:
            print("You need to enter a number")
    else:
        print('----- END -----')