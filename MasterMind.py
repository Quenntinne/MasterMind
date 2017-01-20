import random
n=0
k=0
while n<1 or n>9 :
    n=int(input("Entrez le nombre de chiffres que vous souhaitez dans votre code (compris entre 1 et 9) : "))
k=int(input("Entrez le nombre de coup avant que la partie ne se termine : "))
code=list(range(n))
for i in range(n):
    rand_numb = random.randint(1, 9)
    while rand_numb in code[:i]:
        rand_numb = random.randint(1, 9)
    code[i] = rand_numb
print("[DEBUG]",code)

good=0
while k>0 and good!=n :
    good=0
    print("Il vous reste",k,"chance")
    print("Entrez votre proposition : ")
    liste=[]
    proposition=input()
    for i in proposition :
        liste.append(int(i))
    for a in range(len(liste)):
        if liste[a]==code[a]:
            good=good+1
    print("Il y a",good,"chiffres bon")
    if good==n :
        print("Bravo vous avez gagné !")
    else :
        k=k-1
    if k<1 :
        print("Vous avez perdu")
