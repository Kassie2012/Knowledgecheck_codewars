#convert a number into a string

def number_to_string(num):
    return str(num)

#even or odd

def even_or_odd(number):

    
    if (number % 2) == 0:
        return ("Even")
    else:
        return ("Odd")


#vowel count

def get_count(sentence):
    count = 0
    vowels= 'aeiou'
    for x in sentence:
        if x in vowels:
            count += 1
    return count