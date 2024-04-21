print("Welcome to my computer Quiz!")

playing = input("DO you wanna play the game? ")

if playing.lower() != "yes":
    quit()

print("Okay lets begin the game baby!")

answer = input("What is the capital city of Nepal? ")
if answer.lower() == "kathmandu":
    print("Correct")
else:
    print("Incorrect")
answer = input("What is the capital city of India? ")
if answer.lower() == "delhi":
    print("Correct")
else:
    print("Incorrect")

answer = input("What is the highest peak of the world? ")
if answer.lower() == "Sagarmatha" or answer.lower() == "Mount Everest":
    print("Correct")
else:
    print("Incorrect")

answer = input("Who is the prime minister  of India?")
if answer.lower() == "Narendra modi":
    print("Correct")
else:
    print("Incorrect")

answer = input("What is the capital city of UK?")
if answer.lower() == "london":
    print("Correct")
else:
    print("Incorrect")
