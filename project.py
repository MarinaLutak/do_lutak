import itertools
import numpy as np
from numpy import random
from scipy.optimize import linear_sum_assignment
from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk, Image

class TaskAssignment:

    def __init__(self, task_matrix, mode):
        self.task_matrix = task_matrix
        self.mode = mode
        if mode == 'all_permutation':
            self.min_cost, self.best_solution = self.all_permutation(task_matrix)
        if mode == 'Hungary':
            self.min_cost, self.best_solution = self.Hungary(task_matrix)


    def all_permutation(self, task_matrix):
        number_of_choice = len(task_matrix)
        solutions = []
        values = []
        for each_solution in itertools.permutations(range(number_of_choice)):
            each_solution = list(each_solution)
            solution = []
            value = 0
            for i in range(len(task_matrix)):
                value += task_matrix[i][each_solution[i]]
                solution.append(task_matrix[i][each_solution[i]])
            values.append(value)
            solutions.append(solution)
        min_cost = np.min(values)
        best_solution = solutions[values.index(min_cost)]
        return min_cost, best_solution


    def Hungary(self, task_matrix):
        b = task_matrix.copy()
        for i in range(len(b)):
            row_min = np.min(b[i])
            for j in range(len(b[i])):
                b[i][j] -= row_min
        for i in range(len(b[0])):
            col_min = np.min(b[:, i])
            for j in range(len(b)):
                b[j][i] -= col_min
        line_count = 0

        while (line_count < len(b)):
            line_count = 0
            row_zero_count = []
            col_zero_count = []
            for i in range(len(b)):
                row_zero_count.append(np.sum(b[i] == 0))
            for i in range(len(b[0])):
                col_zero_count.append((np.sum(b[:, i] == 0)))

            line_order = []
            row_or_col = []
            for i in range(len(b[0]), 0, -1):
                while (i in row_zero_count):
                    line_order.append(row_zero_count.index(i))
                    row_or_col.append(0)
                    row_zero_count[row_zero_count.index(i)] = 0
                while (i in col_zero_count):
                    line_order.append(col_zero_count.index(i))
                    row_or_col.append(1)
                    col_zero_count[col_zero_count.index(i)] = 0
            delete_count_of_row = []
            delete_count_of_rol = []
            row_and_col = [i for i in range(len(b))]
            for i in range(len(line_order)):
                if row_or_col[i] == 0:
                    delete_count_of_row.append(line_order[i])
                else:
                    delete_count_of_rol.append(line_order[i])
                c = np.delete(b, delete_count_of_row, axis=0)
                c = np.delete(c, delete_count_of_rol, axis=1)
                line_count = len(delete_count_of_row) + len(delete_count_of_rol)

                if line_count == len(b):
                    break

                if 0 not in c:
                    row_sub = list(set(row_and_col) - set(delete_count_of_row))
                    min_value = np.min(c)
                    for i in row_sub:
                        b[i] = b[i] - min_value
                    for i in delete_count_of_rol:
                        b[:, i] = b[:, i] + min_value
                    break
        row_ind, col_ind = linear_sum_assignment(b)
        min_cost = task_matrix[row_ind, col_ind].sum()
        best_solution = list(task_matrix[row_ind, col_ind])
        return min_cost, best_solution

arr = []
root = Tk()
root.geometry('1400x700')
def f1():
    global a1, a2, a3,a4,a5,a6,a7,a8,a9
    global root
    i = []
    i.append(int(a1.get()))
    i.append(int(a2.get()))
    i.append(int(a3.get()))
    arr.append(i)
    i = []
    i.append(int(a4.get()))
    i.append(int(a5.get()))
    i.append(int(a6.get()))
    arr.append(i)
    i = []
    i.append(int(a7.get()))
    i.append(int(a8.get()))
    i.append(int(a9.get()))
    arr.append(i)
    arr1 = np.array(arr)
    ass_by_per = TaskAssignment(arr1, 'all_permutation')
    # Используйте метод Венгрии для распределения задач
    ass_by_Hun = TaskAssignment(arr1, 'Hungary')
    lbl = Label(root, text="Мінімальна вартість: " + str(ass_by_Hun.min_cost), font=("Arial Bold", 16)).place(x=1100, y=110)
    print('best solution = ', ass_by_Hun.best_solution)
    sol = []
    for i in range(3):
        for j in range(3):
            if ass_by_Hun.best_solution[i] == arr[i][j]:
                sol.append(1)
            else:
                sol.append(0)

    print(sol)
    image1 = Image.open("lopatnik.png")
    image1 = image1.resize((100, 140))
    image1 = ImageTk.PhotoImage(image1)
    panel1 = Label(root, image=image1).place(x=530, y=130)
    image2 = Image.open("kistnik.png")
    image2 = image2.resize((100, 140))
    image2 = ImageTk.PhotoImage(image2)
    panel2 = Label(root, image=image2).place(x=530, y=280)
    image3 = Image.open("kluchnik.png")
    image3 = image3.resize((100, 140))
    image3 = ImageTk.PhotoImage(image3)
    panel3 = Label(root, image=image3).place(x=530, y=430)
    image4 = Image.open("lopata.jpg")
    image4 = image4.resize((100, 100))
    image4 = ImageTk.PhotoImage(image4)
    panel4 = Label(root, image=image4).place(x=640, y=27)
    image5 = Image.open("kist.jpg")
    image5 = image5.resize((100, 100))
    image5 = ImageTk.PhotoImage(image5)
    panel5 = Label(root, image=image5).place(x=760, y=27)
    image6 = Image.open("kluch.jpg")
    image6 = image6.resize((100, 100))
    image6 = ImageTk.PhotoImage(image6)
    panel6 = Label(root, image=image6).place(x=880, y=27)
    a1 = Label(text = str(sol[0]),width=8, justify='center', font=("Arial Bold", 13), bg = 'white')
    a1.place(x=655, y=180, height=45)
    a2 = Label(text = str(sol[1]),width=8, justify='center', font=("Arial Bold", 13), bg = 'white')
    a2.place(x=775, y=180, height=45)
    a3 = Label(text = str(sol[2]),width=8, justify='center', font=("Arial Bold", 13), bg = 'white')
    a3.place(x=895, y=180, height=45)
    a4 = Label(text = str(sol[3]),width=8, justify='center', font=("Arial Bold", 13), bg = 'white')
    a4.place(x=655, y=325, height=45)
    a5 = Label(text = str(sol[4]),width=8, justify='center', font=("Arial Bold", 13), bg = 'white')
    a5.place(x=775, y=325, height=45)
    a6 = Label(text = str(sol[5]),width=8, justify='center', font=("Arial Bold", 13), bg = 'white')
    a6.place(x=895, y=325, height=45)
    a7 = Label(text = str(sol[6]),width=8, justify='center', font=("Arial Bold", 13), bg = 'white')
    a7.place(x=655, y=470, height=45)
    a8 = Label(text = str(sol[7]),width=8, justify='center', font=("Arial Bold", 13), bg = 'white')
    a8.place(x=775, y=470, height=45)
    a9 = Label(text = str(sol[8]),width=8, justify='center', font=("Arial Bold", 13), bg = 'white')
    a9.place(x=895, y=470, height=45)
    root.mainloop()

image1 = Image.open("lopatnik.png")
image1 = image1.resize((100,140))
image1 = ImageTk.PhotoImage(image1)
panel1 = Label(root, image = image1).place(x=50,y=130)
image2 = Image.open("kistnik.png")
image2 = image2.resize((100,140))
image2 = ImageTk.PhotoImage(image2)
panel2 = Label(root, image = image2).place(x=50,y=280)
image3 = Image.open("kluchnik.png")
image3 = image3.resize((100,140))
image3 = ImageTk.PhotoImage(image3)
panel3 = Label(root, image = image3).place(x=50,y=430)
image4 = Image.open("lopata.jpg")
image4 = image4.resize((100,100))
image4 = ImageTk.PhotoImage(image4)
panel4 = Label(root, image = image4).place(x=160,y=27)
image5 = Image.open("kist.jpg")
image5 = image5.resize((100,100))
image5 = ImageTk.PhotoImage(image5)
panel5 = Label(root, image = image5).place(x=280,y=27)
image6 = Image.open("kluch.jpg")
image6 = image6.resize((100,100))
image6 = ImageTk.PhotoImage(image6)
panel6 = Label(root, image = image6).place(x=400,y=27)
a1 = Entry(width = 8, justify = 'center', font=("Arial Bold", 13))
a1.place(x=175, y=180, height = 45)
a2 = Entry(width = 8, justify = 'center', font=("Arial Bold", 13))
a2.place(x=295, y=180, height = 45)
a3 = Entry(width = 8, justify = 'center', font=("Arial Bold", 13))
a3.place(x=415, y=180, height = 45)
a4 = Entry(width = 8, justify = 'center', font=("Arial Bold", 13))
a4.place(x=175, y=325, height = 45)
a5 = Entry(width = 8, justify = 'center', font=("Arial Bold", 13))
a5.place(x=295, y=325, height = 45)
a6 = Entry(width = 8, justify = 'center', font=("Arial Bold", 13))
a6.place(x=415, y=325, height = 45)
a7 = Entry(width = 8, justify = 'center', font=("Arial Bold", 13))
a7.place(x=175, y=470, height = 45)
a8 = Entry(width = 8, justify = 'center', font=("Arial Bold", 13))
a8.place(x=295, y=470, height = 45)
a9 = Entry(width = 8, justify = 'center', font=("Arial Bold", 13))
a9.place(x=415, y=470, height = 45)

btn1 = Button(text="Ok", command = f1,width = 8, justify = 'center', font=("Arial Bold", 16), bg = 'black', fg = 'white')
btn1.place(x=295, y = 600, height = 45)


root.mainloop()