"""If the numbers to are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
 
 
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

#Run Code

def number_to_words(n):
    if 1 <= n < 20:
        return ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
                "eighteen", "nineteen"][n-1]
    elif 20 <= n < 100:
        tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        return tens[n // 10 - 2] + ("" if n % 10 == 0 else number_to_words(n % 10))
    elif 100 <= n < 1000:
        return number_to_words(n // 100) + "hundred" + ("" if n % 100 == 0 else "and" + number_to_words(n % 100))
    elif n == 1000:
        return "onethousand"
    return ""

def count_letters_in_range(start, end):
    total_letters = 0
    for i in range(start, end + 1):
        word = number_to_words(i)
        total_letters += len(word)
    return total_letters

total_letters = count_letters_in_range(1, 1000)
print(total_letters)
