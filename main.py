import tkinter.messagebox as msgbox
from tkinter import *
from zipfile import ZipFile
import sys, os, threading

try:
    os.chdir(sys._MEIPASS)
except:
    os.chdir(os.getcwd())

#function
def btn_func(event):
    global bg_label2, installer
    if installer != 1:
        bg_label2.place(x=-2, y=-1)
        a.start()

def install_func():
    global installer
    if installer == 1:
        return 0
    else:
        installer = 1
        with ZipFile(file, 'r') as zip:
            zip.extractall(target_file)
        msgbox.showinfo("설치 완료", "정상적으로 설치가 완료되었습니다")
    os._exit(0)

#Main
installer = 0
file = "resource/target.zip"
target_file = os.getenv('APPDATA')+'\.minecraft'

root = Tk()
root.title("Example Installer")
root.iconbitmap('resource/icon.ico')
root.geometry("950x600")
root.resizable(False, False)

bg = PhotoImage(file="resource/bg.png")
bg_label = Label(root, image=bg)
bg2 = PhotoImage(file="resource/bg_install.png")
bg_label2 = Label(root, image=bg2)
bg_label.place(x=-2, y=-1)

btn_img = PhotoImage(file="resource/btn.png")
btn = Button(root, image=btn_img)
btn.place(x=255, y=400)
btn.bind("<Button>", btn_func)

a = threading.Thread(target=install_func)
root.mainloop()
