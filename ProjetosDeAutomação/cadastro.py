import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Cadastro de Alunos")

tree = ttk.Treeview(root, columns=('name', 'email'))
tree.heading('name', text='Name')
tree.heading('email', text='Email')
tree.pack()

label_name = tk.Label(root, text='Name')
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()
label_email = tk.Label(root, text='Email')
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

def add_student():
    name = entry_name.get()
    email = entry_email.get()
    tree.insert('', 'end', values=(name, email))
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    
button_add = tk.Button(root, text='Salvar', command=add_student)
button_add.pack()

root.mainloop()