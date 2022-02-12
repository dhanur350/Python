with open("f1.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("This is written data")
myfile.close()
#"r" – Python read file. Read mode which is used when the file is only being read
#‘w’ – Python write file. Write mode which is used to edit and write new information 
#      to the file (any existing files with the same name will be erased when this mode is activated)
#‘a’ – Python append file. Append mode, which is used to add new data to the end of the file; 
#       that is new information is automatically amended to the end
#‘r+’ – Special read and write mode, which is used to handle both actions when working with a file
