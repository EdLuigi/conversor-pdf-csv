import csv
import tabula
import zipfile


#Lê do PDF/tabelas e transforma em CSV
file = "Anexo I - Lista completa de procedimentos (.pdf).pdf"
csv_table = tabula.convert_into(file,'pdf_convertido.csv', pages='3-180')


#Abre o CSV em lista
with open('pdf_convertido.csv', newline='') as file:
    reader = csv.reader(file)
    data = list(reader)


#Tira os outros cabeçalhos e altera os valores 'OD' e 'AMB'
auxList = []
auxListInterna = ''
index = -1
for item in data:
    if item != data[0]:
        auxList.append([])
        index+=1
        for item2 in item:
            auxListInterna = item2
            if(item2=='OD'):
                auxListInterna = 'Seg. Odontológica'
            if(item2=='AMB'):
                auxListInterna = 'Seg. Ambulatorial'
            auxList[index].append(auxListInterna)
        

#Transforma em CSV
with open('pdf_convertido.csv', 'w') as myfile:
     wr = csv.writer(myfile)
     wr.writerow(data[0])
     wr.writerows(auxList)


#Zipa o arquivo CSV
with zipfile.ZipFile('Teste_{Eduardo_Ciuffi}.zip', 'w',
                     compression=zipfile.ZIP_DEFLATED,
                     compresslevel=9) as zf:
    zf.write('pdf_convertido.csv', arcname='pdf_convertido.csv')
