print("Quiz do GTA")
user = input("Quer começar? (S/N)")

if user != "S":
    quit()

score = 0

print("Começando...")
print("1- Quem desenvolveu o jogo GTA ? \n (A) Rockstar Games \n (B) Ubsoft \n (C)Activision \n (D)EA \n") 
user = input("Resposta: ")   

if user == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("2- Qual o GTA mais jogado atualmente ? \n (A) GTA Vice City \n (B) GTA San Andreas \n (C) GTA 5 \n") 
user = input("Resposta: ")   

if user == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")


print("3- Qual ano vai lançar o GTA 6? \n (A) 2027 \n (B) 2026 \n (C) 2025 \n") 
user = input("Resposta: ")   

if user == "B":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")


print("4- Em qual ano lançou o GTA San Andreas? \n (A) 2001 \n (B) 2002 \n (C) 2003 \n (D) 2004 \n (E) 2005 \n") 
user = input("Resposta: ")   

if user == "D":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print(f"O quiz acabou... Sua pontuação é: {score}")