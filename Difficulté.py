print("- signifie que le chiffre se trouve dans le code mais pas a cette place \n * signifie que le chiffre n'est pas dans le code")
    listebon=list(range(n))
    for i in range(n) :
        for j in range(n) :
            if liste[i]==code[j] :
                if d==2 or d==1 :
                    if i==j :
                        good=good+1
                        if d==1 :
                            listebon[i]=1
                else :
                    almostgood=almostgood+1
                    if d==1 :
                        listebon[i]=2
    print(listebon)

'''if d==3 :
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
    for i in range(n) :
        for j in range(n) :
            if liste[i]==code[j] :
                if i==j :
                    good=good+1
                    listebon[i]=1
                else :
                    almostgood=almostgood+1
                    listebon[i]=2
    print(listebon)'''
