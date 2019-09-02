import os
outputFile=open("salida.txt","a")
x=os.listdir()
#y=str(x)
for files in x:
    print(files)
    outputFile.write(files+"\n")
outputFile.write("\n")
outputFile.close()
