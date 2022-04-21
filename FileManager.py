#This is version 3 of the program.

from o_and_f import *

           
            
            
###Code Start
print("\n" + 80 * "%",flush = True)
print("Welcome to Felipe Soriano's File Managment Program.",flush = True)
print("\nThis program is currently in Phase 3") 
print("\nHope you find my program useful!",flush = True)
print("\nIf, at any point, you want to exit the program type exit in any input prompt")
print("\nContact: felysoryano@gmail.com || Twitter: @FeliSoorianoE",flush = True)
print("\n" + 80 * "%" + "\n\n\n",flush = True)


n = 0
m = 0
f = []

deleted_files = []

op = menu()

while op!=0:
    
    
    if op in range (1,5): #Working with a single file
        f.append(Fobject())
        f[n].get_file()
        
    if op ==1: #Open the file
        os.startfile(f[n].path)
        n+=1
            
    elif op == 2: #Move the file
        f[n].move_file('ask')
        n+=1

    elif op == 3:#Delete the file
        deleted_files.append(trash_bin(f[n].path,'yes'))
        n+=1
        
    elif op == 4: #Rename the file
        f[n].rename('ask')
        n+=1

    #cont = input("Do you wish to work with another file? (yes/no)").lower()
    #if cont[0] == 'n':
     #   break
    #else:
     #    n+=1
                
    if op == 5:
        m_op = mass_menu()
        
        if m_op == 0:
            op = 0
            break
            
        #Getting the directory we are going to work with
        if m_op != 4:
            m_dir = input("What's the name of the directory you want to work with?")
            abort(m_dir)
            if is_path():
                msrc = m_dir
                files_list = os.listdir(msrc)
                list_of_objects = make_object_list(msrc,files_list)
            else:
                print("\nNow input the path (can leave blank, but giving specifications speeds up the procces)")
                print("This is an example path. Please use a matching format")
                print("C:\\Users\\Felipe\\Documents\\Feli\\Programación\n\n ")
                m_base = input("Base path = ")
                abort(m_base)
                if m_base == '':
                    m_base = "C:"
                msrc = find(m_base,m_dir)
                print(f"\nWorking with:\n{msrc[0]}\n")
                ##Option to make sure the input is correct
                files_list = os.listdir(msrc[0])
                list_of_objects = make_object_list(msrc[0],files_list)
        
        #Specific Options
        if m_op == 1: #Delete all files
            for file in list_of_objects:
                deleted_files.append(trash_bin(file))
            print(f"All files in \n{msrc[0]} \nhave been deleted succesfully")
            m+=1
            
        if m_op == 2: #Rename all files
            mass_rename(list_of_objects)
            m+=1
            
        if m_op == 3: #Move all files
            while True:
                dst = pathlib.Path(input("Where do you want to send your files (full path required)"))
                abort(dst)
                if dst.is_dir():
                    break
                else:
                    print("\nInvalid destination, try again")
                    
            print("\n\na. Move all files")
            print("b. Move only some files")
            move_op = input("Choose an option (a/b): ")
            abort(move_op)
            
            if move_op == 'a':
                for obj in list_of_objects:
                    obj.move_file('asked', dst)                    
            if move_op == 'b':
                for obj in list_of_objects:
                    want_to_move = input(f"Do you want to move {obj.name}? (y/n)").lower()
                    abort(want_to_move)
                    if  want_to_move[0] == 'y':
                        obj.move_file('asked',dst)
                    else:
                        pass
            
            m+=1
            
        if m_op !=4:               
            cont = input("Do you wish to start again? (yes/no)").lower()
            if cont[0] == 'n':
                break
    clear_output()
    op = menu()
    
print("\nThanks for using my program!. Cheers, Felipe Soriano")
            
        
    

