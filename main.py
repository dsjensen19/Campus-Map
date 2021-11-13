import tkinter as tk
import webbrowser
from PIL import ImageTk, Image
def snowmap():
    #This creates the main window of an application
    webbrowser.open('https://webmailbyui.sharepoint.com/sites/CFP/Shared%20Documents/Forms/AllItems.aspx?RootFolder=%2Fsites%2FCFP%2FShared%20Documents%2FSnow&FolderCTID=0x0120000301951975D9094788730A1C6253FD45')

def hartmap():
    webbrowser.open('https://webmailbyui.sharepoint.com/sites/CFP/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x0120000301951975D9094788730A1C6253FD45&id=%2Fsites%2FCFP%2FShared%20Documents%2FHart&viewid=c7754805%2Df989%2D47bd%2D8123%2Df292b2edd195')
    pass

def byuimap():
    webbrowser.open('https://webmailbyui.sharepoint.com/sites/CFP/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x0120000301951975D9094788730A1C6253FD45&id=%2Fsites%2FCFP%2FShared%20Documents%2FBYU%2DI%20Center&viewid=c7754805%2Df989%2D47bd%2D8123%2Df292b2edd195')
    pass

def mckaymap():
    webbrowser.open('https://webmailbyui.sharepoint.com/sites/CFP/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x0120000301951975D9094788730A1C6253FD45&id=%2Fsites%2FCFP%2FShared%20Documents%2FMcKay%20Library&viewid=c7754805%2Df989%2D47bd%2D8123%2Df292b2edd195')
    pass

def smithmap():
    webbrowser.open('https://webmailbyui.sharepoint.com/sites/CFP/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x0120000301951975D9094788730A1C6253FD45&id=%2Fsites%2FCFP%2FShared%20Documents%2FSmith&viewid=c7754805%2Df989%2D47bd%2D8123%2Df292b2edd195')
    pass

def mcmap():
    webbrowser.open('https://webmailbyui.sharepoint.com/sites/CFP/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x0120000301951975D9094788730A1C6253FD45&id=%2Fsites%2FCFP%2FShared%20Documents%2FManwaring%20Center&viewid=c7754805%2Df989%2D47bd%2D8123%2Df292b2edd195')
    pass

def taylormap():
    webbrowser.open('https://webmailbyui.sharepoint.com/sites/CFP/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x0120000301951975D9094788730A1C6253FD45&id=%2Fsites%2FCFP%2FShared%20Documents%2FTaylor&viewid=c7754805%2Df989%2D47bd%2D8123%2Df292b2edd195')
    pass

def kimballmap():
    webbrowser.open('https://webmailbyui.sharepoint.com/sites/CFP/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x0120000301951975D9094788730A1C6253FD45&id=%2Fsites%2FCFP%2FShared%20Documents%2FKimball&viewid=c7754805%2Df989%2D47bd%2D8123%2Df292b2edd195')
    pass

def austinmap():
    webbrowser.open('https://webmailbyui.sharepoint.com/sites/CFP/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x0120000301951975D9094788730A1C6253FD45&id=%2Fsites%2FCFP%2FShared%20Documents%2FAustin&viewid=c7754805%2Df989%2D47bd%2D8123%2Df292b2edd195')
    pass

def ricksmap():
    webbrowser.open('https://webmailbyui.sharepoint.com/sites/CFP/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x0120000301951975D9094788730A1C6253FD45&id=%2Fsites%2FCFP%2FShared%20Documents%2FRicks&viewid=c7754805%2Df989%2D47bd%2D8123%2Df292b2edd195')
    pass

def hinckleymap():
    webbrowser.open('https://webmailbyui.sharepoint.com/sites/CFP/Shared%20Documents/Forms/AllItems.aspx?FolderCTID=0x0120000301951975D9094788730A1C6253FD45&id=%2Fsites%2FCFP%2FShared%20Documents%2FHinckley&viewid=c7754805%2Df989%2D47bd%2D8123%2Df292b2edd195')
    pass


def main():
    #This creates the main window of an application
    Nwindow = tk.Tk()
    Nwindow.title("Campus")
    Nwindow.geometry("500x650")
    Nwindow.configure(background='grey')

    path = "mapItself.jpg"

    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    img = ImageTk.PhotoImage(Image.open(path))

    #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    panel = tk.Label(Nwindow, image = img)

    #The Pack geometry manager packs widgets in rows or columns.
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    #Snow button
    Snow = tk.Button(text="Snow", height= 1, command=snowmap)
    Snow.place(x=103, y=70)

    #Hart button
    Hart = tk.Button(text="Hart", height= 1, command=hartmap)
    Hart.place(x=50, y=165)

    #Icenter button
    byui = tk.Button(text="BYU I Center", height= 1, command=byuimap)
    byui.place(x=31, y=237)
    
    #McKay button
    Mckay = tk.Button(text="McKay", height= 1, command=mckaymap)
    Mckay.place(x=140, y=201)
    
    #Smith button
    Smith = tk.Button(text="Smith", height= 1, command=smithmap)
    Smith.place(x=221, y=212)
    
    #MC button
    MC = tk.Button(text="MC", height= 1, command=mcmap)
    MC.place(x=184, y=280)

    #Taylor button
    Taylor = tk.Button(text="Talyor", height= 1, command=taylormap)
    Taylor.place(x=168, y=354)

    #Kimball button
    Kimball = tk.Button(text="Kimball", height= 1, command=kimballmap)
    Kimball.place(x=213, y=372)

    #Austin button
    Austin = tk.Button(text="Austin", height= 1, command=austinmap)
    Austin.place(x=67, y=444)

    #Ricks button
    Ricks = tk.Button(text="Ricks", height= 1, command=ricksmap)
    Ricks.place(x=214, y=487)
    
    #Hinckley button
    Hinkley = tk.Button(text="Hinkley", height= 1, command=hinckleymap)
    Hinkley.place(x=270, y=456)
    
    #Start the GUI
    Nwindow.mainloop()

main()