#Welcome to my File Manager Program
#The aim is for this program to facilitate file managment, suchs as moving, deleting and renaiming files.


import pathlib
import shutil
import os
from send2trash import send2trash
import sys

class File: #I don't necessarilly like this name, since the program also work's with directories.
            #But as of yet I have failed to come up with a better one
    
    def __init__(self,src='', name ='',path=''):
        self.src = src
        self.name = name
        self.path = path
        
    
    def get_file(self):
        print("\nThis is an example path. Please use a matching format")
        #I'll eventually add a func that "corrects" the format
        print("\nie:C:\\\\Users\\\\Felipe\\\\Documents\\\\Feli\\\\Programación\\\\file.txt\n\n ")
        while True:
            file = pathlib.Path(input("Please enter the path of the file/directory you want to work with\n"))
            abort(file)
            if file.exists():
                self.src = file
                self.name = file.name
                if self.path == '':
                    self.path = self.src
                break
            else:
                print("\nPlease enter a valid path\n")
    
    def rename(self):
        old_name = self.path
        while True:
            try:
                self.name = input("Choose a new file/directory Name: ")
                abort(self.name)
                new_name = str(self.path.parent) + '\\'+ str(self.name) + str(self.path.suffix)
                os.rename(old_name,new_name)
                
            except FileExistsError:
                print("A file with that name already exists, please try a new one")
            
            else:
                break
        self.path = new_name
        
    def move_file(self): #There may be a problem here, have to check.
        while True: 
            dst = pathlib.Path(input("\nEnter your file's destination - "))
            abort(dst)
            if dst.is_dir():
                shutil.move(str(self.path),dst) #Have to convert to string since self.path is a pathlib.WindowsPath
                #print("\n {self.path.name} has been moved from {self.path.parent} to {dst} ")
                self.path = dst
                break
            else:
                print("\nI'm sorry, but that is not a valid destination")
            

def trash_bin(file):
    send2trash(str(file))
    print("\nThe File or Directory has been successfully sent to the Trash Bin")
        
        
def menu():
    print(30* "=" + " Choose an Option " + 30* "=", flush = True)
    print("If, at any point, you want to exit the program type exit in any input prompt")
    print("1. Move a File or Folder", flush = True)
    print("2. Delete a File or Directory", flush = True)
    print("3. Rename a File or Directory", flush = True)
    print("4. Exit", flush = True)
    print(78* "=", flush = True)
    
   
    while True:
        try:
            choise = int(input("Choose an option (1-4) ->"))
            abort(choise)
            if choise in range(1,5):
                break
            else:
                print("That's not a valid option!")
        except ValueError:
            print("I'm sorry, but that is not a valid option. Let's try again")
        
    return choise

def abort(s):
    if str(s).lower() == 'exit':
       sys.exit("Thanks for using my program!")


###Program Start
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%",flush = True)
print("Welcome to Felipe Soriano's File Managment Program.",flush = True)
print("\nThis program is currently in Phase 1. This means it requires a lot of user input (such as full file path's)",flush = True)
print("\nEventually, you will be able to easily modify multiple files & folders with ease",flush = True)
print("\nHope you find my program useful!",flush = True)
print("\nContact: felysoryano@gmail.com || Twitter: @FeliSoorianoE",flush = True)
print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%",flush = True)

working = True
f = []
n=0
while working:
    op = menu()
    f.append(File())
    f[n].get_file()

    if op == 1:
        f[n].move_file()

    elif op == 2:
        trash_bin(f[n].path)
    
    elif op == 3:
        f[n].rename()
        
    elif op == 5:
        quit()
    
    cont = input("Do you wish to work with another file? (yes/no)").lower()
    if cont[0] == 'n':
        print("Thanks for using my program")
        working = False
    else:
        n+=1