# n=int(input('sonni kiriting:'))
# k=int(input(' k sonni kiriting:'))
# for i in range(n):
#     print(k)
#



#
# v=a/1000
# print("km=", v)


# def f(r):
#       for i in range(r):
#           print(' '*(r-i-1)+'*'*(2*i+1))
#
# f(7)
# my=[[1], [2, 3], [4, 5, 6]]
#
# bo= sum(my, [])
# print(bo)
# bo = {1, 3, 4, 5, 6}
#
# bo.discard(2)
# print(bo)


#
# n=int(input("son="))
# for i in range(2, int(n**0.5)+1):
#     if n% i ==0:
#       break
#
# else:
#    print(True)
#


# con= 0
#
# def yes():
#     con += 1
#
# yes()

#
#
# from turtle import *
#
# def floo():
#     for i in range(300):
#         circle(190-i, 90)
#         left(90)
#         circle(190-i, 90)
#         left(18)
#
# floo()
# mainloop()

#
# word = input("text kiriting=")
# let  =  input("harf  kiriting=")
#
# def find(word, let):
#     for i in word:
#         if i==let:
#           d=word.count(i)
#     print(d)
#
# find(word, let)


# import tkinter as tk
#
# class App(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)
#         self.pack()
#
#         self.entrythingy = tk.Entry()
#         self.entrythingy.pack()
#
#         # Create the application variable.
#         self.contents = tk.StringVar()
#         # Set it to some value.
#         self.contents.set("this is a variable")
#         # Tell the entry widget to watch this variable.
#         self.entrythingy["textvariable"] = self.contents
#
#         # Define a callback for when the user hits return.
#         # It prints the current value of the variable.
#         self.entrythingy.bind('<Key-Return>',
#                              self.print_contents)
#
#     def print_contents(self, event):
#         print("Hi. The current entry content is:",
#               self.contents.get())
#
# root = tk.Tk()
# myapp = App(root)eef
# myapp.mainloop()


# import netfilterqueue
# def process_packet(packet):
#     print(packet)
#     packet.accept()
#
# q = netfilterqueue.NetfilterQueue()
# q.bind(0,  process_packet)
# q.run()

# import tkinter as tk
# import pystray
# from PIL import Image
#
#
# class MyApp(tk.Tk):
#           def __init__(self):
#                     super().__init__()
#
#                     self.title("System Tray App")
#                     self.geometry('300x150')
#                     self.protocol('WM_DELETE_WINDOW', self.minimize_to_tray)
#
#           def minimize_to_tray(self):
#                     self.withdraw()
#                     image = Image.open("1.jpg")
#                     menu = (pystray.MenuItem('Quit', self.quit_window),
#                             pystray.MenuItem('Show', self.show_window))
#                     icon = pystray.Icon("name", image, "My App", menu)
#                     icon.run()
#
#           def quit_window(self, icon):
#                     icon.stop()
#                     self.destroy()
#
#           def show_window(self, icon):
#                     icon.stop()
#                     self.after(0, self.deiconify)
#
#
# if __name__ == "__main__":
#           app = MyApp()
#           app.mainloop()

import tkinter as tk


root = tk.Tk()

# place a label on the root window
message = tk.Label(root, text="Web dasturlash kursiga hush kelibsiz !")
message.pack()

# keep the window displaying
root.mainloop()