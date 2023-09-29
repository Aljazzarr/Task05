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