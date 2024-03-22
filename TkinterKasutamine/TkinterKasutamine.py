#from tkinter import *
#k=0
#def vajuta_():
#    global k
#    k+=1
#    nupp.configure(text=k)

#def vajuta__(event):
#    global k
#    k-=1

#def tst_psse(event):
#    t=textbox.get()
#    pealkiri.configure(text=t,width=len(t))
#    textbox.delete(0,END)

#def valik():
#    arv=var.get()
#    textbox.insert(arv)


#aken=Tk()
#aken.geometry("350x350")
#aken.iconbitmap("icon.ico")
#aken.title("Sup_my_hommies")
#tekst="Dungeon_master\n"
#pealkiri=Label(aken,
#               text=tekst, 
#               bg="#5b1d76", 
#               fg="#468499", 
#               font="Algerian 20", 
#               height=3,
#               width=len(tekst))
#textbox=Entry(aken, 
#              bg="#5b1d76", 
#              fg="#468499", 
#              font="Algerian 20",
#              width=20, 
#              justify=CENTER) #show="*" 
#nupp=Button(aken,
#            text="Vajuta mind!",
#            font="Arial 20",
#            height=3, width=10,
#            relief=RAISED, 
#            bg="LightBlue",
#            command=vajuta_) #SUNKER, #GROOVE
#f=Frame(aken)
#var=IntVar()
#e=Radiobutton(f,text="Esimine",variable=var, value=1, font="Algerian 20", command=valik)
#t=Radiobutton(f,text="Teine",variable=var, value=2, font="Algerian 20", command=valik)
#K=Radiobutton(f,text="Kolmas",variable=var, value=3, font="Algerian 20", command=valik)
#nupp.bind("<Button-3>", vajuta_) #PKM
#textbox.bind=("<Return>",tst_psse) #Enter         

#obj=[pealkiri, textbox, nupp,f]
#for i in obj:
#    i.pack()
#obj2=[e,t,k]
#for i in range (len(obj2)):
#    obj[i].grid(row=0,colomun=i)


#pealkiri.pack()
#textbox.pack()
#nupp.pack()
#aken.mainloop()

from tkinter import *
aken = Tk()
aken.geometry("975x475")
tekst = "Решение квадаратного уравнения\n"
pealkiri=Label(aken,
               text=tekst, 
               bg="#5b1d76", 
               fg="#468499", 
               font="Algerian 20", 
               height=3,
               width=len(tekst))
textbox=Entry(aken, 
              bg="#5b1d76", 
              fg="#468499", 
              font="Algerian 20",
              width=15)

pealkiri.pack()
textbox.pack(side = LEFT)
textbox.pack(side = LEFT)
aken.mainloop()
             