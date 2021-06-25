import math

import datetime as dt


pi = 3.144444444
a = 230
b = -484.43434
c = -999.999


print(abs(c))
print(int(c))
print(int(abs(c)))
print(round(pi,4))
print(bin(a))
print(hex(a))
print(oct(a))
print(max(pi,a,b,c))
print(type(pi))
print(type(a))
print(type(str(b)))


g = -816.9789
print(math.floor(g))

username = "Ram"


print(f"Hello {username}")




aa = 255
print(hex(aa))



zz = complex(2,-4)
print(zz)


print(zz.real)

print(zz.imag)


#strings

first_name = "king"
initial_name = "M"
last_name = "Ram"
full_name = first_name +" "+ initial_name +" " + last_name
print(full_name)

s1 = ""
s2 = " "
s3 = "A B C"
print(len(s1))
print(len(s2))
print(len(s3))




s4= "Aspire Systems as da'ta analytics and artificial intelligence"

print("t" in s4)
print("T" in s4)
print("T" not in s4)

print("-" * 15)

print(s4[0])

print(s4[20:39])

print(s4[0:44:3])


print(min(s4))
print(max(s4))

print(s4.index("s"))


print(s4.index("a",22,44))

print(s4.capitalize())

print(s4.upper())




#String with methods


today = dt.date.today()

lastjobless_date = dt.date(2019,12,31)

print(today)
print(lastjobless_date)
print(lastjobless_date.day)


print(f"{lastjobless_date:%A, %B %d, %Y}")



time = dt.time()
print(time)


right_now = dt.datetime.now()
print(right_now)


newyear = dt.date(2021,6,24)
janaki = dt.date(2019,12,19)

days_gone = janaki - newyear

print(days_gone)




now = dt.datetime.now()
birthdatetime = dt.datetime(1993,6,20,20)
age = now - birthdatetime
print(age)

print(type(age))

here_now = dt.datetime.now()
utc_now = dt.datetime.utcnow()
timediff = (utc_now - here_now)

print(f"my time    :   {here_now:%I:%M:%p}")
print(f"utc time      :{utc_now:%I:%m:%p}")
print(f"differrence    :{timediff}")