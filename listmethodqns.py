    # Author     : Sanjaykumar.M
    # Date       : 07-02-2024
    # Description: python list methods using some logic questions
    # Batch time : 4.00 - 7.00pm

# python list methods using some logic questions

#accending alphabet?

a = ["jay","sanjay","surya", "zam", "kumar", "lol", "art", "power", "cat", "hi", "man"]
a.sort(reverse=True)
print(a)

#decending alphabet?

a = ["jay","sanjay","surya", "zam", "kumar", "lol", "art", "power", "cat", "hi", "man"]
a.sort()
print(a)

#assending order nos?

a = [33, 55, 56, 89, 90, 23, 21, 11, 3]
a.sort()
print(a)

#decending order nos?

a = [33, 55, 56, 89, 90, 23, 21, 11, 3]
a.sort(reverse=True)
print(a)

#find max and min no?

a = [33, 55, 56, 89, 90, 23, 21, 11, 3]
print("List =", a)
b = max(a)
print("maximum number :", b)
c = min(a)
print("minimum number :", c)

#change the order of nos?

a = [1, 2, 3, 4]
a.reverse()
print(a)

#add anyone string/no inside the existing list by user input?

a = ["jay","sanjay","surya", "zam", "kumar"]
x = input("add anyone string/number : ")
a.append(x)
print(a)

#how to find number of element in list?

a = ["jay", "sanjay", "surya", "zam", "kumar", "san", "man"]
x = len(a)
print(x)

#how to find largest and smallest no in list?

a = [33, 55, 56, 89, 90, 23, 21, 11, 3]
x = max(a)
y = min(a)
print("largest no in the string :", x)
print("smallest no in the string :", y)

#how to access the list?

a = ["jay","sanjay","surya", "zam", "kumar"]
x = int(input("access the index :"))
y = a[x]


#how to modify the list?

a = ["jay", "sanjay", "surya", "zam", "kumar"]
x = int(input("access the index :"))
y = a[x]
print("index value :", y)
m = str(input("modified the index value to :"))
a[x] = m
print(a)

#how to add the list

a = ["jay","sanjay","surya", "zam", "kumar"]
b = [33, 55, 56, 89, 90, 23, 21, 11, 3]
a.append(b)
print(a)

#how to remove the duplicate in list?

a = ["jay", "sanjay", "surya", "zam", "kumar", "jay", "sanjay", "surya", "zam", "kumar"]
x = list(set(a))
print(x)

#find the 1st nd last element in list?

a = ["jay", "sanjay", "surya", "zam", "kumar", "jay", "sanjay", "surya", "zam", "kumar"]
x = a[0]
y = a[-1]
print("first element in the list :", x)
print("last element in the list: ", y)










