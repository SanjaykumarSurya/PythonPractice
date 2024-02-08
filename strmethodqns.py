    # Author     : Sanjaykumar.M
    # Date       : 08-02-2024
    # Description: python string methods questions
    # Batch time : 4.00 - 7.00pm

#pyhton string methods some logical interview qestion & answers

#first and last letter capital
a = input("Enter the string:")
b = a[:-1].capitalize()+a[-1].capitalize()
print(b)

#fisrt 2 lower and last 2 upper and every 4th letter caps
a = input("Enter the string:")
b = a[:2].lower()+a[::4].upper()+a[-2:].upper()
print(b)

#emailformat
a = input("enter your email id: ")
b = a[0].islower() and a[0].isalpha() and a.endswith("@gmail.com")
print(b)

#every 2nd ltr caps
a = input("enter the string : ")
b = a[0].lower()+a[1].upper()+a[2].lower()+a[3].upper()+a[4].lower()+a[5].upper()+a[6].lower()+a[7].upper()+a[8].lower()+a[9].upper()+a[10].lower()+a[11].upper()
print(b)

#replace the index to that value
a = input("enter your name: ")
find_position = a.rindex("")
b = input()
replace_word = input("replace letter :")
x = a.replace("find_position", "replace_word")
print(x)












