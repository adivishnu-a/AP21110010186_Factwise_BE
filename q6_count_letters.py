"""If the numbers to are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
 
 
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

#Run Code

total = 0
for i in range(1, 1001):
    thou = i//1000
    hun = (i%1000)//100
    ten = (i%100)//10
    one = (i%10)

    if thou==1:
        total = total + 11 #one thousand
    
    if hun==1:
        total = total + 13 #one hundred and
    elif hun==2:
        total = total + 13 #two hundred and
    elif hun==3:
        total = total + 15 #three hundred and
    elif hun==4:
        total = total + 14 #four hundrer and
    elif hun==5:
        total = total + 14 #five hundred and
    elif hun==6:
        total = total + 13 #six hundred and
    elif hun==7:
        total = total + 15 #seven hundred and
    elif hun==8:
        total = total + 15 #eight hundred and
    elif hun==9:
        total = total + 14 #nine hundred and
    
    if ten==1:
        if one==1:
            total = total + 6 #eleven
        elif one==2:
            total = total + 6 #twelve
        elif one==3:
            total = total + 8 #thirteen
        elif one==4:
            total = total + 8 #fourteen
        elif one==5:
            total = total + 7 #fifteen
        elif one==6:
            total = total + 7 #sixteen
        elif one==7:
            total = total + 9 #seventeen
        elif one==8:
            total = total + 8 #eighteen
        elif one==9:
            total = total + 8 #nineteen
        elif one==0:
            total = total + 3 #ten
        continue
    elif ten==2:
        total = total + 6 #twenty
    elif ten==3:
        total = total + 6 #thirty
    elif ten==4:
        total = total + 6 #fourty
    elif ten==5:
        total = total + 5 #fifty
    elif ten==6:
        total = total + 5 #sixty
    elif ten==7:
        total = total + 7 #seventy
    elif ten==8:
        total = total + 6 #eighty
    elif ten==9:
        total = total + 6 #ninety

    if one==1:
        total = total + 3 #one
    elif one==2:
        total = total + 3 #two
    elif one==3:
        total = total + 5 #three
    elif one==4:
        total = total + 4 #four
    elif one==5:
        total = total + 4 #five
    elif one==6:
        total = total + 3 #six
    elif one==7:
        total = total + 5 #seven
    elif one==8:
        total = total + 5 #eight
    elif one==9:
        total = total + 4 #nine

print("Total Number of letters used to write all the numbers from 1 to 1000: ", total)

#Output = 21251
