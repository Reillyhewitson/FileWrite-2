import os
import time
import glob #necassery functions


file_name = str('Generic')
new_file_name = str('Generic')
rpath = "C:\\Users\\Reilly Hewitson\\OneDrive - UTC Reading\\GCSE Computer science\\Python\\Personal Python\\Made in Python"
path = "C:\\Users\\Reilly Hewitson\\OneDrive - UTC Reading\\GCSE Computer science\\Python\\Personal Python\\Made in Python\\"
file_list = [f for f in os.listdir(rpath) if os.path.isfile(os.path.join(rpath, f))] #taking all data in the directory and saving it
file_exist = int(0)
run = 0
# all needed variables

def list_file(file_list, path): #outputs the list of files
    os.chdir(rpath)
    for file in glob.glob('*.txt'): #searches the directory for files with ending .txt and prints it
        print(file)
        
def error(file_name): #runs if an error is found
    print('Unfortunately', file_name, 'is not a recognised file. FileWrite will restart when you press "enter"')
    user = str(input())
    clear()
def genericError(): #runs if a non file related error is found.
    print('Somthing went wrong give us a second...')
    time.sleep(3)


def clear(): #clears the screen
    os.system('cls' if os.name == 'nt' else 'clear')
def enter(): #If the code works it does this
    print('success')
    print('press enter to continue')
    enter = str(input())

def cancel(): #if the user cancels the operation do this
    clear()
    print('Cancelling...')
    time.sleep(1)

def addTo(): #the loop that allows you to add multiple lines to a file
    print('Input what you would like to write. Use ctrl-C on a new line to end') #\n adds a new line.
    while True:
        try:
            add_to = str(input())
            file.write(add_to + '\n')
        except KeyboardInterrupt or EOFError: #stops the loop by catching a keyboard interrupt
            break
    enter()
    
        
while run == 0: #the main loop
    try: 
        file_list = [f for f in os.listdir(rpath) if os.path.isfile(os.path.join(rpath, f))] #refreshes the file list
        clear()
        print ('would you like to: \n 1. make a document \n 2. add to a document \n 3. read a document \n 4. delete a document \n 5. Rename a document \n 6. See documents \n 7. Switch Directory \n press ctrl-c to quit')
        #prints the list of options

        #put \n to create a new line
        select = str(input())[:1] #takes the first inputted number and saves it as a variable
       

        if select == '1': 
            clear()
            print ('what would you like to call the file?')
            file_name = str.lower(input())[:50] #limits file names to 50 characters
            file_name = file_name.translate({ord(ch):'' for ch in '\/:*?"<>|'}) #cleans any characters that are not allowed in windows filenames
            if file_name+'.txt' in file_list:
                print('Do you want to overwrite', file_name+'? y/n')#checks if the user is ok with overwriting a file
                answer = str.lower(input())
                if answer == 'y':
                    print ('OK')
                else:
                    while file_name+'.txt' in file_list: #gets them to rename if they don't want to overwrite
                        print('please enter a different name')
                        file_name = str.lower(input())[:50]

            if file_name == '': #allows user to cancel the function
                cancel()
            else:
                file = open(path + file_name +'.txt' , "w+") #opens the file
                addTo()
            file.close()

        elif select == '2':
            clear()
            list_file(file_list, rpath) #shows the files in the directory
            print ('What file do you want to open?')
            file_name = str.lower(input())[:50]
            file_name = file_name.translate({ord(ch):'' for ch in '\/:*?"<>|'})
            clear()
            full_file_name = str(file_name +'.txt')
            if file_name == '':
                cancel()
            elif full_file_name in file_list:
                file = open(path + file_name +'.txt' , "a")
                addTo()
            else:
                error(file_name) #if somthing unexpected happens run error
            file.close()


        elif select == '3':
            clear()
            list_file(file_list, rpath)
            print ('What file do you want to open?')
            file_name = str.lower(input())[:50]
            file_name = file_name.translate({ord(ch):'' for ch in '\/:*?"<>|'})
            clear()
            full_file_name = str(file_name +'.txt')
            if file_name == '':
                cancel()
            elif full_file_name in file_list:
                file = open(path + file_name +'.txt' , "r")
                full_file = file.read() #removes all extra syntax so it is human readable
                print (full_file) #prints the output
                file.close()#closes the file
                enter()
            else:
                error(file_name)

        elif select == '4':
            clear()
            list_file(file_list, rpath)
            print ('what file do you want to remove')
            file_name = str.lower(input())[:50]
            file_name = file_name.translate({ord(ch):'' for ch in '\/:*?"<>|'})
            clear()
            full_file_name = file_name +'.txt'
            if file_name == '':
                cancel()
            elif file_name == 'all': #allows you to delete all files in the directory
                print ('are you sure you want to delete all .txt files? y/n')
                select = str.lower(input())
                if select == 'y':
                    for file in file_list:
                        if file.endswith('.txt'): 
                            os.remove(file) #removes all .txt files from a directory
                            print('deleted', file)
                    enter()
                else:
                    cancel()

            elif full_file_name in file_list:
                os.remove(path + file_name +'.txt') #deletes the specified file
                print ('file removed')
                enter()
            else:
                error(file_name)

        elif select == '6':
            clear()
            list_file(file_list, rpath) #lists files
            enter()

        elif select == '8': #allows you to quit REDUNDANT
            clear()
            print(' 1. Quit \n 2. remain')
            select = str(input())
            if select == '1':
                run = 1
            else:
                print('OK')
        elif select == '7': 
            clear()
            oldpath = rpath
            print('Which directory do you want?' )
            rpath = str(input())
            
            if rpath == 'shopping': #tells it to go to a specific folder
                print('Going to shopping')
                rpath = 'C:\\Users\\Reilly Hewitson\\python'
                path = rpath + '\\'
            elif os.path.isdir(rpath) == False: #checks if the directory exists and resets it
                print('Unfortunatly that directory does not exist resetting to current directory')
                rpath = oldpath
            elif rpath != '' and rpath != '.': #sets to specified directory
                path = rpath + '\\'
            else:
                path = "C:\\Users\\Reilly Hewitson\\Documents\\Made in Python\\" #sets to standard directory
                rpath = "C:\\Users\\Reilly Hewitson\\Documents\\Made in Python"
            print(path)
            enter()
                
            print('Do you want to list the new directory? \n 1. Yes \n 2. No')
            select = str(input())
            file_list = os.listdir(rpath) #lists files in the new directory
            if select == '1':
                clear()
                list_file(file_list, rpath)
            else:
                print('Goodbye')
        elif select == '5':
            clear()
            list_file(file_list, rpath)
            print('Which file do you want to rename?')
            file_name = str.lower(input()) #forces the filename to be lower case
            no = 0
            while no == 0:
                if file_name+'.txt' in file_list: #checks file exists in current directory
                    print('What is the new name?')
                    new_name = str.lower(input()) #gets new name
                    no = 1
                else:
                    print('That file does not exist. Choose a new name')
                    file_name = str.lower(input()) #forces the user to pick an existing file

            if new_name == '':
                cancel()
            elif file_name+'.txt' in file_list:
                os.rename(file_name+'.txt', new_name+'.txt') #renames the file
                enter()
            else:
                error()
        else:
            clear()
            print ('An error occured. \nPlease wait...')
            time.sleep(1)
    except KeyboardInterrupt: #allows you to quit CURRENT
        break
