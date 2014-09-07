import re
import codecs
import sys
sys.stderr.write('ouverture du fichier',)
fichier=codecs.open(sys.argv[1],"r","utf-8")
text=fichier.read()
fichier.close()
ngram=5
text=text.lower()
pc=[".",",",";",":","?","!","-","--","..."]
sys.stderr.write('remplacement de la ponctuation')
for ponct in pc:
    text=text.replace(ponct,"")
    text=text.replace("'"," ")
    text=text.replace("  "," ")

fich=text.splitlines()


for line in fich:
    line=line.strip()
    espace= line.count(" ")
    i=0
    
    while i <= len(line)-ngram-espace:
        if line[i]!=" ":
            lettres=0
            lettreslocales=0
            j=0
            type=""
            dict={}
            while lettres<ngram:
                if line [i+j] != " ":
                    print line [i+j].encode('utf8'),
                    lettres+=1
                    lettreslocales+=1
                    
                else:
                    type=type+str(lettreslocales)+"."
                    lettreslocales=0
                
                j+=1
            type=type+str(lettreslocales)
            print
            i=i+1
            print type
            
        i=i+1
        #print line , espace
        
