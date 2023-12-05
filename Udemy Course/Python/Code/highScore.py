# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
High_Score = 0

for i in student_scores:
    if i > High_Score:
        High_Score = i 
    else:
        High_Score = High_Score

print(f'The high score in the class is: {High_Score}')
