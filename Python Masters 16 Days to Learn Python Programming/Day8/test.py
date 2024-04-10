from collections import Counter , defaultdict
number =[3,3,4,5,5,12,8,6,73,2,12]
sentense = "you will never win if you never begin"
print(Counter("mississippi"))
print(Counter(sentense.split()))
print(Counter(number))


series = Counter([1,1,1,1,1,2,2,2,3,3,3,3,4,4,4])
print(series.most_common())
print(list(series))

# my_dict = {'one': 'green', 'two': "blue", "tree": "red"}
# print(my_dict["two"])
my_dict = defaultdict(lambda : "nothing")
my_dict["one"]= "green"
