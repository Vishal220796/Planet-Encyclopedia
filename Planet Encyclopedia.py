from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Planet Encycolopedia")
root.geomatry("500x500")
root.config(bg="lightblue")

Mercury = ImageTk.PhotoImage(Image.open ("Mercury.jpg"))
Venus = ImageTk.PhotoImage(Image.open ("Venus.jpg"))
Earth = ImageTk.PhotoImage(Image.open ("Earth.jpg"))
Mars = ImageTk.PhotoImage(Image.open ("Mars.jpg"))
Jupiter = ImageTk.PhotoImage(Image.open ("Jupiter.jpg"))
Saturn = ImageTk.PhotoImage(Image.open ("Saturn.jpg"))
Uranus = ImageTk.PhotoImage(Image.open ("Uranus.jpg"))
Neptune = ImageTk.PhotoImage(Image.open ("Neptune.jpg"))

label_planet = Label(root, text="Planet : ", bg="Lightblue")
label_planet_name = Label(root,font=("courier",18,"bold"),bg="lightblue")
LABEL_planet_image = Label(root,bg="gold2", highlightthickness=5, borderwidth=2,relief=SOLID)
label_planet_gravity_radius = Label(root,font=("castellar"), bg="lightblue")
label_planet_info = Label(root,font=("courier",10,"bold"), bg="lightblue", wrap=500)

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
selectedval = StringVar()
dropdown = ttk.Combobox(root, values = planets, textvariable=selectdval)

def PlanetInfo():
    planet = selectedvl.get()
    if planet == "Mercury":
        label_planet_name['text']= "Mercury"
        label_planet_image['image'] = Mercury
        label_planet_gravity_radius-radius['text'] = "Gravity : 3.7 m/s² \n Radius : 2,439.7 km"
        label_planet_info['text'] = " Mercury is the smallest planet in the Solar System and the closest to the Sun"