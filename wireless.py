from tkinter import *
from tkinter import PhotoImage
from threading import Thread
from wifi import Cell, Scheme
import subprocess
x = subprocess.Popen("whoami",shell=True,stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
if "root" in (str(x.communicate())):
	print("You are logged as root")
	root = Tk()
	root.title("Wireless Viewer")
	root.geometry("396x411")
	root.resizable(False,False)
	root.configure(bg="white")

	# // Imag
	root_image_1 = PhotoImage(file="img/wireless.png")
	# // Entry
	root_entry_1 = Entry(root,width=36,font=("Arial",16),borderwidth=0, highlightcolor="#1ac6ff",fg="#1ac6ff")
	root_entry_1.place(x=0, y=381)
	# // Text
	root_label_1 = Label(root, image=root_image_1)
	root_label_1.place(x=0, y=0)
	# // Canva
	#root_canvas_1 = Canvas(root, height=3, borderwidth=0, bg="#00ffff")
	#root_canvas_1.place(x=0, y=328)
	# // Listbox
	root_listbox_1 = Listbox(root, width=33, bg="#00ffff", borderwidth=0, highlightcolor="white", fg="white", font=("Arial",16))
	root_listbox_1.place(x=-1, y=120)

	def wireless_scanner():
		root_listbox_1.delete(0, END)
		root_entry_1.delete(0, END)
		try:
			a = list(Cell.all('wlan0'))
			root_entry_1.insert(INSERT," Wireless adapter is detected")
			for x in a:
				root_listbox_1.insert(1," " + (str(x)).replace("Cell(ssid=","").replace(")",""))
		except:
			root_entry_1.insert(INSERT," Wireless adapter is not detected")

	root_button_1 = Button(root, text="Scan", width=46, fg="white", bg="#1ac6ff", borderwidth=0, command=lambda : Thread(target=wireless_scanner).start())
	root_button_1.place(x=0, y=94)
	root.mainloop()
else:
	print("You are not logged as root")

