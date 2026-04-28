print("**********Welcome to the Intractive personal Data Collector!**********")
name=str(input("Enter you name:"))
age=int(input("Enter your age:"))
height=float(input("Enter your height in feets:"))
Fav_num=int(input("Enter your Favourite number:"))

print("**********Thank you for your information",name,":)**********")

print("Your name is:",name,".{Data Type is:",type(name),"}{Memory Address:",id(name),"}")
print(name,"your age is:",age,".{Data Type:",type(age),"}{Memory Address:",id(age),"}")
print("and your height is:",height,".{Data Type:",type(height),"}{Memory Address:",id(height),"}")
print("and nice to see your favourite number:",Fav_num,".{Data Type:",type(Fav_num),"}{Memory Address:",id(Fav_num),"}")

print(name,"Your approx birth year is this:",2026-age,"")
ap_h=int(height)
print(name,"your approx height is:",ap_h,"feet")

print("Hello",name,"Your age is",age,"& your approx birth year is",2026-age,"and your hight is",height,"and your favourite number is",Fav_num,".")

print("**********Thank you for using my application, Have a Good Day",name,".**********")