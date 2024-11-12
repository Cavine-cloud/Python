#palindrome
name =input('enter any name')
reversed_name = name[-1::-1]
if name == reversed_name:
    print(f"{name}is a palindrome")
else:
    print(f"{name} is not a palindrome")