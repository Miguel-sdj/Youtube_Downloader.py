import subprocess
import os

version_bat = open(r'temporary_update.bat','w+')
version_bat.write("curl -L https://raw.githubusercontent.com/Miguel-sdj/Youtube_Downloader.py/main/version.txt > version.txt")
version_bat.close()
subprocess.call([r'temporary_update.bat'])
os.remove("temporary_update.bat")

def separate_phrase(name_file):
    file = open(name_file, "r", encoding='utf-8')
    lines_phrase = file.readlines()
    list_phrases = []
    for lines in lines_phrase:
        lines = lines.rstrip('\n')
        if not (lines.isnumeric()) and lines:
            list_phrases.append(lines)
    file.close()
    return list_phrases

links_separados = separate_phrase('version.txt')

version = links_separados[0]
name_zip = links_separados[1]
zip_version = name_zip.split()


myBat = open(r'temporary_update.bat','w+')

name_repo = "curl -L https://github.com/Miguel-sdj/Youtube_Downloader.py/releases/download/"

myBat.write(name_repo + version + name_zip)
cwd = os.getcwd()
myBat.write("\nmd "+ cwd + "\\novo_update")

power_shell = ('\npowershell.exe -nologo -noprofile -command ' + '"' + "& { $shell = New-Object -COM Shell.Application; $target = $shell.NameSpace('" + cwd + "\\novo_update" + "')" + "; $zip = $shell.NameSpace('" + cwd + "\\" + zip_version[0] + "')" + "; $target.CopyHere($zip.Items(), 16); }")
myBat.write(power_shell)

myBat.close()
subprocess.call([r'temporary_update.bat'])

os.remove("temporary_update.bat")
os.remove("version.txt")
