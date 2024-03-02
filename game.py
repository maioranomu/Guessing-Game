
import random

maxtries = 6
tries = 0 

difficultylist = ["1", "2", "3"]
difficulty = input("Qual dificuldade você quer? [1 FACIL | 2 MEDIO | 3 DIFICIL] ")
while difficulty not in difficultylist:
    difficulty = input("Qual dificuldade você quer? [1 FACIL | 2 MEDIO | 3 DIFICIL] ")

if difficulty == "1":
    difficulty = 10
    
elif difficulty == "2":
    difficulty = 50
    
elif difficulty == "3":
    difficulty = 100    




rannum = random.randint(0, difficulty)
print(rannum)
print(f"Advinhe o numero de 0 a {difficulty}")

while tries < maxtries:
    
    guess = input("Qual numero você acha que é? ")
    
    while guess.isalpha() or guess == "":
        guess = input("Qual numero você acha que é? ")
        
    if guess.isdigit():
        guess = int(guess)
        
    if guess == rannum:
        print("Parabéns, você acertou! ")
        break
    
    elif guess < rannum:
        print("Mais")

        tries += 1
    elif guess > rannum:
        print("Menos")

if tries > maxtries:
    print("Você perdeu")