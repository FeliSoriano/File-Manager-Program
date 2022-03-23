#Welcome to my File Manager Program
#The aim is for this program to facilitate file managment, suchs as moving, deleting and renaiming files.

#This is Version 2 - I have added a function that avoids the need of a full path. U can still provide it, in order to
#reduce the running time.


import pathlib
import shutil
import os
from send2trash import send2trash
import sys
import ctypes

def is_sym_link(path):
    #http://stackoverflow.com/a/35915819
    FILE_ATTRIBUTE_REPARSE_POINT = 0x0400
    return os.path.isdir(path) and (ctypes.windll.kernel32.GetFileAttributesW(str(path)) & FILE_ATTRIBUTE_REPARSE_POINT)

def find(base, filenames):
   
    hits = [] #Have to check for a way to modify the code, since I only need a single string output.
                #For some reason changing the list hits[] for a string always returns None.
                #Also sometimes find a dir with the same name we are looking for, but not the correct one.
                #Would be cool to add a way to find all matching hits and then let the user choose one
    skipped = []

    def find_in_dir_subdir(direc):
        content = os.scandir(direc)
        for entry in content:
            if entry.name in filenames:
                hits.append(os.path.join(direc, entry.name))

            elif entry.is_dir() and not is_sym_link(os.path.join(direc, entry.name)):
                                #The original code used is_sym_link. But it does not appear to be necesarry
                try:
                    find_in_dir_subdir(os.path.join(direc, entry.name))
                except UnicodeDecodeError:
                    print("Could not resolve " + os.path.join(direc, entry.name))
                    continue
                except PermissionError:
                    skipped.append(os.path.join(direc,entry.name))
                    continue

    if not os.path.exists(base):
        return
    else:
        find_in_dir_subdir(base)
      
    if len(skipped) != 0:
        print(str(len(skipped)) + " folder/s have been skipped because of lacking permission")
        see_skipped = input("Do you wish to see them? (Yes/No)").lower()

        if see_skipped[0] =='y':
            for skip in skipped:
                print(skip)
    if len(hits) == 0:
        hits.append("Not_Found")
    return hits

class Fobject: #I don't necessarilly like this name, since the program also work's with directories.
            #But as of yet I have failed to come up with a better one
    
    def __init__(self,src ='', name ='',path =''):
        self.src = src
        self.name = name
        self.path = path
        
    
    def get_file(self):
               
        while True:
            
            print("Input the name of the File or Directory you want to work with, ")
            print("if working with a file, make sure to include a suffix (i.e : .txt)")
            self.name = input("Name = ")
            abort(self.name)
            
            print("\nNow input the path (can leave blank, but giving specifications speeds up the procces)")
            print("This is an example path. Please use a matching format")
            print("C:\\Users\\Felipe\\Documents\\Feli\\Programación\\file.txt\n\n ")
            base = input("Base path = ")
            abort(base)
            if base == '':
                base = "C:\\"
            
            match = find(base, [self.name])
            file = match[0]
            
            if file != "Not_Found":
                print(file)
                correct = input("\nIs this the file you want to work with? (Yes/No)? ").lower()
                if correct[0] == 'y':
                    self.src = pathlib.Path(file)
                    if self.path == '':
                        self.path = self.src
                    break
            else:
                print("\nI'm sorry, we couldn't find the file you are looking for. Please try again")
            
    
    def rename(self):
        old_name = self.path
        while True:
            try:
                self.name = input("Choose a new file/directory Name (no suffix needed): ")
                abort(self.name)
                new_name = str(self.path.parent) + '\\'+ str(self.name) + str(self.path.suffix)
                os.rename(old_name,new_name)
                
            except FileExistsError:
                print("\nA file with that name already exists in this directory, please try a new one")
            
            else:
                break
        self.path = new_name
        
    def move_file(self): #There may be a problem here, have to check.
        while True: 
            dst = pathlib.Path(input("\nEnter your file's destination (must be a Directory) - "))
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
    print("The File / Directory has been successfully sent to the Trash Bin")
        
        
def menu():
    print("\n\n\n" + 20* "=" + " Choose an Option " + 20* "=", flush = True)
    print("If, at any point, you want to exit the program type exit in any input prompt")
    print("1. Move a File or Folder", flush = True)
    print("2. Delete a File or Directory", flush = True)
    print("3. Rename a File or Directory", flush = True)
    print("4. Exit", flush = True)
    print(58 * "=", flush = True)
    
    while True:
        try:
            choise = int(input("Option (1-4) ->"))
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
print("\n" + 80 * "%",flush = True)
print("Welcome to Felipe Soriano's File Managment Program.",flush = True)
print("\nThis program is currently in Phase 2") 
print("\nEventually, you will be able to easily modify multiple files & folders with ease",flush = True)
print("\nHope you find my program useful!",flush = True)
print("\nIf, at any point, you want to exit the program type exit in any input prompt")
print("\nContact: felysoryano@gmail.com || Twitter: @FeliSoorianoE",flush = True)
print("\n" + 80 * "%" + "\n\n\n",flush = True)


f = []
n=0

op = menu()
while op != 4:
    
    f.append(Fobject())
    f[n].get_file()

    if op == 1:
        f[n].move_file()

    elif op == 2:
        trash_bin(f[n].path)
    
    elif op == 3:
        f[n].rename()

    
    cont = input("Do you wish to work with another file? (yes/no)").lower()
    if cont[0] == 'n':
        break
    else:
        n+=1
    
    op = menu()

print("\n\nThanks for using my program!")
