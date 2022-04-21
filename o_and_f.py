#This file stores all functions and objects used in FileManager.py

import pathlib
import shutil
import os
from send2trash import send2trash
import sys
from IPython.display import clear_output
import ctypes

#Object
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
            self.name = input("Name = ") #Fix in Phase 3 to get consistency in suffix usage
            abort(self.name)
            
            print("\nNow input the path (can leave blank, but giving specifications speeds up the procces)")
            print("This is an example path. Please use a matching format")
            #I'll eventually add a func that "corrects" the format
            print("C:\\Users\\Felipe\\Documents\\Feli\\Programación\\file.txt\n\n ")
            base = input("Base path = ")
            abort(base)
            if base == '':
                base = "C:\\"
            
            match = find(base, [self.name])
            if match == None:
                sys.exit("Sory, something went wrong")
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
            
    
    def rename(self,op, named =''):
        old_name = self.path
        while True:
            try:
                
                if op == 'ask': #I need to ask for the names
                    
                    self.name = input("Choose a new file/directory Name (no suffix needed): ")
                    abort(self.name)
                
                if op == 'asked': #I already have the names
                    self.name = named
                    
                new_name = str(self.path.parent) + '\\'+ str(self.name) + str(self.path.suffix)
                os.rename(old_name,new_name)
                
            except FileExistsError:
                print("\nA file with that name already exists in this directory, please try a new one")
                if op =='asked':
                    break #A temporary patch to avoid infinite loops
            else:
                break
        self.path = new_name
        
   
        
    
    def move_file(self, op, dest =''): #There may be a problem here, have to check.
        
        if op == 'ask':
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
        if op == 'asked':
            shutil.move(str(self.path), dest) #We asume it has already been check for valid path


#FUNCTIONS
def menu(clear =''):
    if clear == 'yes':
        clear_output()
    print("\n\n\n" + 20* "=" + " Choose an Option " + 20* "=", flush = True)
    print("0. Exit", flush = True)
    print("1. Open File", flush = True)
    print("2. Move a File or Folder", flush = True)
    print("3. Delete a File or Directory", flush = True)
    print("4. Rename a File or Directory", flush = True)
    print("5. Go to mass-file managing menu", flush = True)
    print(58 * "=", flush = True)
    
    while True:
        try:
            choise = int(input("Option (0-5) ->"))
            abort(choise)
            if choise in range(0,6):
                break
            else:
                print("That's not a valid option!")
        except ValueError:
            print("I'm sorry, but that is not a valid option. Let's try again")
        
    return choise

def mass_menu(clear =''):
    if clear =='yes':
        clear_output()
        
    print("\n\n\n" + 20* "=" + " Choose an Option " + 20* "=", flush = True)
    print("This is the mass-file-managing menu",flush = True)
    print("0. Exit", flush = True)
    print("1. Mass-Deletion", flush = True)
    print("2. Mass-Renaming", flush = True)
    print("3. Mass-Moving", flush = True)
    print("4. Back to single file managing menu", flush = True)
    print(58 * "=", flush = True)
    
    while True:
        try:
            choise = int(input("Option (0-4) ->"))
            abort(choise)
            if choise in range(0,5):
                break
            else:
                print("That's not a valid option!")
        except ValueError:
            print("I'm sorry, but that is not a valid option. Let's try again")
        
    return choise


def example(op):
    if op ==1:
        print('\n\n' + 20 * '~' + "This is an example!" + 20 * '~')
    if op ==2:
        print(59 * '~' + '\n')

def abort(s):
    if str(s).lower() == 'exit':
       sys.exit("Thanks for using my program!")
    
def trash_bin(file, show=''): #Deletes a file
    send2trash(str(file))
    deleted_file = file.name
    if show == 'yes':
        print(f"{file.name} has been successfully sent to the Trash Bin")
    return deleted_file

def is_sym_link(path):
    #http://stackoverflow.com/a/35915819
    FILE_ATTRIBUTE_REPARSE_POINT = 0x0400
    return os.path.isdir(path) and (ctypes.windll.kernel32.GetFileAttributesW(str(path)) & FILE_ATTRIBUTE_REPARSE_POINT)

def find(base, filenames): #Looks for file in whole computer
   
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

def is_path():
    is_path = input("Did you input a path (yes/no)")
    if is_path.lower()[0] == 'y':
        return True
    else:
        return False

def make_object_list(msrc,f_l): #msrc stands for mass source, f_l stands for file_list,
    
    path_lobject = []
    
    for file in f_l:
        
        path_lobject.append(Fobject())
        path_lobject[-1].path = path_lobject[-1].src = pathlib.Path(os.path.join(msrc,file))
        path_lobject[-1].name = path_lobject[-1].src.stem      
        
    
    return path_lobject
    
def get_format(): #funcs that allows for easy mass-file renaming
    
    print("\n\nYou will now choose a format to make the renaming file process easier")
    print("Here is an example to show you how this will work:")
    example(1)
    print("Let's say I want my files to be named File_1, File_2, etc.")
    print("Then, I could choose the letter x, and then when asked for a format type it like this:")
    print("File_x")
    print("After that, you just need to choose, for each case, what do you want to replace the x with!")
    example(2)
    
    format_key = input("Which key-letter are you gonna use to format? (single digit only) : ")
    name_format = input("Now type the actual format, using the letter you chose: ")
    
    #Add option so that you can input more than one letter/number as format_key
    #Right now, using 'xx' as format_key wouldn't work.
    
    while True:
        ok = input("Is your format correct? (Yes/No)").lower()
        if ok[0] == 'n':
            change = input("Do you want to change your key-letter? (Yes/no)").lower()
            if change[0] == 'y':
                format_key = input("Which key-letter are you gonna use to format? ")
            name_format = input("Now type the actual format, using the letter you chose -> ")
        else: 
            break
    
    return {format_key: name_format}

   

def get_key(dic): #Only works for dictionaries with a single item
    x = str(dic.keys()) #str(dic.keys()) returns -> "dict_keys(['x'])". So key-letter is x[-4]
    return x[-4]

def format_renaming(dic, list_names,list_objects):
    
    new_lis =[]
    aux_key = get_key(dic)
    aux = dic[aux_key].split(aux_key)
    replace = ''
    print(f'\n««FORMAT: {dic[aux_key]}»»')
    for item,obj in zip(list_names,list_objects):
        if replace != 'end':
            print(f"\nRenaming {item}")
            replace  =input(f"Replace {aux_key} with :  ")
            if replace != 'pass' and replace != 'end':
                aux_name = aux[0] + replace + aux[1]
                obj.rename('asked', aux_name)
                new_lis.append(aux_name)
           
            elif replace == 'pass':
                aux_name = item
                
        new_lis.append(aux_name) #regardless of if you change the name, the list will contain all files.
            
        
    #print("\n\n")
    #for num in range(0,len(list_names)):
        #print(f"{list_names[num]} changed to --> {new_lis[num]}")
    
   # confirm = input("\nConfirm?(Yes/No) ").lower() Confirming doesn't make sense beacuse we are
                                                    #reanming in every iteration. Regardless, since we have
                                                    #the original names, we (in theory) could change everything back
    
    #if 'n' in confirm:
        #print("Let's try again!")
        #formating(dic,lis)
        
    return new_lis

def mass_rename(list_of_objects):
    
    print("Warning this does not differentiate between files and folders ")
    print("\nChoose an option:")
    print("1. Unique Renames")
    print("2. Pre Format Renaming (ie. File_1, File_2,etc)")
    
    op = input("Option --> ")
    if op == '1':
        for obj in list_of_objects:
            print(f"\nRenaming : {obj.name} ({obj.path.suffix})")
            obj.rename('ask')
    
    if op == '2':
        print("pass skips the file, end finishes the renaming process\n")
        full_format = get_format()
        og_names = [item.name for item in list_of_objects]
        new_names = format_renaming(full_format,og_names,list_of_objects)
        #for name, obj in zip(list_of_names,list_of_objects):
            #obj.rename('asked', name)