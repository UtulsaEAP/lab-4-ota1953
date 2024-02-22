"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: OWEN ANDERSON
Lab Time: THUR 2:00-3:15

"""


def reverse_binary():
    user_num = int(input())
    while user_num >=1:
        print(user_num%2, end="")
        user_num //= 2



if __name__ == "__main__":
    reverse_binary()