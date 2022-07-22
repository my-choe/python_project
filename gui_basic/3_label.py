from tkinter import *

root = Tk()
root.title("GUI Project")
root.geometry("640x480+600+300") # 가로 * 세로 + x좌표 + y좌표

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")
    global photo2 #함수가 끝나도 garbage collection이 불필요하다고 생각해서 지우지 않도록 글로벌로 변수 선언
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop()