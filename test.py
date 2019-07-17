import random

secret = random.randint(1,10)
temp = input("give me a guess: ")
guess = int(temp)

while guess != secret:
    temp = input("WRONG, give me a new guess: ")
    guess = int(temp)
    
    if guess == secret:
        print("Yep")
    else:
        print("Nope")

print("Thats all")


for i in range(10):
    if i % 2 != 0:
        print(i)
        continue
    i+=2
    print(i)


empty = []
empty.append(2)
