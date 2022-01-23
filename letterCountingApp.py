#welcome the user
print("Welcome to the letter counting app \n")

#collet first name and second name from the user
first_name = input("Enter your first name here: ")
second_name = input("Enter your second name here: ")

#intro. program to the user
print("Hey " + first_name + "! \n")
print("I am a bot from roktech.org, I will count for you the number of letter in a given message \n")

#accept msg input from user and count the letter
message = input("Give me a message")
message = message.lower()
letter = input("Which letter do you want me to count? ")
msg_count = message.count(letter)

print("counting...")
print("counting is completed... Hit the enter or return key to continue")
input()

#display the results to the user
print(letter + " occured in your message " + str(msg_count) + " times ")
print(f"Goodbye {second_name}!")