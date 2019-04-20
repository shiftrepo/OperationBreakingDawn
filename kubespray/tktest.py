import tkinter

root = tkinter.Tk()

root.title("This is a tkinter sample")
root.geometry("300x200")

canvas = tkinter.Canvas(root, width=300, height=200)
canvas.create_rectangle(10, 10, 30, 60, fill='yellow')
canvas.place(x=0, y=0)

root.mainloop()
