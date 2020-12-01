##################################################
#                  It's old code                 #
##################################################

import os

running = True
hello_var = 'hello__'
exit_var = 'exit__'
help_var = 'help__'
temp_var = 'temp__'
createFile_var = 'crfile__'
deletefile_var = 'delfile__'
createFolder_var = 'crdir__'
deletefolder_var = 'deldir__'
readfile_var = 'openfile__'

while running:
    def helpfun():
        while running:
            print('"exit__" will came out terminal')
            print('"hello__" terminal will say "Hello, world!"')
            print('"temp__" terminal will show temperature in certain city')
            print('"crfile__" terminal will create a file')
            print('"delfile" terminal will delete file')
            print('"crdir" terminal will create folder')
            print('"deldir" terminal will delete folder')
            print('"openfile" terminal will open file')
            break


    def createfilefun():
        while running:
            text_in_file = input('Text in file: ')
            file_var = open(input('library and file name: '), 'a')
            file_var.write(text_in_file)
            file_var.close()
            break


    def deletefilefun():
        while running:
            os.listdir()
            os.remove(input(r'library and file name: '))
            break


    def createfolderfun():
        while running:
            os.mkdir(input(r'library and folder name: '))
            break


    def deletefolderfun():
        while running:
            os.rmdir(input(r'library and folder name: '))
            break


    def openfilefun():
        while running:
            file_read = open(input(r'library and file name: '), encoding='utf-8')
            print(file_read.read())
            break


    def tempfun():
        while running:
            import pyowm
            owm = pyowm.OWM('abdd95174182b13df02a471f1fb2b996')
            city = input('City: ')
            observation = owm.weather_at_place(city)
            w = observation.get_weather()
            temp = w.get_temperature('celsius')['temp']
            print('In this city ' + str(temp))
            break


    def hello():
        while running:
            print('Hello, world!')
            break


    def exitfun():
        while running:
            exit(code=" ")


    otv = input('>: ')

    if otv == hello_var:
        hello()
    elif otv == exit_var:
        exitfun()
    elif otv == help_var:
        helpfun()
    elif otv == temp_var:
        tempfun()
    elif otv == createFile_var:
        createfilefun()
    elif otv == deletefile_var:
        deletefilefun()
    elif otv == createFolder_var:
        createfolderfun()
    elif otv == deletefolder_var:
        deletefolderfun()
    elif otv == readfile_var:
        openfilefun()
    else:
        print('Inputed incorrectly command')
