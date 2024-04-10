#Sum of numbers
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
sum_of_num = 0
for num in range(0, target+1, 2):
    sum_of_num += num
    
print(sum_of_num)

