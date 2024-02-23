"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Owen Anderson
Lab Time: THUR 2:00 - 3:15
"""

def norm():
    first_num = int(input())
    numlist = []
    for i in range(first_num):
        number = input()
        numlist.append(float(number))
    max_num = max(numlist)
    for x in numlist:
        new_val = x/max_num
        print(f'{new_val:.2f}')






if __name__ == "__main__":
    norm()