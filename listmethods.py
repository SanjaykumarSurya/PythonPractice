    # Author     : Sanjaykumar.M
    # Date       : 07-02-2024
    # Description: python list methods and some examples
    # Batch time : 4.00 - 7.00pm

# python list methods and some examples

# 12 list methods and examples
#append()

a = ["sanjay", "sanjay","sanjay"]
b = ["sanjay", "sanjay","sanjay"]
a.append("surya")
a.append(b)
print(a)

#clear()

a = ["sanjay", "sanjay","sanjay", "sur"]
a.clear()
print(a)

#copy()

a = ["sanjay", "sanjay","sanjay"]
x = a.copy()
print(x)

#count()

a = ["sanjay", "sanjay","sanjay", "sanjay", "sanjay","sanjay"]
x = a.count("sanjay")
print(x)

#extend()

a = ["sanjay", "sanjay","sanjay", "sanjay", "sanjay","sanjay"]
x = ["ssssssssssssssss", 1, 2, 3]
a.extend(x)
print(a)

#index()

a = ["sanjay","sanjay1","sanjay2", "suray", "surya3", "suray4"]
x = a.index("surya3")
print(x)

#insert()

a = ["sanjay","sanjay1","sanjay2", "suray", "surya3", "suray4"]
a.insert(5,"sssssssssssss")
print(a)

#pop()

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
a.pop(1)
print(a)

#remove()

a = ["sanjay", "surya", "loga", 1, 2, 3]
a.remove(1)
a.remove("sanjay")
print(a)

#reverse()

a = ["sanjay", "surya", "loga", 1, 2, 3]
a.reverse()
print(a)

#sort()

a = ["rnand","queue", "sanjay", "surya", "loga", "zamboo"]
a.sort(reverse=True)
a.sort()
print(a)

#sort in funtion
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW','a', 'sssssssssssss']
cars.sort(key=myFunc)
print(cars)











