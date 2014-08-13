#module pour g�rer les expressions r�guil�res
import re
#module qui contient des m�thodes et des fonctions pour g�rer les encodages
import codecs
#module qui contient des m�thodes et des fonctions pour g�rer le syst�me
import sys
#ouvrir le fichier qui est dans la 2�me position
fichier=codecs.open(sys.argv[1],"r","utf-8")
#lire le text
text=fichier.read()
#fermer le fichier
fichier.close()
#la variable ngram vaut la valeur 5
ngram=5
#mettre tout le texte en muniscule
text=text.lower()
#liste de ponctuation dans le texte
pc=[".",",",";",":","?","!","-","--","..."]
# boucle pour lire chaque ponct dans la liste pc
for ponct in pc:
    #remplacer dans text ponct par rien
    text=text.replace(ponct,"")
    #remplacer dans text "'" par espace
    text=text.replace("'"," ")
    #remplacer dans text "  " (les deux espaces) par " " (un seul espace)
    text=text.replace("  "," ")

# d�couper le fichier par text
fich=text.splitlines()


# boucle pour lire chaque line dans fich
for line in fich:
    # enlever les blancs dans line
    line=line.strip()
    #compte le nombre des espaces dans la line
    espace= line.count(" ")
    #initier le compteur pour la boucle while
    i=0
    #tant que i est infierure ou egale � la longueur de line - ngram -espace
    while i <= len(line)-ngram-espace:
        #si l'indice de line[i] est diff�rent d'espace " "
        if line[i]!=" ":
            #la variable lettres vaut la valeur 0
            lettres=0
            #la variable lettreslocales vaut 0
            lettreslocales=0
            #initier le compteur pour la boucle while 
            j=0
            #type vaut ""
            type=""
            #tant que lettres est inf�rieur de ngram
            while lettres<ngram:
                #si l'indice de line est [i+j]est diff�rent d'espace " "
                if line [i+j] != " ":
                    #afficher line [i+j]
                    print line [i+j],
                    #incr�menter la variable
                    lettres +=1
                    #incr�menter la variable  
                    lettreslocales+=1
                #autrement
                else:
                    #la variable type vaut type +str(reconversion en chaine de caract�res)
                    #+un point"."
                    type=type+str(lettreslocales)+"."
                    #la variable lettreslocales vaut 0
                    lettreslocales=0
                #incr�menter la variable j
                j+=1
            #la variable type vaut type +str(reconversion en chaine de caract�res)
            type=type+str(lettreslocales)
            #afficher
            print
            #afficher type
            print type
        #changer la valeur du compteur	
        i=i+1
        #print line , espace
