import os

homedir = os.environ['HOME']
destinationdir = homedir + '/.local/share/applications/'
itype=""
iencoding=""
iname=""
icomment=""
iexec=""
iicon=""
iterminal=""
icategories=""

def header():
    code  = '    ____  ____      \n'
    code += '   ||.D||||G ||     \n'
    code += '   ||__||||__||     \n'
    code += '   |/__\||/__\|     \n'
    code += '                    \n'
    code += ' .desktop generator \n'
    code += '                    \n'
    code += ' Destination path: ' + destinationdir + '\n'
    return code

def set_data():
    global itype
    global iencoding
    global iname
    global icomment
    global iexec
    global iicon
    global iterminal
    global icategories
    itype = input(' Type [Intro=\'Application\'] = ')
    iencoding = input(' Encoding [Intro=\'UTF-8\'] = ')
    iname = input(' Name = ')
    icomment = input(' Comment = ')
    iexec = input(' Exec = ')
    iicon = input(' Icon = ')
    iterminal = input(' Terminal [Intro=\'false\'] = ')
    icategories = input(' Categories = ')

def generate_desktop():
    global itype
    global iencoding
    global iterminal
    if itype == "":
        itype = "Application"
    if iencoding == "":
        iencoding = "UTF-8"
    if iterminal == "":
        iterminal = "false"	
    file_name = iname.lower().replace(" ", "_") + ".desktop"
    data_file = open(destinationdir + file_name, 'wb')
    data_file.write('[Desktop Entry]\n'.encode())
    data_file.write(('Type=' + itype + '\n').encode())
    data_file.write(('Name=' + iname + '\n').encode())
    data_file.write(('Encoding=' + iencoding + '\n').encode())
    data_file.write(('Comment=' + icomment + '\n').encode())
    data_file.write(('Exec=' + iexec + '\n').encode())
    data_file.write(('Icon=' + iicon + '\n').encode())
    data_file.write(('Terminal=' + iterminal + '\n').encode())
    data_file.write(('Categories=' + icategories + '\n').encode())
    data_file.close()
    return '\n Created: ' + destinationdir + file_name + '\n'
    
print(header())
set_data()
print(generate_desktop())
