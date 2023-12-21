'''import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','&','*','(',')']
print("Welcome to password generator")
n_letters=int(input("How many letters you want in your password"))
n_symbols=int(input("How many symbole you want in your password"))
n_numbers=int(input("How many numbers you want in your password"))
password_list=[]
for i in range(1,n_letters+1):
    char= random.choice(letters)
    password_list+=char
#print(password)
for i in range(1,n_symbols+1):
    char= random.choice(symbols)
    password_list+=char
#print(password)
for i in range(1,n_numbers+1):
    char= random.choice(numbers)
    password_list+=char
print(password_list)
random.shuffle(password_list)
print(password_list)
password=''
for char in password_list:
    password+=char
print(password)


a={
    "name":"Trupti",
    "age":23,
    "surname":"Ninghot"
}
for i,j in a.items():
   # print(i,j)
    if(type(j)==int):
        print(i)

for i,j in a.items():
    if isinstance(j,int):
        print(i)

dic={}
n=int(input())
for i in range (n):
    key=input("Enter a key")
    value=input("Enter a value")
    dic[key]=value
print(dic)
'''

#Operator overloading example
class Book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
    def __add__(self,other):
        total=self.pages+other.pages
        return Book('All books', total)
    def __str__(self):
        return str(self.pages)
b1=Book('One indian girl', 300)
b2=Book('making india awesome', 200)
b3=Book('half girl', 400)
b4=Book('full', 300)
print('total number of pages', b1+b2+b3+b4)


