print("The Love Calculator is calculating your score...")
name1 = input("name1:") # What is your name?
name2 = input("name2:") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name3 = (name1 + name2).lower()

count = 0
target_letters = "truelove"

for letter in target_letters:
    count += name3.count(letter)

print("Count:", count)

# #Combine the counts to make a 2-digit number
# love_score = true_count * 10 + love_count

# #Determine the message based on the love score
# if love_score < 10 or love_score > 90:
#     message = f"Your score is {love_score}, you go together like coke and mentos."
# elif 40 <= love_score <= 50:
#     message = f"Your score is {love_score}, you are alright together."
# else:
#     message = f"Your score is {love_score}."

# print(count)