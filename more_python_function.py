def max_num(*numbers):
    return max(numbers)
print(max_num(1,2,3,4))

def mult_list(*numbers):
    result = 1
    for number in numbers:
        result *= number
        print(result)
numbers_list = [1, 2, 3]
print(mult_list(numbers_list))
    

def rev_string(string):
    return string[::-1]
print(rev_string("juicy"))

def num_within(num, start, end):
    return start <= num <= end
print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))

def pascal(number):
    #base case if number is equal to 0
    if number == 0:
        print("Invalid Number Input")
    #and a second base case if the number is 1, to print a single line for the triangle
    elif number == 1 :
        return[[1]]
    else:
        triangle = pascal(number-1)
        last_row = triangle[-1]
        new_row = [1] + [last_row[i] + last_row[i+1] for i in range(len(last_row)-1)] + [1]
        triangle.append(new_row)
        return triangle
    
print(pascal(5))
print(pascal(1))