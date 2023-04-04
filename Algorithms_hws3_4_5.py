#HW3

#Below The Arithmetical Mean
#When given a list, the program should return a list of all the elements below the original list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of elements.
#Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

def below_arithmetical_men(arr):
    arithmetical_mean = sum(arr) / len(arr)
    print(f"Arithmetical mean: {arithmetical_mean}")
    final_list = []
    for element in arr:
        if element < arithmetical_mean:
            final_list.append(element)
    return final_list

test_list = [1, 3, 5, 6, 4, 10, 2, 3]  #4.25
test_result = below_arithmetical_men(test_list) # [1, 3, 4, 2, 3]
print(test_result)

#Two Lowest Elements
#When given a list of elements, find the two lowest elements.
#They can be equal to each other or different.
#Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def find_two_lowest(arr):
    arr.sort()
    return arr[:2]


test_list = [54, 32, 1, 43, 9, 16]
test_result = find_two_lowest(test_list) # [1, 9]
print(test_result)



#HW4

#Even First
#Your input is a list of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input list).
#Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def even_odd(arr: list):
    next_even = 0
    next_odd = len(arr) - 1
    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next.odd], arr[next_even]
            next_odd -= 1
        return arr

    test_list = [5, 3, 4, 6, 10, 9, 11]
    print(test_list)
    test_result_list = even_odd(test_list)
    print(test_result_list)  # [4, 6, 10,...]
    print(test_list)




#Increment a Number
#Write a program that takes as input a list of digits encoding a nonnegative decimal integer D and updates the list to represent the integer D + 1.
#For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

def plus_one(arr: list):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] !=10:
            break
        arr[i] = 0
        arr[i - 1] += 1
    if arr[0] == 10:
        arr[0] =1
        arr.append(0)git st

    return arr


test_digit1 = [1, 2, 3]
test_digit2 =[1, 9, 9]
test_digit3 = [9, 9, 0]







