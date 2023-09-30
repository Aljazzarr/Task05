a_Seperator = "---------------------------------------------------------------------------"
# 01
print("Question No.01")
print("Please Enter Your Name ,Age ,street, city, and country")
print(a_Seperator)
# 02
print("Question No.02")
user_Name = "Lama"
user_Age = "20"
user_Street = "159"
user_city = "Gaza"
user_Country = "Palestine"
full_Data = f'"Name: {user_Name}" \n "Age: {user_Age}" \n "Address: {user_Street}, {user_city}, {user_Country}" '
print(full_Data)
print(a_Seperator)
# 03
print("Question No.03")
print("# Hello Lama I Modified Your Age Based on the Task question no.3")
print(
    f'" Hello {user_Name} Yor Age is {int(user_Age) - 5} Years Old ,Your \n Address is {user_Street}, {user_city}, {user_Country}"')
print(a_Seperator)
# 04
print("Question No.04")
print(f"{type(user_Name)}, {type(user_Age)}, \n {type(user_Street)}, {type(user_city)},\n {type(user_Country)} ")
print(a_Seperator)
# 05
print("Question No.05")
print(f' "Hello {user_Name}, How Are You \\ ""\" Your Age is "{user_Age}"" + \n And Your Country is {user_Country} ')
print(a_Seperator)
# 06
print("Question No.06")
print(f' "Hello {user_Name}, How Are You \\ \n ""\" Your Age is "{user_Age}"" + And\n Your Country is {user_Country} ')
print(a_Seperator)
# 07
print("Question No.07")
name = 'ITF Gsg Python'
print(f'first letter is "{name[0]}"')
print(f'Third letter is "{name[2]}"')
print(f'Last letter is "{name[-1]}"')
print(a_Seperator)
# 08
print("Question No.08")
print((name[-3:]))
print((name[:3]))
print((name[0:7:2]))
print((name[-1:6:-1]))
print(a_Seperator)
# 09
print("Question No.09")
name = "$&$&Mohammed$&$&"
print((name[4:-4]))
print(a_Seperator)
# 10
print("Question No.10")
msg = "I %7 Python And Although I %7 GSG with Trainer Eng-Zakaria"
msg = msg.replace("%7", "love")
print(msg)
print(a_Seperator)
# 11 + 12
print("Question No.11+12")
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num5.zfill(5))
print(num6.zfill(5))
print(a_Seperator)
# 13
print("Question No.13")  # two examples
my_String = "i love python with eng zakarya "
print(my_String.capitalize())
print("# Capitalize makes the first letter in the string to uppercase")
print(my_String.title())
print("# Title makes the first letter in Every word in string to uppercase")
first_name = "Hussaine"
print(a_Seperator)
# 14
print("Question No.14")
print("*" * 10 + first_name)
print("*" * 10 + first_name + "*" * 11)
print(first_name + "*" * 11)
print(a_Seperator)
# 15
print("Question No.15")
name_one = "SaMER"
name_two = "Abed"
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())
print(a_Seperator)
# 16
print("Question No.16")
print(name_one.isupper())
print(name_two.islower())
print(a_Seperator)
# 17
print("Question No.17")
print(name_one.startswith("S"))
print(name_two.endswith("HD"))
print(a_Seperator)
# 18
print("Question No.18")
msg = "I Love Python And Although I Love GSG with Eng. Zakaria"
print(f'Number of <Love> is {msg.count("Love")}')
print(f'Number of <t> is {msg.count("t")}')
print(a_Seperator)
# 19
print("Question No.19")
msg = "I %7 Python And Although I %7 GSG with Zakaria"
msg = msg.replace("%7", "love", 1)
print(msg)
print(a_Seperator)
print("Question No.20")
# palindrome  => Palindrome Strings are a sequence of alphabets which when reversed, stay similar to the original
# sequence.
# Symmetrical => A string that, when broken into two halves, produces two similar sequences of characters
test1 = "ZakZak"
test2 = "Zakaria"
test3 = "A war at Tarawa."
test4 = "madam"
test3 = (test3.casefold().lower()).replace(" ","").replace(".","")
print(test3)
half1 = len(test1) // 2
half2= len(test2) // 2
half3= len(test3) // 2
half4= len(test4) // 2
# 1. check if symmetrical (both halves are the same)=>
######################## in  case of true ###################
# will check  if
# is it palindrome(can read reverse) in case of true will print(symmetrical and palindrome  )
# in case of false will print (symmetric but not palindrome)
###################### in case of false ######################
# print "ZakZak" is not a symmetrical and check if palindrome again
if test1[0:half1] == test1[half1::]:  # check if symmetrical
    if test1 == test1[::-1]:  # check the symmetrical st if palindrome also
        print("ZakZak is symmetrical,And ZakZak is palindrome")  # True
    else:
        print("ZakZak is symmetrical, But ZakZak is Not Palindrome.")  # False
else:
    if test1 == test1[::-1]:
        print("ZakZak is not Symmetrical, But ZaZak is Palindrome")
    else:
        print("ZakZak is not Symmetrical, And ZaZak is Not Palindrome")
print (a_Seperator)
####
if test2[0:half2] == test2[half2::]:  # check if symmetrical
    if test2 == test2[::-1]:  # check the symmetrical st if palindrome also
        print("Zakaria is symmetrical,And Zakaria is palindrome")  # True
    else:
        print("Zakaria is symmetrical, But Zakaria is Not Palindrome.")  # False
else:
    if test2 == test2[::-1]:
        print("Zakaria is not Symmetrical, But Zakaria is Palindrome")
    else:
        print("Zakaria is not Symmetrical, And Zakaria is Not Palindrome")
print (a_Seperator)
####
if test3[0:half3] == test3[half3::]:  # check if symmetrical
    if test3 == test3[::-1]:  # check the symmetrical st if palindrome also
        print("madam, is symmetrical,And madam, is palindrome")  # True
    else:
        print("madam, is symmetrical, madam is Not Palindrome.")  # False
else:
    if test3 == test3[::-1]:
        print("madam, is not Symmetrical, But madam, is Palindrome")
    else:
        print("madam is not Symmetrical, And madam is Not Palindrome")
print(a_Seperator)
if test4[0:half4] == test4[half4::]:  # check if symmetrical
    if test4 == test4[::-1]:  # check the symmetrical st if palindrome also
        print("madam, is symmetrical,And madam is palindrome")  # True
    else:
        print("madam, is symmetrical, But madam is Not Palindrome.")  # False
else:
    if test4 == test4[::-1]:
        print("madam, is not Symmetrical, But madam, is Palindrome")
    else:
        print("madam is not Symmetrical, And madam is Not Palindrome")
print(a_Seperator)
print("*****without Any function or loop just using slicing and indexing wit conditional if**** ")
print(a_Seperator)