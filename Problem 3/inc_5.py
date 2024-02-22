"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Owen Anderson
Lab Time: THUR 2:00-3:15
"""

def inc_5():
    first_num = int(input())
    sec_num = int(input())
    if first_num > sec_num:
        print("Second integer can't be less than the first.")
    else:
        for i in range(first_num, sec_num, 5):
            print(i, end=' ')


if __name__ == '__main__':
    inc_5()