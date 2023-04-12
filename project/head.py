import tkinter as tk
from tkinter import ttk
import json
from calculation import simulate
from result import result

def head():

    machines = []
    adjusters = []

    # Open the file for reading
    with open('machines.json', 'r') as f:
        # Load the JSON data from the file
        data1 = json.load(f)

    # Store the data in a list
    machines = list(data1)
    # print(machines)

    # Open the file for reading
    with open('adjusters.json', 'r') as f:
        # Load the JSON data from the file
        data2 = json.load(f)

    # Store the data in a list
    adjusters = list(data2)
    # print(adjusters)

    #FUNCTIONS

    def cal():
        y = int(years.get())
        # print(type(y))
        ans = simulate(adjusters,machines,y)
        # print(ans)
        with open('result.json','w') as outfile:
            json.dump(ans,outfile)
        result()
        

    # {"avg_machine_util": 89.86, "avg_adjuster_util": 28.77, "machine_util": {"abc": 94.79, "def": 87.4}, "adjuster_util": {"1": 28.77}}

    #MAIN WINDOW
    root = tk.Tk()
    root.title('HEAD')

    #MACHINE TABLE
    # create a table with 4 columns
    columns = ('Machine Name', 'MTTF', 'Repair Time', 'Quantity')
    table_machine = ttk.Treeview(root, columns=columns, show='headings')

    # set the headings for each column
    for col in columns:
        table_machine.heading(col, text=col)

    for i, row in enumerate(machines):
        values = (row["machineName"], row["MTTF"], row["repairTime"],row["quantity"])
        table_machine.insert(parent="", index="end", iid=i, text=str(i+1), values=values)

    # pack the table to the window
    table_machine.pack()
    # table_machine.pack(expand=True, fill="both")

    #ADJUSTER TABLE
    # create a table with 4 columns
    columns = ('Adjuster Type', 'Expertise', 'Number of Adjusters')
    table_adjuster = ttk.Treeview(root, columns=columns, show='headings')

    # set the headings for each column
    for col in columns:
        table_adjuster.heading(col, text=col)

    for i, row in enumerate(adjusters):
        values = (row["adjusterType"], row["expertise"], row["numberOfAdjusters"])
        table_adjuster.insert(parent="", index="end", iid=i, text=str(i+1), values=values)

    # pack the table to the window
    table_adjuster.pack()
    # table_machine.pack(expand=True, fill="both")
    label = ttk.Label(root, text="Years:")
    years = ttk.Entry(master = root)
    sim = ttk.Button(master = root, text = 'Simulate', command = cal)
    label.pack()
    years.pack()
    sim.pack()


    #RUN
    root.mainloop()