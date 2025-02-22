# using Arithmetic Operators
dosa=30
quantity=int(input("how many dhosa you want:"))
print(dosa*quantity)
print(type(dosa))

# using assignment operators
dosa+=10
print(dosa)
print(type(dosa))

# using comparison operators
your_dosa=input("Enter your number:")
print(dosa>=10)

#using not operator
print(not(dosa==10))
print(type(dosa))

# using identity operators
hotel=dosa
print(dosa is hotel)
print(type(hotel))
print(dosa is not hotel)

# using membership operator
fruits="apple"
print("banana" in fruits)
print(type(fruits))
print("banana" not in fruits)

# using string array
print(fruits[1])
print(fruits[3:5])
print(fruits[2:])
print(fruits[:3])
print(fruits[-1])
print(fruits[-5:-3])
print(type(fruits))

# upper method
print(fruits.upper())

# strip method
print(fruits.strip())

#replace method
print(fruits.replace("a","b"))

#split method
names="python"#"java"#"c#""c++"
names=names.split(",")
print(names)

# list
shop=["apple","banana","orange","kiwi"]
print(type(shop))
print(shop)

# List allow duplicate
shop=["apple","banana","orange","kiwi","apple"] 
print(shop)

# list is changable
shop=["apple","banana","orange","kiwi","apple"]
shop[0]="green apple"
print(shop)

# accessing the list
print(shop[2:5])

# using append method
shop.append("mango")
print(shop)

# using empty list
idly=[]
idly.append("rice")
print(idly)

# using insert element
shop.insert(1,"guava")
print(shop)

# using remove element
shop.remove("kiwi")
print(shop)

# using pop elements
shop.pop(3)
print(shop)
shop.pop(-1)
print(shop)

# using count method
gender=["gir;","boy","male","female","women","women","women"]
x=gender.count("women")
print(x)

# using clear method
gender.clear()
print(gender)

#using sort method
numbers=[10,3,4,7,6,5]
numbers.sort()
print(numbers)

# using reverse method
numbers.reverse()
print(numbers)

# using count(string,begin,end) method
y="male"
z=y.count('m')
print(z)

# using isdigit method
s="1234"
f="122-23-45"
g=s.isdigit()
h=f.isdigit()
print(g)
print(h)

# using isidentifier()
abc="abcdef"
abc1=abc.isidentifier()
print(abc1)






