import PyPDF2 as p2
import nltk
import re

PDFfile=open("cvtest3.pdf","rb")
pdfReader= p2.PdfFileReader(PDFfile)
x=pdfReader.getPage(0)
y=pdfReader.getFields("a")
print(x.getContents())
domaine=""
sentence=[]
dico=[]
dicoEXP=[]
dicoSkill=[]
skill=[]
experience=[]
education=[]
compteurEXP=0
nbrExp=0;
compteurEDU=0
nbrEdu=0;
boucle=False

#print(x.extractText())
search_word = "skills"
search_word_count = 0
print( pdfReader.numPages)
for pageNum in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    text = pageObj.extractText()
    search_text = text.lower().split()
    for word in search_text:
        sentence.append(word)

print(sentence)
for value in sentence:

    if value=="skill":
        pos=sentence.index(value)
        print("BLOC DE MOT : *********************************************************************************")
        while(sentence[pos]!="experience" or sentence[pos]!="formation"or sentence[pos]!="education"):
            #print(sentence[pos],pos)
            skill.append(sentence[pos])
            if (sentence[pos] == "experience" or sentence[pos] == "formation" or sentence[pos] == "education"or pos>=len(sentence)-1):
                break
            pos+=1

    elif(value=="experience" and boucle==False):
        pos = sentence.index(value)

        print("BLOC DE MOT : *********************************************************************************")
        while (sentence[pos] != "skill" or sentence[pos] != "formation" or sentence[pos] != "education"):
            print(sentence[pos])
            #dico.append(sentence[pos])
            experience.append(sentence[pos])
            if (sentence[pos] == "skill" or sentence[pos] == "formation" or sentence[pos] == "education"or pos>=len(sentence)-1):
                break
            pos += 1

        for i in range(0,len(experience)):
            if re.findall("\d{4}", experience[i]):
                compteurEXP+=1
                dicoEXP.append(experience[i])
        boucle=True
        nbrExp=compteurEXP//2

    elif (value == "education"):
        pos = sentence.index(value)
        print("BLOC DE MOT : *********************************************************************************")
        while (sentence[pos] != "skill" or sentence[pos] != "formation" or sentence[pos] != "experience" ):
            print(sentence[pos])
            #dico.append(sentence[pos])
            education.append(sentence[pos])
            if (sentence[pos] == "skill" or sentence[pos] == "formation" or sentence[pos] == "experience" or pos>=len(sentence)-1):
                break
            pos += 1
        for i in range(0,len(education)):
            if re.findall("\d{4}", education[i]):
                print(compteurEXP)
                compteurEDU+=1
                dico.append(education[i])

results = list(map(int, dicoEXP))
print("Nombre d'experience pro ",nbrExp)

print("Temps d'experience pro",max(results)-min(results))


#Recuperation d'une liste de mot se situant apres le mot cle








#print(dico)

#print("le mot {} est present {} fois".format(search_word, search_word_count))
