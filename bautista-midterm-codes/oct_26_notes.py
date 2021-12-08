#Multiline
#print("test\ntest2\ntest3")

#print(""" 
#         awesome 
# """)

#Typecasting
#print(str(1) + "a" + str(2) + "b")

#x = 3.14
#print(int(x)) 
#output: 3

#y = 3
#print(float(y))
#output: 3.00

#print(Hello Katy\'s Friend)
#backslash to display the single quote


#age = 20
#age_category = "Legal Age" if age >= 18 else "Not Legal Age"
#print(age_category)

#age = 20
#age_category = "Legal Age" if (age >= 18 and age <= 59) else "Not Legal Age"
#print(age_category)

#list = [["teddy bear", "candy", "alcohol", "masks"], ["glass", "toy", "wallet"], ["cup", "picture", "chair", "phone"]]
#print(list[0][2])  # 2-dimensional array [y-axis] [x-axis]
#print(list[2][1][1])  # [y-axis][x-axis][index of that word]

#list = [["teddy bear", "candy", "alcohol", "masks"], ["glass", "toy", "wallet"], ["teddy bear", "candy", "alcohol", "masks" ["cup", "picture", "chair", "phone"]]]
#print(list[2][1][2])  # [y-axis][x-axis][inside x-axis]

#sentence = "printing words one-by-one"
#for char in sentence:
#    print(char)

#for num in range (10): # ranges only from 0 to 9
#    print(num)
#for num in range (1, 11): # ranges from 1 to 10
#    print(num)

#list = ["teddy bear", "candy", "alcohol", "masks"]
#for items in list:
#    print(items) # printing the items inside the list

#list = [["teddy bear", "candy", "alcohol", "masks"], ["glass", "toy", "wallet"]]
#for items in list:
#    for inner_items in items:
#        print(inner_items)
#for y in range(len(list)):
#    for x in range(len(list[y])):
#        print(list[y][x])

# len(items) = 3
# len(items[y]) = 4

#for y in range(5):
#    print("OUTER " + str(y))
#    for x in range(3):
#        print("INNER")

#username = "different_admin"
#if username != "admin":
#    print ("Wrong account")
#    exit()
#print ("Login")