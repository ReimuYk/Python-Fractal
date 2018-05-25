from tkinter import *
from math import *

# select[0] 科赫雪花
def drawKochLine(n,start,end):
    if n==0:
        c.create_line(start+end)
        return
    p1 = start
    p2 = ((start[0]*2+end[0])/3,(start[1]*2+end[1])/3)
    p2 = (int(p2[0]),int(p2[1]))
    p3x = start[0]/2+end[0]/2+start[1]*sqrt(3)/6-end[1]*sqrt(3)/6
    p3y = start[1]/2+end[1]/2+end[0]*sqrt(3)/6-start[0]*sqrt(3)/6
    p3 = (int(p3x),int(p3y))                            
    p4 = ((start[0]+end[0]*2)/3,(start[1]+end[1]*2)/3)
    p4 = (int(p4[0]),int(p4[1]))
    p5 = end
    l = [p1,p2,p3,p4,p5]
    for i in range(4):
        drawKochLine(n-1,l[i],l[i+1])
def drawKoch(n):
    p1 = (40,375)
    p2 = (460,375)
    p3 = (250,11)
    drawKochLine(n,p3,p1)
    drawKochLine(n,p2,p3)
    drawKochLine(n,p1,p2)

# select[1] 圆形窗花
def drawChuangSingle(n,start,end):
    c.create_oval(start+end,fill='white')
    if n==0:
        return
    center=(int((start[0]+end[0])/2),int((start[1]+end[1])/2))
    rr = int((start[0]-end[0])/4)#小圆半径
    # 井字 上下左右
    l = center[0]-rr
    r = center[0]+rr
    u = center[1]-rr
    d = center[1]+rr
    # oval up
    c.create_oval((l,start[1],r,center[1]))
    # oval down
    c.create_oval((l,center[1],r,end[1]))
    # oval left
    c.create_oval((start[0],u,center[0],d))
    # oval right
    c.create_oval((center[0],u,end[0],d))
    new_r = sqrt(2)*rr
    new_start = (center[0]-new_r,center[1]-new_r)
    new_end = (center[0]+new_r,center[1]+new_r)
    drawChuangSingle(n-1,new_start,new_end)
def drawChuang(n):
    start = (50,50)
    end = (450,450)
    drawChuangSingle(n,start,end)

def run():
    global c,n,selectvalue,func
    num = n.get()
    c = Canvas(root,height=500,width=500,bg='white')
    c.place(x=0,y=0)
    runtype = func[selectvalue.get()]
    runtype(num)
    print(selectvalue.get())

def nextstep():
    global n
    n.set(n.get()+1)
    run()

select = ['科赫雪花','圆形窗花']
func = [drawKoch,drawChuang]

root = Tk()
root.title("Fractal")
root.geometry("700x500")
c = Canvas(root,height=500,width=500,bg='white')
f = Frame(root,height=len(select)*30,width=200)
selectvalue = IntVar()
for i in range(len(select)):
    Radiobutton(f,variable = selectvalue,text=select[i],value=i).pack()
Label(f,text='阶数:').pack()
n = IntVar()
Entry(f,textvariable=n).pack()
Button(f,text='draw',command=run).pack()
Button(f,text='next',command=nextstep).pack()
c.place(x=0,y=0)
f.place(x=525,y=100)
root.mainloop()
