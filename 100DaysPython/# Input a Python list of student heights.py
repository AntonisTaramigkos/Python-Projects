# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
sum_height = 0
for heights in student_heights:
  sum_height += heights

num_of_student = len(student_heights)
average_height = round(sum_height/num_of_student)

print(sum_height)
print(num_of_student)
print(average_height)