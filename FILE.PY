# a = input("Enter a first Number")
# #list = [1,2,3,4,5,6,7,8,9,10]
# for i in range(1,11):
#    # print(i)
#     j = i*int(a)
#     print(j)

#     Input a string of ‘n’ charactersIf the length of string is even, then create a list with split two characters as elements of listIf the length is odd, then the last split of 1 character should be appended with an underscoreFor e.g. 
# Say input is "abcde" ( which has got odd number of characters )Output should be: ["ab","cd","e_"]Say input is "abcd"Output should be: ["ab","cd"]

# from typing import final


# name  = input("Enter a string")
# str_lenth = len(name)

# final_star = []
# if str_lenth %2 == 0:

#     list_str = list(name)
#     print(list_str)

#     print(name[0:2])
    
#     #for i in list_str:
#         #print(i[0:1])

# *a,b = 1,2,3,4,5,6,7,8,9
# print(a)
# print(b)
        
    
    


# elif str_lenth % 2 != 0:
#     pass


# Input a list say [‘a’, ‘b’, ‘c’]
# Create a python program so that below output is displayedOutput as:

# A
# BB
# CCC
    
# input_list = ['a','b','c']
# for i in input_list:
#     print(i)
#     for j in i:
#         print(j)



# n = int(input("Enter number of rows: "))

# a = ['a','b','c']

# for i in range(1,n+1):
#     for j in range(1, i+1):
#         print("%c" %(a), end="")
#     a +=1
#     print()


# for i in input_list:
#     for j in range(0, i+1):
#         print(str(j),end="")
#     print()


# name = input("Enter a name :")
# print(name)
# st1 =[]
# str_len = len(name)

# print(str_len)
# str_list = list(name)
# if str_len % 2 == 0:
#     print("Even")
#     st = (str_list[0:2])
    
#     for i in st:
#         st1.append(i.split(',')[0])
    
#         print(st1)
    
# else:
#     print("Odd")


# Python program to demonstrate
# string slicing

# String slicing
# String ='satish'

# # Using slice constructor
# # s1 = slice(2)
# # s2 = slice(2,4)
# # s3 = slice(4,6)
# strln = len(String)
# if strln %2 == 0:
#     sl =2
#     s1 = slice(sl)
#     print("String slicing")
#     print(String[s1])
#     sl = slice(sl,sl+2)
#     sl+1
    
    # print(String[s2])
    # print(String[s3])


x = "satish"
new_lst = []

for i in range(0, len(x), 2):
    
    new_lst.append(x[i : i+2])
    if len(x) % 2 == 1:
        new_lst.append("__")
    # list_last_str = new_lst[-1:]
    # if len(list_last_str) == 1:
    #    # new_lst.append('_')
    #     pass

print(new_lst)
#print(list_last_str)
