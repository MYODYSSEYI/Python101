student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {

}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
  grades = student_scores[student]
  if grades <= 70:
    student_grades[student] = "Fail"
  elif grades > 70 and grades < 81:
    student_grades[student] = "Acceptable"
  elif grades > 80 and grades < 91:
    student_grades[student] = "Exceeds Expectations"
  elif grades > 90:
    student_grades[student] = "Outstanding"

# 🚨 Don't change the code below 👇
print(student_grades)
