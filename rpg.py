import random

def main():
    maxlen = 12

    digits = ['0','1','2','3','4','5','6','7','8','9']
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','w','x','y','z']
    letters_u = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
    symbols = ['!','@','#','$','%','^','&','*']

    combined_list = digits + letters + letters_u + symbols

    rdigits = random.choice(digits)
    rletters = random.choice(letters)
    rletters_u = random.choice(letters_u)
    rsymbols = random.choice(symbols)

    temp_list = rdigits + rletters + rletters_u + rsymbols

    password = ""
    for i in range(maxlen - 4):
        temp_list = temp_list + random.choice(combined_list)

    for i in temp_list:
        password = password + i

    print(password)
main()
    
