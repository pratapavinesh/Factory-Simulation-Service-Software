import tkinter as tk
from tkinter import ttk
import json

def manager():

    machines = []
    adjusters = []
    machineNames = []

    #FUNCTIONS
    def add_entry_table_machine():
        m_name = machine_name.get()
        mttf = int(MTTF.get())
        r_time = int(repair_time.get())
        q = int(quantity.get())
        machine={}
        machine["machineName"] = m_name
        machine["MTTF"] = mttf
        machine["repairTime"] = r_time
        machine["quantity"] = q
        machines.append(machine)
        machineNames.append(m_name)
        last_machine = machines[-1:]
        table_machine.insert('', 'end', values=(f'{last_machine[0]["machineName"]}', f'{last_machine[0]["MTTF"]}', f'{last_machine[0]["repairTime"]}', f'{last_machine[0]["quantity"]}'))

    # def display_machine():
    #     for i in machines:
    #         print(i)

    # def display_adjuster():
    #     for i in adjusters:
    #         print(i)

    def add_entry_table_adjuster():
        id = adjuster_id.get()
        f = selected_items
        q = int(quantity_adjuster.get())
        adjuster={}
        adjuster["adjusterType"] = id
        adjuster["expertise"] = f
        adjuster["numberOfAdjusters"] = q
        adjusters.append(adjuster)
        last_adjuster = adjusters[-1:]
        table_adjuster.insert('', 'end', values=(f'{last_adjuster[0]["adjusterType"]}', f'{last_adjuster[0]["expertise"]}', f'{last_adjuster[0]["numberOfAdjusters"]}'))

    def done():
        with open('machines.json', 'w') as outfile:
        # Write the JSON data to the file
            json.dump(machines, outfile)
        with open('adjusters.json', 'w') as outfile:
        # Write the JSON data to the file
            json.dump(adjusters, outfile)
        root.destroy()


    def update_dropdown_menu():
        dropdown_menu.menu.delete(0, tk.END)
        for item in machineNames:
            dropdown_menu.menu.add_checkbutton(label=item, command=lambda i=item: update_selected_items(i))

    def update_selected_items(machineNames):
        if machineNames in selected_items:
            selected_items.remove(machineNames)
        else:
            selected_items.append(machineNames)

    def show_selected_items():
        if selected_items:
            print("Selected items:", selected_items)
        else:
            print("Please select at least one item.")

    #MAIN WINDOW
    root = tk.Tk()
    root.title('SERVICE MANAGER')


    #TABS
    tabcontrol = ttk.Notebook(master = root)
    tab1 = ttk.Frame(tabcontrol)
    tab2 = ttk.Frame(tabcontrol)
    tabcontrol.add(tab1, text ='Add Machine')
    tabcontrol.add(tab2, text ='Add Adjuster')
    tabcontrol.pack()

    #INSIDE TAB 1

    # create a table with 4 columns
    columns = ('Machine Name', 'MTTF', 'Repair Time', 'Quantity')
    table_machine = ttk.Treeview(tab1, columns=columns, show='headings')

    # set the headings for each column
    for col in columns:
        table_machine.heading(col, text=col)

    # pack the table to the window
    table_machine.pack()


    machine_name = ttk.Entry(master = tab1)
    machine_name.insert(0, "Enter Machine Name")
    machine_name.pack()
    MTTF = ttk.Spinbox(master = tab1)
    MTTF.insert(0, "Enter Mean Time to Failure")
    MTTF.pack()
    repair_time = ttk.Spinbox(master = tab1)
    repair_time.insert(0, "Enter Repair Time")
    repair_time.pack()
    quantity = ttk.Spinbox(master = tab1)
    quantity.insert(0, "Enter Quantity")
    quantity.pack()
    submit = ttk.Button(master = tab1,text = 'Add', command = add_entry_table_machine)
    submit.pack()

    #DISPLAY CONENT INSIDE TERMINAL
    # show = ttk.Button(master = tab1,text = 'Show', command = display_machine)
    # show.pack()


    #INSIDE TAB 2


    # create a table with 4 columns
    columns = ('Adjuster ID', 'Fix', 'Number of Adjuster')
    table_adjuster = ttk.Treeview(tab2, columns=columns, show='headings')

    # set the headings for each column
    for col in columns:
        table_adjuster.heading(col, text=col)


    # pack the table to the window
    table_adjuster.pack()

    adjuster_id = ttk.Entry(master = tab2)
    adjuster_id.insert(0, "Enter Adjuster ID")
    adjuster_id.pack()


    # fix = ttk.Spinbox(master = tab2)
    # fix.insert(0, "type")
    # fix.pack()


    # List of items for the dropdown menu
    # items = ["Option 1", "Option 2", "Option 3", "Option 4"]


    # List to hold the selected items
    selected_items = []

    # Create the dropdown menu
    dropdown_menu = tk.Menubutton(tab2, text="Select options", relief=tk.RAISED)
    dropdown_menu.menu = tk.Menu(dropdown_menu, tearoff=0)
    dropdown_menu["menu"] = dropdown_menu.menu
    update_dropdown_menu()

    # Create the dropdown button
    dropdown_menu.pack()

    # Create the Submit button
    submit_button = ttk.Button(tab2, text="Submit", command=show_selected_items)
    submit_button.pack()

    # Create a button to update the dropdown menu
    update_button = ttk.Button(tab2, text="Update options", command=update_dropdown_menu)
    update_button.pack()


    quantity_adjuster = ttk.Spinbox(master = tab2)
    quantity_adjuster.insert(0, "Enter Number of Adjuster")
    quantity_adjuster.pack()
    submit = ttk.Button(master = tab2,text = 'Add', command = add_entry_table_adjuster)
    submit.pack()

    #DISPLAY CONENT INSIDE TERMINAL
    # show = ttk.Button(master = tab2,text = 'Show', command = display_adjuster)
    # show.pack()


    #OUPUT TO A FILE

    done = ttk.Button(master = root, text = 'Done', command = done)
    done.pack()


    #RUN
    root.mainloop()