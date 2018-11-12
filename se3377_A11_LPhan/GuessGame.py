import random
def random_number(min, max):
    numb = random.randint(min, max)
    return numb

count = 0

print("Welcome to guess game!!")
print("what is your name?")
name = input()
print ("Hello ", name, "you will have 7 guesses to win this guess game!")
rn = random_number(-100,100)
print ("Enter a number from -100 to 100")
while count <= 6:
    guess = input ()
    guess = int(guess)
    count = count + 1
    if guess < rn:
        print ("Higher")
    elif guess > rn:
        print ("Lower")
    elif guess == rn:
        f = open('reportpython.txt', 'w')
        print ("Victory")
        print ("you have made ", count, " guesses.")
        f.write(str(name))
        f.write(" ")
        f.write(str(count))
        f.close()
    else:
        break
if count > 7:
    print("Deafeat!")
    print("The correct number is: ", rn)
