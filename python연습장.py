# import random

# for i in range(10):
    
#     a = random.randint(1, 400)
#     b = random.randint(1, 400)
#     print(a, b)

students = []
for n in range(10):
    a, b = list(map(int, input().split()))
    students.append(a)
    students.append(b)
    
students.sort()
print(students)