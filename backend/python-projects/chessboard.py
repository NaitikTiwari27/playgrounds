import tkinter as tk

root = tk.Tk()
root.title("Chessboard")

size = 70
canvas = tk.Canvas(root, width=8*size, height=8*size)
canvas.pack()

for i in range(0,9):
    for j in range(0,9):
        color = ""
        if (i+j) % 2 == 0:
            color = "white"
        else:
            color = "black"
        canvas.create_rectangle(j*size, i*size, (j+1)*size, (i+1)*size, fill=color)
'''top left corner of the rectangle = (j*size, i*size) and bottom right corner = ((j+1)*size, (i+1)*size)'''

root.mainloop()