import random
choix=0
n=4
k=10
d=3
choixoption=10
choixjeu=10

while choix!=3 :
    for i in range(30) :
        print("\n")
    if choix==0 :
        print("1. Jouer")
        print("2. Options")
        print("3. Quitter")
        if choixoption==1 or choixoption==2 or choixoption==3 :
            choix=2
        elif choixjeu==1 :
            choix=2
            choixjeu=10
        elif choixjeu==2 :
            choix=1
        else :
            choix=int(input())

        if choix==1 :
            for i in range(30) :
                print("\n")
            code=list(range(n))
            for i in range(n):
                rand_numb = random.randint(1, 9)
                while rand_numb in code[:i]:
                    rand_numb = random.randint(1, 9)
                code[i] = rand_numb

            good=0
            almostgood=0
            while k>0 and good!=n :
                good=0
                almostgood=0
                print("Il vous reste",k,"chance")
                print("Entrez votre proposition : ")
                liste=[]
                proposition=input()
                while len(proposition)!=n :
                    proposition=input()
                for i in proposition :
                    liste.append(int(i))
                if d==1 :
                    print("\n - signifie que le chiffre se trouve dans le code mais pas a cette place \n * signifie que le chiffre n'est pas dans le code \n")
                if d==4 :
                    for i in range(n) :
                        if liste[i]==code[i] :
                            good=good+1
                elif d==3 :
                    for i in range(n) :
                        for j in range(n) :
                            if liste[i]==code[j] :
                                good=good+1
                elif d==2 :
                    for i in range(n) :
                        for j in range(n) :
                            if liste[i]==code[j] :
                                if i==j :
                                    good=good+1
                                else :
                                    almostgood=almostgood+1
                elif d==1 :
                    listebon=list(range(n))
                    for l in range(n) :
                        listebon[l]=0
                    for i in range(n) :
                        for j in range(n) :
                            if liste[i]==code[j] :
                                if i==j :
                                    good=good+1
                                    listebon[i]=liste[i]
                                else :
                                    almostgood=almostgood+1
                                    listebon[i]='-'
                        if listebon[i]==0 :
                            listebon[i]='*'
                if d==1 :
                    print(listebon)
                elif d==2 :
                    print("Il y a",good,"chiffres bien placer et",almostgood,"chiffres mal placer")
                elif d==3 or d==4 :
                    print("Il y a",good,"chiffres bon")
                if good==n :
                    print("Bravo vous avez gagné !")
                else :
                    k=k-1
                if k<1 :
                    print("Vous avez perdu")
            print("Voulez vous rejouer ?")
            print("1. Oui avec d'autres parametres")
            print("2. Oui avec les mêmes parametres")
            print("3. Non je veut fermer le jeu")
            choixjeu=10
            while choixjeu<1 or choixjeu>3 :
                choixjeu=int(input())
            if choixjeu==1 :
                choix=0
            elif choixjeu==2 :
                choix=0
            else :
                choix=3
            
        elif choix==2 :
            for i in range(30) :
                print("\n")
            print("1. Modifier la taille du code. Actuellement :",n)
            print("2. Modifier le nombre de coup maximal. Actuellement :",k)
            print("3. Modifier la difficulté. Actuellement :",d)
            print("0. Revenir au menu précédent")
            choixoption=10
            while choixoption<0 or choixoption>3 :
                choixoption=int(input())
            if choixoption==1 :
                n=int(input("Entrez le nombre de chiffres que vous souhaitez dans votre code (compris entre 1 et 9) : "))
                while n<1 or n>9 :
                    n=int(input("Entrez le nombre de chiffres que vous souhaitez dans votre code (compris entre 1 et 9) : "))
                choix=0
            elif choixoption==2 :
                k=int(input("Entrez le nombre de coup avant que la partie ne se termine : "))
                choix=0
            elif choixoption==3 :
                d=int(input("Choissisez la difficulté : \n 1. Facile \n 2. Moyen \n 3. Difficile \n 4. Expert \n"))
                while d<1 or d>4 :
                    d=int(input("Choissisez la difficulté : \n 1. Facile \n 2. Moyen \n 3. Difficile \n 4. Expert \n"))
                choix=0
            else :
                choix=0
exit()
