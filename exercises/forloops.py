
# FOR LOOPS
# execute a block of code a fixed number of times 

# for x in range(1, 11):
#     print(x)
    
# # reversed version    
# for x in reversed(range(1, 11)):
#     print(x) 

# # it will count by 2
# for x in range(1, 11, 2):
#     print(x) 

#it will stop once reached 13
# for x in range(1, 21):
#     if x ==13:
#         break
#     else:
#         print(x)

# il will skip number 13 only
for x in range(1, 21):
    if x ==13:
        continue
    else:
        print(x)                  
