"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Owen Anderson
Lab Time: THUR 2:00 - 3:15
"""

def password_mod():
    word = str(input())
    password = ''
    word_list = list(word)

    index = 0
    while index < len(word_list):
        if word_list[index] == 'i':
            word_list[index] = '1'

        if word_list[index] =='a':
            word_list[index] = '@'

        if word_list[index] == 'm':
            word_list[index] = 'M'

        if word_list[index] == 'B':
            word_list[index] = '8'

        if word_list[index] == 's':
            word_list[index] = '$'
        
        password += word_list[index]
        index += 1

        
    print(password+"!")
if __name__ == "__main__":
    password_mod()