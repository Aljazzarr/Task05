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
#17
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
