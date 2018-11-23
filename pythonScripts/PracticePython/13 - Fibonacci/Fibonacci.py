# Exercise 13

# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci sequence is a sequence of numbers where the next number in the sequence is the sum
# of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibonaccisequence():
    number = int(input("How many numbers would you like to generate? "))
    count = 1
    sequence = []
    if number == 0:
        sequence = []
    elif number == 1:
        sequence = [1]
    elif number == 2:
        sequence = [1,1]
    elif number > 2:
        sequence = [1,1]
        while count < (number - 1):
            sequence.append(sequence[count] + sequence[count - 1])
            count += 1
    return sequence
print(fibonaccisequence())