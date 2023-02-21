import random

def generate_random_list(length):
    """Generate a list of random numbers of a given length"""
    random_list = []

    for i in range(length):
        random_list.append(random.random())
    
    return random_list
print(generate_random_list(20))
def find_max(numbers):
    """Find the largest(maximum) number in a list of numbers"""
    for i in range(len(numbers)):
        if i < len(numbers) - 1:
            if numbers[i] > numbers[i+1]:
                max_number = numbers[i]
        else:
            if numbers[i] > numbers[i-1]:
                max_number = numbers[i]
    return (max_number)


def find_min(numbers):
    """Find the smallest(minimum) number in a list of numbers"""
    return min(numbers)


def find_average(numbers):
    """Find the average of a list of numbers int the list 'numbers' and return 
    it as a float to one decimal point"""
    pass

def find_even_pairs(numbers):
    """Find the neigbouring pairs of numbers that sum up to an even number and 
    then return a list of immutable lists with the pairs' index numbers 
    ie: [1,3,5] returns [(0,1)]
    """
    index_list = []
    
    for i in range(len(numbers)):
        if i < len(numbers) - 1:
            if (numbers[i] + numbers[i+1]) % 2 == 0:
                index_list.append((i,(i+1)))
    
    return  index_list


def find_odd_pairs(numbers):
    """Find the neigbouring pairs of numbers that sum up to an even number and 
    then return a list of immutable lists with the pairs' index numbers 
    ie: [1,3,5] returns [(1,2)]
    """
    index_list = []
    for i in range(len(numbers)):
        if i < len(numbers) - 1:
            if (numbers[i] + numbers[i+1]) % 2 != 0:
                index_list.append((i,(i+1)))
    return  index_list


def find_number_of_even_numbers(numbers):
    """Find the total number of odd numbers in the list 'numbers' and return 
    the number as an integer"""
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count = count+1

    return count

def find_number_of_odd_numbers(numbers):
    """Find the total number of odd numbers in the list 'numbers' and return 
    the number as an integer"""
    count = 0
    for i in numbers:
        if i % 2 != 0:
            count = count+1

    return count


def find_even_numbers(numbers):
    """Find the number of odd numbers in a list of numbers and return them in
    in an immutable list"""
    even_numbers = []

    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)
        
    return tuple(even_numbers)

      
def find_odd_numbers(numbers):
    """Find the number of odd numbers in a list of numbers and return them in
    in an immutable list"""
    pass

def return_list_stats(numbers):
    """Using the list of numbers, use the relevant functions to return a
        dictionary of statics for the list of numbers. This dictionary must have
        the following keys:
            unique_numbers : a set of unique numbers in the list 'numbers',
            max : largest number in the list 'numbers',
            min : smallest number in the list 'numbers',
            average : average of the numbers in the list 'numbers',
            even_pairs : a list of immutable lists that have neighboring pairs 
                that sum up to an even number in the list 'numbers',
            odd_pairs : a list of immutable lists that have neighboring pairs 
                that sum up to an even number in the list 'numbers',
            even_numbers : an immutable list of all the even numbers in the list
                'numbers',
            odd_numbers : an immutable list of all the odd numbers in the list 
                'numbers',
            number_of_even_numbers : the total number of even numbers in the 
                list 'numbers',
            number_of_odd_numbers : the total number of even numbers in the list
                 'numbers'
    """


    pass
