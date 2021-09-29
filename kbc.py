print("Welcome to the game KBH(koun banega hajarpati)")
print()
name=str(input("Enter your Name:-    "))
print()
Q=["Who is the Presindent of India ?",'what is the capital of india ?',"What is the capital of Maharashtra ?","How many continents are there ?","NavGurukul me koun sa course padhaya jaata hai........"]
A=["Rahul Gandhi","Pranav Mukharji","Ramnath Kovind","Narendra Modi"],["Mumbai","Delhi","Bhopal","Agra"],["Pune","Nagpur","Mumbai","Nasik"],["Five","Seven","Six","Nine"],["Tourism","B.Ed.","Defence","Software Engneering"]
O=[3,2,3,2,4]
f5050=["1 Pranav Mukharji\n2 Ramnath Kovind","1 Bhopal \n2 Delhi","1 Pune\n 2 Mumbai","1 Five\n2 Seven","1 Defence \n2 Software Engineering "]
M=1000
b=1
fifity=0
total=0
for i in range(len(A)):
	print("Rs",M,"ke liye!")
	print(name,"Apka sawal hai..")
	print("Q",b,"."," 	 ",Q[i])
	b+=1
	c=1
	for x in A[i]:
		print(c," ",x)
		c+=1
	guess=int(input("plz choose correct option.:-    "))
	if guess==(O[i]):
		print("Contrats!")
		print("you are right.")
		total+=M
	elif guess==5050 and fifity==0:
			for x in f5050:
				if x== f5050[i]:
					print(x)
					guess1=int(input("plz choose correct option:-    "))
					if guess1==2:
						print("Contrats!")
						print("you are right.")
						total+=M
						fifity+=1
					else:
						print("wrong Answer.")
						print("aap Rs",total,"jeet gye.")
						print("Sorry!, aap game se bahar ho gye.")
			break
	elif guess==5050 and fifity!=0:
		print("Sorry!, aap ne lifeline pahilehi use kr di")
		print("aap Rs",total,"jeet gye.")
		print("Sorry!, aap game se bahar ho gye.")
		break
	else:
		print("wrong Answer.")
		print("aap Rs",total,"jeet gye.")
		print("Sorry!, aap game se bahar ho gye.")
		break
	M+=1000
	if M==6000:
		print("Thank you",name," for playing.")
		print("aap Total Rs",total,"jeet gye.")
		break
	print()