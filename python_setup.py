print("Hello from inside a file!")

#a function that prints a greeting to a user but accepts no arguments and returns nothing
def hello():
    print("Greetings User")
hello()

# a function that accepts 3 arguments and returns a single list with the three arguments insdes as a list elements
def pack(food, drink, fruit_snack):
    return [food, drink, fruit_snack]
result = pack("Pizza", "OJ", "Apple")
print(result)

# a function that should accept a list of any length and prints out a series or strings that say "First I eat __", and "Next I eat __", and if list is empty prints "My lunchbox is empty!", the function should not return anything
def eat_lunch(lunch_meal):
    if not lunch_meal:
        print("My lunchbox is empty :-( ")
    else:
        print("First I eat " + lunch_meal[0])
        if lunch_meal:
            print("Next I eat " + lunch_meal[2])
eat_lunch([])
eat_lunch(['Pizza', 'Tacos', 'PB&J'])  
