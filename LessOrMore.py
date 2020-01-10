from tkinter import * 
from random import randrange
import time


diff = 0

def setDiff(diff): 
    if diff == 1:
        diff = 1
        global cg
        global timed
        timed = time.time()
        cg = randrange(1,1000)
        entree["state"] = "normal"
        tryb["state"] = "normal"
        tryb["command"] = tryGame1
        entree.bind("<Return>", tryGame1)

    elif diff == 2:
        diff = 2
        cg = randrange(1,5000)
        timed = time.time()
        entree["state"] = "normal"
        tryb["state"] = "normal"
        tryb["command"] = tryGame2
        entree.bind("<Return>", tryGame2)
    elif diff == 3:
        diff = 3
        timed = time.time()
        cg = randrange(1,10000)
        entree["state"] = "normal"
        tryb["state"] = "normal"
        tryb["command"] = tryGame3
        entree.bind("<Return>", tryGame3)



hits = 0
def changeHits(nbr):
    global hits
    hits = int(nbr)

timerLose = 0
def changeTime(tps):
    global timerLose
    timerLose = int(tps)

count = 0
def tryGame1(self):
    global count
    G = int(entree.get())
    if G > cg and count < hits and time.time()-timed < timerLose:
        count = count + 1
        hlce["text"] = "Plus petit !"
    elif G < cg and count < hits and time.time()-timed < timerLose:
        count = count + 1
        hlce["text"] = "Plus grand !"
    elif G == cg:
        winwindow = Tk()
        timer = int(time.time()) - int(timed)
        wl = LabelFrame(winwindow, text="Félicitations !", padx=20, pady=20)
        wl.pack(fill="both", expand="yes")
        WonTexte = str("Bien joué ! Vous avez gagné la partie en :" + str(count) + " coups.\nDe plus vous avez mis : " + str(timer) + " secondes. \nDe plus le nombre à trouver étais : " + str(cg) +".\n Nous aviez choisi la difficulté " + str(diff) +".")
        wintext = Label(wl, text=WonTexte)
        wintext.pack()
    else:
        hlce["text"] = "Vous n'avez plus de coup / plus de temps ! \n Le chiffre étais : " + str(cg)
        entree["state"] = "disabled"
        tryb["state"] = "disabled"

def tryGame2(self):
    global count
    G = int(entree.get())
    if G > cg and count < hits and time.time()-timed < timerLose:
        count = count + 1
        hlce["text"] = "Plus petit !"
    elif G < cg and count < hits and time.time()-timed < timerLose:
        count = count + 1
        hlce["text"] = "Plus grand !"
    elif G == cg:
        winwindow = Tk()
        timer = int(time.time()) - int(timed)
        wl = LabelFrame(winwindow, text="Félicitations !", padx=20, pady=20)
        wl.pack(fill="both", expand="yes")
        WonTexte = str("Bien joué ! Vous avez gagné la partie en :" + str(count) + " coups.\nDe plus vous avez mis : " + str(timer) + " secondes. \nDe plus le nombre à trouver étais : " + str(cg) +".\n Nous aviez choisi la difficulté " + str(diff) +".")
        wintext = Label(wl, text=WonTexte)
        wintext.pack()
    else:
        hlce["text"] = "Vous n'avez plus de coup / plus de temps ! \n Le chiffre étais : " + str(cg)
        entree["state"] = "disabled"
        tryb["state"] = "disabled"

def tryGame3(self):
    global count
    G = int(entree.get())
    if G > cg and count < hits and time.time()-timed < timerLose:
        count = count + 1
        hlce["text"] = "Plus petit !"
    elif G < cg and count < hits and time.time()-timed < timerLose:
        count = count + 1
        hlce["text"] = "Plus grand !"
    elif G == cg:
        winwindow = Tk()
        timer = int(time.time()) - int(timed)
        wl = LabelFrame(winwindow, text="Félicitations !", padx=20, pady=20)
        wl.pack(fill="both", expand="yes")
        WonTexte = str("Bien joué ! Vous avez gagné la partie en :" + str(count) + " coups.\nDe plus vous avez mis : " + str(timer) + " secondes. \nDe plus le nombre à trouver étais : " + str(cg) +".\n Nous aviez choisi la difficulté " + str(diff) +".")
        wintext = Label(wl, text=WonTexte)
        wintext.pack()
    else:
        hlce["text"] = "Vous n'avez plus de coup / plus de temps ! \n Le chiffre étais : " + str(cg)
        entree["state"] = "disabled"
        tryb["state"] = "disabled"



fenetre = Tk()
value = 0

l = LabelFrame(fenetre, text="Le jeu du plus ou moins | + or - Game !", padx=20, pady=20)
l.pack(fill="both", expand="yes")

entree = Entry(l, width=75, state="disabled")
entree.pack()

tryb = Button(l, text="Essayer", command = tryGame1, state="disabled")
tryb.pack(side="left")

hlce = Label(l, text="Veuillez choisir une difficulté, Bonne chance !") 
hlce.pack(side="bottom")

diffs = LabelFrame(fenetre, text="Choix de la difficulté :", padx=20, pady=20)
diffs.pack(fill="both", expand="yes")

diff3 = Button(diffs, text="3 (Difficile): 10000", command = lambda: setDiff(3))
diff3.pack(side="bottom")

diff2 = Button(diffs, text="2 (Normal): 5000", command = lambda: setDiff(2))
diff2.pack(side="bottom")

diff1 = Button(diffs, text="1 (Facile) : 1000", command = lambda: setDiff(1))
diff1.pack(side="bottom")

entrcoups = Entry(diffs, width=45)
entrcoups.pack(side="right")
diff1 = Button(diffs, text="Changer le nombre de coups maximum \n(Laisser vide si pas de limite de coups)", command = lambda: changeHits(entrcoups.get()))
diff1.pack(side="right")

entrtime = Entry(diffs, width=45)
entrtime.pack(side="right")
difftime = Button(diffs, text="Changer le temps maximum \n(Laisser vide si pas de limite de temps)", command = lambda: changeTime(entrtime.get()))
difftime.pack(side="right")


fenetre.mainloop()