from tkinter import *
import random

counter = 0
contador = 0
segundinhos = 2000

def adicionar():
	global contador
	global segundinhos

	contador += 1
	segundinhos -= 30
	print("Contador: " + str(contador) + "\nSegundos: " + str(segundinhos))

	x1 = random.randint(0, 492)
	y1 = random.randint(0, 570)
	button.place(x = x1, y = y1)

def anda():
	global segundinhos
	x1 = random.randint(0, 492)
	y1 = random.randint(0, 570)
	button.place(x = x1, y = y1)
	root.after(segundinhos, anda)

def counter_label(label):
	counter = 0
	def count():
		global counter
		counter += 1
		label.config(text = str(counter))
		label.after(1000, count)
		if counter == 61:
			root.destroy()
	count()
 
root = Tk()
root.title("Macacada 3")
root.geometry("600x600")
root.call('wm', 'iconphoto', root._w, PhotoImage(file='bandeira.png'))
root.resizable(False, False)
label = Label(root, fg="dark green")
label.config(font=("Arial", 16))
label.pack()
counter_label(label)
button = Button(root, text = 'Vem', highlightbackground = "black", width = 10, fg = 'white', bg = 'black', command = adicionar)
button.place(x = random.randint(0, 492), y = random.randint(0, 570))

anda()

root.mainloop()