#Input a Python list of student heights
inputs = "151 145 179"
student_heights = inputs.split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
students = 0
total = 0
average = 0
# for students in student_heights:
for i in student_heights:
  students += 1


for i in student_heights: 
   total += i  

average = int(total / students)

print(f'total height = {total}')
print(f'number of students = {students}')
print(f'average height = {average}')
