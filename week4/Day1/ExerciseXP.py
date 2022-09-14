#Exercise 1------------------------------------
print ("Hello world \n"*4);

#Exercise2----------------------------------
result=(99*99*99)*8;
print(result)

#Exercise3 ---------------------------
#>>> 5 < 3
#False
#>>> 3 == 3
# True
#>>> 3 == "3"
#False
#>>> "3" > 3
#True
#>>> "Hello" == "hello"
#False


#Exercise4 ---------------------------
computer_brand="HP-Probook";
print("I have a {} computer".format(computer_brand));

#Exercise5 ---------------------------
name="Nicodeme";
age=19;
shoe_size=45;
info= "Hello everyone my name is:{} i'm {} years old and my shoe_size is:{}".format(name,age,shoe_size);
print(info);

#Exercise6  ---------------------------
a=5 ;
b=6;
if a>b:
	print("Hello World");


#Exercise7  ---------------------------
number=input("Enter a number in order to check if it is an odd or an even number!");
if (number%2)==0:
	print("{} is an odd number".format(number));
else:
	print("{} is an even number".format(number))

#Exercise8  ---------------------------
My_Name="Nicodeme";
What_is_your_name=input("What's your Name Dear friend?");
if (What_is_your_name==My_Name):
	print("Ohhhh my God !! we got the same name")
else:
    print("Ok thanks {} my name is {}".format(What_is_your_name,My_Name))	


#Exercise9---------------------------
What_is_your_height=input("Enter your height in inches Dear friend?");
if(What_is_your_height>145):
	print("You are tall enougth to ride");
else:
	print("you need to grow some more to ride");


