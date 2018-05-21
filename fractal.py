from tkinter import *
from math import *

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
    

select = ['科赫雪花']

root = Tk()
root.title("Fractal")
root.geometry("700x500")
c = Canvas(root,height=500,width=500,bg='white')
f = Frame(root,height=len(select)*30,width=200,bg='blue')
selectvalue = IntVar()
for i in range(len(select)):
    Radiobutton(f,variable = selectvalue,text=select[i],value=i).pack()
c.place(x=0,y=0)
f.place(x=550,y=0)
drawKoch(2)
root.mainloop()
