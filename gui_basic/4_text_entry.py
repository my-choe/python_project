from tkinter import *

root = Tk()
root.title("GUI Project")
root.geometry("640x480+600+300") # 가로 * 세로 + x좌표 + y좌표

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요") #기본값

e = Entry(root, width=30) #엔터 입력 불가(로그인 같은 곳에서 사용)
e.pack()
e.insert(0, "한줄만 입력")

def btncmd():

    #내용 출력
    print(txt.get("1.0", END)) #1.0 =  라인 1부터 컬럼기준으로 0번째 위치에서부터 가져와라
    print(e.get()) #엔트리는 그냥 get만

    #내용 삭제
    txt.delete("1.0", END) #모두 삭제
    e.delete(0, END) #0부터 끝까지 삭제

    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()