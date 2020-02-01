import PyPDF2 as p2
import nltk

PDFfile=open("cvtest2.pdf","rb")
pdfReader= p2.PdfFileReader(PDFfile)
x=pdfReader.getPage(0)
y=pdfReader.getFields("a")
print(x.extractText())
sentence=[]
dico=[]

#print(x.extractText())
search_word = "skills"
search_word_count = 0
for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    text = pageObj.extractText()
    search_text = text.lower().split()
    for word in search_text:
        sentence.append(word)
        #print(word)

    #Recuperation d'une liste de mot se situant apres le mot cle
    for value in sentence:
        if value==search_word:
            pos=sentence.index(value)
            while(pos<len(sentence)):
                #print(sentence[pos])
                dico.append(sentence[pos])
                pos+=1





#print(dico)

#print("le mot {} est present {} fois".format(search_word, search_word_count))
