#ID & Name : 20CE013 Mayank Chovatiya
#Aim       : You are given a string and your task is to swap cases.
#            In other words, convert all lowercase letters to uppercase letters and vice versa.

def swapcase(S):
    x = ""
    for i in S:
        if i.isupper() == True: #check letter is uppercase or not
            x += (i.lower()) #convert uppercase letters to lowercase letters
        else:
            x += (i.upper()) #convert lowercase letters to uppercase letters
    return x

if __name__ == '__main__':
    S = input() #HackerRank.com presents "Pythonist 2"
    Answer = swapcase(S)
    print(Answer) #hACKERrANK.COM PRESENTS "pYTHONIST 2"