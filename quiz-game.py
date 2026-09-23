print("Welcome to my Computer Science Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is the time complexity of binary search? ")
if answer.lower() == "o(log n)":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does HTTP stand for? ")
if answer.lower() == "hypertext transfer protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which data structure follows the LIFO principle? ")
if answer.lower() == "stack":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the main purpose of an operating system? ")
if answer.lower() == "manage computer resources":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does SQL stand for? ")
if answer.lower() == "structured query language":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which number system do computers primarily use? ")
if answer.lower() == "binary":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does API stand for? ")
if answer.lower() == "application programming interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which sorting algorithm has an average time complexity of O(n log n)? ")
if answer.lower() in ["merge sort", "quicksort", "quick sort"]:
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 8) * 100) + "%.")
