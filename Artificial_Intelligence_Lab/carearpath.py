#desion making system 
print("enter the subject of your intrest:")
print("1.maths,2.physics,3.biology,4.programing,5.chemistry,6.electronics,7.AI&DS,8.circuits")
sub1=input("1st subject:")
sub2=input("2nd subject:")
if sub1=="maths" and sub2=="physics"or sub1=="physics" and sub2=="maths":
	print("your sujested carear path is {mechenical engineering}\n")
	
elif  sub1=="chemistry" and sub2=="biology"or sub1=="biology" and sub2=="chemistry":
	print("your sujested carear path is {biotechnology}\n")
	
elif  sub1=="maths" and sub2=="programing"or sub1=="programing" and sub2=="maths":
	print("your sujested carear path is {computer science engineering}\n")
	
elif  sub1=="AI&DS" and sub2=="programing"or sub1=="programing" and sub2=="AI&DS":
	print("your sujested carear path is {AI&DS engineering or AI&ML engineering}\n")
	
elif  sub1=="electronics" and sub2=="circuits"or sub1=="circuits" and sub2=="electronics":
	print("your sujested carear path is {electrical engineering}\n")
	
else  :
	print("your choice refers 2 diffrent streams!!!...\n")
	print("thank you !!!>>> \n")
	
