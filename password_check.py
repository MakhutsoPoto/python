def is_valid_password(password):
    

    if not len(password.replace(" ", "")) >=8 :
        return False
    count_letter,count_digit,count_upper = 0,0,0
    for letter in password:
        if letter.isalpha():
            count_letter +=1
        if letter.isdigit():
            count_digit += 1
        if letter.isupper():
            count_upper += 1
    return  count_letter>=1 and count_digit>=1 and count_upper>=1
