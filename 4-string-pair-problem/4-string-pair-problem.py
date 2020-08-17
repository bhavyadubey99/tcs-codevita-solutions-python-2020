n = int(input())  # for taking input, although, not very useful in our case
string = input()  # taking the list as a string for input with whitespaces

string = string.split(" ")  # for removing whitespaces

# creating a dictionary with key as numbers and value
# as corresponding vowels in their spelling

nums = {"1": "oe",
        "2": "o",
        "3": "ee",
        "4": "ou",
        "5": "ie",
        "6": "i",
        "7": "ee",
        "8": "ei",
        "9": "ie",
        "0": "eo"}

# an empty string where we will store the vowels if the number occurs
vowels = ""

for s in string:  # checking every character in string
    for num in nums:  # with every key in dictionary
        if s == num:
            vowels += nums[s]

# storing length of vowels string to get final number of vowels
d = int(len(vowels))

# checking if numbers add up to the digit.
count = 0
for s in range(len(string) - 1):
    if int(string[s]) + int(string[s + 1]) == d:
        count += 1
# another dictionary to store spelling of numbers.
letters = {"1": "one",
           "2": "two",
           "3": "three",
           "4": "four",
           "5": "five",
           "6": "six",
           "7": "seven",
           "8": "eight",
           "9": "nine",
           "0": "zero"}

for letter in letters:  # for checking in count number in dictionary
    if str(count) == letter:
        print(letters[letter])  # finally printing the answer
