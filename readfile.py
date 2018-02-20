#get number of files
try:
    FileNum = int(input("How many files to read?: "))
except TypeError:
    print("Please input integers only")

#set variables and create list to store directories
FilesDir = []
FilesCont = []
charcounts = []

#user inputs directories into list
for i in range(FileNum):
    FilesDir.append(input("Directory for File #"+str(i+1)+": "))

print(FilesDir)

#reads each file
contPrint= input("print contents? y/n: ")

for i in range(len(FilesDir)):
    file = open (FilesDir[i], "r")
    content = file.read()
    FilesCont.append(content)
    if contPrint == "y":
        file.seek(0)
        print("\n contents of file "+str(i+1)+": "+str(content))
    file.seek(0)
    charcounts.append(len(content))


print(charcounts)
large = max(charcounts)
location = charcounts.index(max(charcounts))
print("Largets file: File number "+str(location)+" at "+str(large)+" characters.")
   
