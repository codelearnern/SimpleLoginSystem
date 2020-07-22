existingAccount = input("Do you have an existing account? ")

if existingAccount.lower() == "yes":
	email_uname = input("Enter your username or email. ")
	pwdYes = input("Enter your password. ")

	emailCheck = open("email.txt", "r")
	unameCheck = open("unames.txt", "r")
	pwdCheck = open("pwds.txt", "r")

	emailList = []
	unameList = []
	pwdList = []

	for line in emailCheck.readlines():
		emailList.append(line.strip())
	for line in unameCheck.readlines():
		unameList.append(line.strip())
	for line in pwdCheck.readlines():
		pwdList.append(line.strip())

	emailCheck.close()
	unameCheck.close()
	pwdCheck.close()

	if email_uname in emailList or email_uname in unameList:
		if pwdYes in pwdList:
			print("You're signed in!")
		else:
			print("Sorry your password doesn't match.  To sign in run the program again.")
	else:
		print("Sorry, your email/username/password didn't match.  To sign in again run the program again.")


elif existingAccount.lower() == "no":
	print("Now you are gonna sign up")
	email = input("What is your email? ")
	unameNo = input("What do you want your username to be? ")
	pwd = input("What do you want your password to be? ")
	repeatPwd = input("Repeat your password? ")
	if repeatPwd != pwd:
		print("You have to enter same password as what you entered, run the program again.")
	else:
		emails = open("email.txt", "a")
		unames = open("unames.txt", "a")
		pwds = open("pwds.txt", "a")

		emails.write(f"{email}\n")
		unames.write(f"{unameNo}\n")
		pwds.write(f"{pwd}\n")

		emails.close()
		unames.close()
		pwds.close()

		print("Okay, you're now signed up!  Run the program again to login.")

else:
	print("You have to answer yes or no, run the program again.")
