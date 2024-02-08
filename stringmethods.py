  # Author     : Sanjaykumar.M
  # Date       : 08-02-2024
  # Description: python string methods
  # Batch time : 4.00 - 7.00pm

#47 string methods & some examples!
#capitalize --- first letter capital
a = "sanjayKUMAR"
x = a.capitalize()
print(x)
b = "123sanjayKUMAR"
y = b.capitalize()
print(y)
#casefold ---- all character convert lowercase
a = "SaNjAyKuMaR"
x = a.casefold()
print(x)
#center --- in fn(len, "char")
a = "Sanjaykumar"
x = a.center(40, "*")
print(x)
#count --- no of times present values in fn(value, start , end)
a = "sanjay kumar sanjay kumar sanjay kumar"
x = a.count("sanjay", 12, 35)
print(x)

#encode
X = "My name is Ståle"
a = X.encode()
print(a)
x = "My name is Ståle"
print(x.encode(encoding="ascii",errors="backslashreplace"))
print(x.encode(encoding="ascii",errors="ignore"))
print(x.encode(encoding="ascii",errors="namereplace"))
print(x.encode(encoding="ascii",errors="replace"))
print(x.encode(encoding="ascii",errors="xmlcharrefreplace"))

#endswith---- with the value is lat print--true,false

a = " sanjaykumar"
x = a.endswith("r")
print(x)

#expandtabs ---- spacing tabs

a = "s\ta\tn\tj\ta\ty"
x = a.expandtabs(5)
print(x)

#find --- print position
a = "sanjay kumar sanjay kumar sanjay kumar"
x = a.find("u")
print(x)

#format ---ofter desimal count using
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
a = "my name is {n}, age {a}".format(n="sanjay", a= 25)
print(a)

#index

txt = "Hello, welcome to my world."

print(txt.find("w"))
# print(txt.index("t"))

#isalnum
txt = "compadddddny11112@gmail.com"
x = txt.isalnum()
print(x)

#isalpha

txt = "Company"
x = txt.isalpha()
print(x)

#isascii
txt = "Company123"
x = txt.isascii()
print(x)

#isdecimal

txt = "1234"
x = txt.isdecimal()
print(x)

#isdigit
txt = "50800"
x = txt.isdigit()
print(x)

#isidentifier
txt = "Demo"
x = txt.isidentifier()
print(x)

#islower

txt = "hello world!"
x = txt.islower()
print(x)

#isnumeric

txt = "1223"
x = txt.isnumeric()
print(x)

#isprintable

txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)

#isspace

txt = "  "
x = txt.isspace()
print(x)

#istitle
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

#isupper
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

#join

a = ("san", "san", "san", "san")
x = "jay ".join(a)
print(x)

myDict = {"name": "John", "country": "Norway", "state": "tamilnadu"}
x = " and ".join(myDict)
print(x)

#ljust

a = "s"
x = a.ljust(2)
print(x, "is my name")

txt = "sanjay"
x = txt.ljust(10, "O")
print(x)

#lower

txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

#lstrip
a = "    sanjay    sanjay"
x = a.lstrip()
print(x)

a = ",.,k.,l.,m.,klm,sanjay"
x = a.lstrip(",.klm")
print(x)

#translate
a = "hanjaykumar"
b = str.maketrans("h", "S")
print(a.translate(b))

#partition
a = "my name is sanjaykumar and im studying in hope"
x = a.partition("and")
print(x)
a = "my name is sanjaykumar and im studying in hope"
x = a.partition("found")
print(x)

#replace
a = " i am  sanjaykumar sanjaykumar sanjaykumar sanjaykumar sanjaykumar sanjaykumar"
x =a.replace("sanjaykumar", "rocky", 3)
print(x)

#rfind
#rindex
a = "san van gan jan"
x = a.rfind("jan")
y = a.rindex("jan")
print(x)
print(y)

#rjust

a = "banana"
x = a.rjust(7)
print(x, "is my fav ")
#rpartition

a = "my name is sanjaykumar and im studying in hope"
x = a.rpartition("and")
print(x)

#rsplit
a = "san, vam, dan, gun, tun"
x = a.rsplit(",", 2 )
print(x)

#rstrip
a = "   sanjay    "
x = a.rstrip()
print("my name is ", x, "and")
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)

#split
# a = "i am sanjay"
# x = a.split()
# print(x)

#splitline
a = "i am sanjay\n and sanjay"
x = a.splitlines(True)
print(x)

#startwith
a = "i am sanjay"
x = a.startswith("i")
print(x)

#strip
a = "   sanjay        "
x = a.strip()
print(x)

#swapcase
a = "SANJAY kumar"
x = a.swapcase()
print(x)

#title
a = "i am sanjay kumar"
x = a.title()
print(x)

#translate
a = {83: 80}
x = "hello Sam"
print(x.translate(a))

#upper
a = "sanjay"
x = a.upper()
print(x)

#zzfill
a = "01"
x = a.zfill(20)
print(x)