def arb_args(*args):
    print(args)
arb_args('test', 123, '12Test3', False)

def inner_func(num1, num2):
    integer1 = num1 + num2
    integer2 = num1 * num2
    return integer2 + integer1
inner_func(1, 3)

def lunch_lady(student_name, lunch_preference=None):
    if lunch_preference is None:
        lunch_preference = "Mystery Meat"
        print(f"{student_name}  will be served  {lunch_preference}")
lunch_lady("Tim Morton", "Pizza")
lunch_lady("Vincent")

def sum_product(integer1, integer2):
    sum = integer1 + integer2
    product = integer1 * integer2
    print(f"The sum is {sum}, and the product is {product}")
sum_product(2,5)

alias_arbs_args = arb_args

def arb_mean(*numbers):
    total = 0
    for i in numbers:
        total += i 
        avg = i/len(numbers)
    print(f"The average of all of the {numbers} is {avg}")
arb_mean(1,2,3,4,5)

def arb_longest_string(*strings):
    long = 0
    longest = ""
    for a in strings:
        if len(a) > long:
            long = len(a)
            longest = a
    return longest
arb_longest_string(["apple", "pear", "jicama", "elephant", "dinosaur"])