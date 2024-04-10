import random
list_of_answers = ["Yes - definitely.",
"It is decidedly so.",
"Without a doubt.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]

question = input("Ask you question and the great Jinn will answer! :\n")
answer = random.randint(1,8)
print(f"The Great Jinn says : {list_of_answers[answer]}")