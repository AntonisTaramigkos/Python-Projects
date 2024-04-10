# # # # Define a function called myfunc that takes in a string,
# # # and returns a matching string where every even letter is uppercase, 
# # # and every odd letter is lowercase. Assume that the incoming string only contains letters, 
# # # and don't worry about numbers, spaces or punctuation. The output string can start with either
# # #  an uppercase or lowercase letter, so long as letters alternate throughout the string.def 

# # # def myfunc (string):
# # #     new_string  = []
    
# # #     for index, letters in enumerate(string):
# # #         if index %2 == 0 :
# # #             new_string.append(letters.upper())
# # #         else:
# # #             new_string.append(letters.lower())
        
# # #     return "".join(new_string)
    
# # # def myfunc(string):
# # #     result = ""
# # #     for i in range(len(string)):
# # #         if i % 2 == 0:
# # #             result += string[i].upper()
# # #         else:
# # #             result += string[i].lower()
# # #     return result
# # # x = myfunc ("my name is antonis")
# # # print(x)

# # # def mydef(string):
# # #   new_string_list = string.split()
  
# # #   if new_string_list[0][0] == new_string_list[1][0]:
# # #     return True
# # #   else:
# # #     pass
# # #   return False
  
# # # print(mydef('Levelheaded Llama'))
# # # x = mydef('Crazy Kangaroo')
# # # print(x)

# # def makes_twenty(n1,n2):
# #   if (n1+n2) == 20: 
# #     return True 
# #   elif n1 == 20 or n2 == 20:
# #     return True
# #   else:
# #     False

# # print(makes_twenty(20,10)) 
# # print(makes_twenty(12,8)) 
# # print(makes_twenty(2,3))

# def old_macdonald(name):
    
#     new_name = name[0].capitalize() + name[1:3] + name[3].capitalize() +name[4:]
#     return new_name

# print(old_macdonald("antonis"))

# def master_yoda(text):
#     # text = text.split()
#     # x1 = text[::-1]
#     return " ".join(text.split()[::-1])


# x = master_yoda("home am I")
# print(x)   


# # Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# # has_33([1, 3, 3]) → True
# # has_33([1, 3, 1, 3]) → False
# # has_33([3, 1, 3]) → False

# # def has_33(nums):
# #     for n in nums:
# #         if n[n] ==3 and  n[n+1]==3:
# #             print (f"{n} s True")
# #         else:
# #             print(f"{n} s False")
# def has_33(nums):
#     for i in range(0, len(nums)-1):
      
#         # nicer looking alternative in commented code
#         if nums[i] == 3 and nums[i+1] == 3:
    
#         # if nums[i:i+2] == [3,3]:
#             return True  
    
#     return False

def paper_doll(str):
    # new = [l*3 for l in str]
    return "".join([l*3 for l in str])

print(paper_doll('Hello') )
        

