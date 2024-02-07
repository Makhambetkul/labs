def pal(str):
    a=str[::-1]
    b=str
    if b==a:
        print("palindrome")
    else:
        print("not palindrome")
user_input=input()
pal(user_input)