def square(N):
    for i in range(N+1):
        #generate the squares of numbers from 0 to N 
        yield i*i

def even_numbers(N):
    for i in range(0, N+1):
        if i%2 == 0: #checking is number divided by 2 without the reminder  
            yield i 

def numbers_divide_by_12(N):
    for i in range(0, N+1):
        if i%4 == 0 and i%3 == 0: #checking is number divided by 3 and by 4 without the reminders   
            yield i 

def squares(a, b):
    for i in range(a, b + 1): #generate the squares of numbers between a and b
        yield i * i

def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("write the last number for generating the sequences of the squares > "))
k = int(input("write the last number for generating the sequences of the even numbers > "))
c = int(input("write the last number for generating the sequences of the numbers divisible by 4 and 3 > "))
a,b = map(int, input("write two numbers for generating the sequences of the squares between them > ").split())
d = int(input("write number for returning all numbers from that down to 0 > "))

print("-----------------------Task 1----------------------------------")
for i in square(n):
    print(i, end=' ')
print("\n")
print("-----------------------Task 2----------------------------------")
print(*even_numbers(k), sep=',')
print("-----------------------Task 3----------------------------------")
print(*numbers_divide_by_12(c))
print("-----------------------Task 4----------------------------------")
for j in squares(a,b):
    print(j)
print("-----------------------Task 5----------------------------------")
for i in countdown(d):
    print(i)