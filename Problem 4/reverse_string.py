"""
Complete the following python code to reverse the string entered by the user.

Name: Owen Anderson
Lab Time: THUR 2:00 - 3:15
"""

def reverse_string():
    word_input = input()
    reverse = ''
    while len(word_input) > 0 and word_input != "done" and word_input != "Done" and word_input != "d":
        print(word_input[::-1])
        word_input = input()
    pass


    

if __name__ == "__main__":
    reverse_string()