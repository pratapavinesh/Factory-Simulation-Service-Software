import tkinter as tk
from tkinter import ttk
import json


def result():

    #MAIN WINDOW
    root = tk.Tk()
    root.title('RESULT')
    root.geometry('600x600')

    result = []

    with open('result.json', 'r') as f:
        # Load the JSON data from the file
        data1 = json.load(f)

    result = data1
    # print(result)
    # print(result['avg_machine_util'])
    # print("dsada")

    #LABEL FOR ADJUSTER UTILITY
    aau = ttk.Label(master = root, text = f'Average Adjuster Utilization: {result["avg_adjuster_util"]}')
    aau.pack()

    #ADJUSTER TABLE
    au = result['adjuster_util']
    au_keys = list(au)
    au_values = list(au.values())

    tree1 = tk.ttk.Treeview(root, columns=("Adjuster Type", "Utilization in %"), show="headings")
    tree1.heading("Adjuster Type", text="Adjuster Type")
    tree1.heading("Utilization in %", text="Utilization in %")
    tree1.pack()

    for i1,i2 in zip(au_keys,au_values):
        tree1.insert("", tk.END, values=(i1, i2))

    #LABEL FOR MACHINE UTILITY
    aau = ttk.Label(master = root, text = f'Average Machine Utilization: {result["avg_machine_util"]}')
    aau.pack()

    #MACHINE TABLE
    mu = result['machine_util']
    mu_keys = list(mu)
    mu_values = list(mu.values())

    tree2 = tk.ttk.Treeview(root, columns=("Machine Name", "Utilization in %"), show="headings")
    tree2.heading("Machine Name", text="Machine Name")
    tree2.heading("Utilization in %", text="Utilization in %")
    tree2.pack()

    for i1,i2 in zip(mu_keys,mu_values):
        tree2.insert("", tk.END, values=(i1, i2))

    #RUN
    root.mainloop()