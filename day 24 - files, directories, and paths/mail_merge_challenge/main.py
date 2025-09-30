#TODO: Create a letter using starting_letter.txt 
with open("./input/letters/starting_letter.txt") as letter:
	invitation_letter = letter.read()

#for each name in invited_names.txt
with open('./input/names/invited_names.txt') as guests:
	guest_list = guests.readlines()
	
#Replace the [name] placeholder with the actual name.
for guest in guest_list:
	formatted_guest = guest.strip()
	invitation_letter_populated = invitation_letter.replace('[name]', formatted_guest)
	
	#Save the letters in the folder "ReadyToSend".
	with open(f"./output/ready_to_send/{formatted_guest}_invite_letter.txt", mode="w") as file:
		file.write(invitation_letter_populated)
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp