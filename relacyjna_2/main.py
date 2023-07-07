import tkinter as tk
from tkinter import ttk
import re

from database import Database


class UniManagementApp:
    def __init__(self):
        self.filter_entry = []

        def toggle_filter_input():
            if self.do_filter_results_bool.get() == 1:
                self.filter_frame.pack()
            else:
                self.filter_frame.pack_forget()

        self.current_tab = None
        self.db = Database()
        self.tables = {}
        self.table_data = {}  # Store table data in memory

        for key in self.db.get_keys():
            self.tables[key] = self.db.get_column(key)
            self.table_data[key] = self.db.get(key)  # Fetch table data and store in memory

        self.window = tk.Tk()
        self.window.title("Uni management db")

        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill="both", expand=True)

        for table in self.tables:
            # create tabs
            tab = ttk.Frame(self.notebook, name=table)
            self.notebook.add(tab, text=table)

        self.notebook.bind("<<NotebookTabChanged>>", self.tab_changed)
        self.do_filter_results_bool = tk.IntVar()

        self.create_filter_frame()

        # Add Refresh and Set Filter buttons
        button_frame = ttk.Frame(self.window)
        button_frame.pack(pady=10)

        label = tk.Label(button_frame, text="WARNING, TABLES TAKE TIME TO UPDATE!!!")
        label.config(font=("TkDefaultFont", 12, "bold"), fg="red")
        label.pack()

        refresh_button = ttk.Button(button_frame, text="Refresh", command=self.refresh_tab)
        refresh_button.pack(side="left", padx=5)

        filter_checkbox = tk.Checkbutton(button_frame, text="Filter results", variable=self.do_filter_results_bool,
                                         command=toggle_filter_input)
        filter_checkbox.pack(side="right", padx=5)

        create_button = ttk.Button(button_frame, text="Create entry", command=self.create_entry)
        create_button.pack(side="left", padx=5)

        update_button = ttk.Button(button_frame, text="Update entry", command=self.create_update_popup)
        update_button.pack(side="left", padx=5)

        delete_button = ttk.Button(button_frame, text="Delete entry", command=self.create_delete_popup)
        delete_button.pack(side="left", padx=5)

        self.filter_frame = ttk.Frame(self.window)

    def tab_changed(self, event):
        self.do_filter_results_bool.set(False)
        selected_tab = event.widget.winfo_children()[event.widget.index("current")]
        tab_id = event.widget.index("current")
        tab_name = event.widget.tab(tab_id, "text")
        self.current_tab = tab_name
        print("Selected tab:", tab_name)

        # Get the column names for the selected tab
        column_names = self.tables[tab_name]
        num_columns = len(column_names)

        # Clear existing columns in the tab
        for widget in selected_tab.winfo_children():
            widget.destroy()

        # Create a canvas for scrolling
        treeview = ttk.Treeview(selected_tab, columns=column_names, show="headings")
        treeview.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(selected_tab, orient="vertical", command=treeview.yview)
        treeview.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Configure the treeview columns
        [treeview.heading(col, text=col) for col in column_names]
        [treeview.column(col, width=100, anchor="center") for col in column_names]

        # Fetch data from memory and display it in the frame
        rows = self.table_data[tab_name]
        for row in rows:
            values = [val if val is not None else "" for val in row]
            treeview.insert("", tk.END, values=values)

        for col in column_names:
            treeview.heading(col, command=lambda c=col: self.sort_column(treeview, c, False))

        for widget in self.filter_frame.winfo_children():
            widget.destroy()

        # create filter field
        self.filter_entry = []
        for index, column in enumerate(column_names):
            label = tk.Label(self.filter_frame, text=column)
            label.grid(row=0, column=index, padx=(2, 3))

            filter_entry = tk.Entry(self.filter_frame)
            filter_entry.grid(row=1, column=index, padx=(2, 3))
            self.filter_entry.append(filter_entry)

    def refresh_tab(self):
        # Get the currently selected tab
        tab_id = self.notebook.select()
        tab_name = self.notebook.tab(tab_id, "text")

        # Perform the refresh operation for the selected tab
        # Fetch the updated data and display it again

        # Clear existing data in the tab
        selected_tab = self.notebook.nametowidget(tab_id)
        treeview = selected_tab.winfo_children()[0]  # Assume the treeview is the first child
        treeview.delete(*treeview.get_children())

        # Get the column names for the selected tab
        column_names = self.tables[tab_name]

        # Fetch data from the database and display it in the treeview
        rows = self.db.get(tab_name)  # Fetch updated data from the database
        for row in rows:
            values = [val if val is not None else "" for val in row]
            treeview.insert("", tk.END, values=values)

    def sort_column(self, treeview, col, reverse):
        """Sort the treeview contents by the specified column."""
        data = [(treeview.set(child, col), child) for child in treeview.get_children("")]
        data.sort(reverse=reverse)

        for index, (_, child) in enumerate(data):
            treeview.move(child, "", index)

        # Reverse sort order for next click on the same column
        treeview.heading(col, command=lambda c=col: self.sort_column(treeview, c, not reverse))

    def create_entry(self):
        def create_entry():
            keys = [label["text"] for label in labels]
            values = [entry.get() for entry in entries]
            self.db.create_entry(self.current_tab, keys, query=values)
            self.refresh_tab()

        labels = []
        entries = []
        top = tk.Toplevel()
        top.title("Create entry in {} table".format(self.current_tab))
        top.wm_minsize(width=600, height=-1)
        top.grid_columnconfigure(0, weight=1)

        content = tk.Frame(top)
        content.grid(row=0, column=0, sticky="we", padx=10, pady=(1, 2), columnspan=3)
        content.grid_columnconfigure(2, weight=1)  # Configure column 0 to have weight

        for index, column in enumerate(self.tables[self.current_tab]):
            if column == "id" or column == "join_date" or column == "semester" or column == "student_count":
                continue

            if re.search(r"\bid_[a-zA-z]*\b", column):
                label = tk.Label(content, text=column[3:])
                label.grid(row=index, column=1)
                labels.append(label)

                query = self.db.get(column[3:])
                values = [" ".join(map(str, row)) for row in query]

                opt = tk.Listbox(content)
                opt.insert(tk.END, *values)
                opt.grid(row=index, column=2, sticky="we", padx=10, pady=(1, 2))  # Remove fill="both" option

                entries.append(opt)
            else:
                label = tk.Label(content, text=column)
                label.grid(row=index, column=1)
                labels.append(label)

                entry = tk.Entry(content)
                entry.grid(row=index, column=2, sticky="we", padx=10, pady=(1, 2))
                entries.append(entry)

        button_frame = tk.Frame(top)
        button_frame.grid(row=1, column=0)

        create_button = ttk.Button(button_frame, text="Create", command=create_entry)
        create_button.pack(side="left", padx=5)

        clear_button = ttk.Button(button_frame, text="Clear", command=None)
        clear_button.pack(side="left", padx=5)

        content.grid(sticky="nsew")

        top.mainloop()

    def create_delete_popup(self):
        def delete_entry():
            selected_entry = entry_listbox.get(tk.ACTIVE)
            if selected_entry:
                self.db.delete_entry(self.current_tab, selected_entry)
                self.refresh_tab()
            top.destroy()

        top = tk.Toplevel()
        top.title("Delete Entry")
        top.minsize(width=600, height=-1)
        top.grid_columnconfigure(0, weight=1)

        content = tk.Frame(top)
        content.grid(row=0, column=0, sticky="we", padx=10, pady=(1, 2))
        content.grid_columnconfigure(0, weight=1)  # Configure column 0 to have weight

        label = tk.Label(content, text="Select entry to delete:")
        label.grid(row=0, column=0, sticky="we")

        # Create a new frame for the entry_listbox
        listbox_frame = tk.Frame(content)
        listbox_frame.grid(row=1, column=0, sticky="nsew")

        entry_listbox = tk.Listbox(listbox_frame)
        entry_listbox.pack(fill="both", expand=True)

        # Fetch the entries from the current tab's data
        tab_id = self.notebook.select()
        tab_name = self.notebook.tab(tab_id, "text")
        rows = self.table_data[tab_name]

        # Fetch the column names for the selected tab
        column_names = self.tables[tab_name]

        # Create a template string to format the values for display
        template = " | ".join(["{}"] * len(column_names))

        for row in rows:
            # Format the row values using the template
            formatted_row = template.format(*row)
            entry_listbox.insert(tk.END, formatted_row)

        delete_button = ttk.Button(content, text="Delete", command=delete_entry)
        delete_button.grid(row=2, column=0, pady=10)

    def create_update_popup(self):
        def update_entry():
            selected_entry = entry_listbox.get(tk.ACTIVE)
            if selected_entry:
                # Get the column names and values to update
                columns = [label["text"] for label in labels]
                values = [entry.get() for entry in entries]

                # Call the update_entry method from the Database class
                self.db.update_entry(self.current_tab, selected_entry, columns, values)
                self.refresh_tab()
            top.destroy()

        top = tk.Toplevel()
        top.title("Update Entry")
        top.minsize(width=600, height=-1)
        top.grid_columnconfigure(0, weight=1)

        content = tk.Frame(top)
        content.grid(row=0, column=0, sticky="we", padx=10, pady=(1, 2))
        content.grid_columnconfigure(0, weight=1)  # Configure column 0 to have weight

        labels = []
        entries = []

        label = tk.Label(content, text="Select entry to update:")
        label.grid(row=0, column=0, sticky="we")

        # Create a new frame for the entry_listbox
        listbox_frame = tk.Frame(content)
        listbox_frame.grid(row=1, column=0, sticky="nsew")

        entry_listbox = tk.Listbox(listbox_frame)
        entry_listbox.pack(fill="both", expand=True)

        # Fetch the entries from the current tab's data
        tab_id = self.notebook.select()
        tab_name = self.notebook.tab(tab_id, "text")
        rows = self.table_data[tab_name]

        # Fetch the column names for the selected tab
        column_names = self.tables[tab_name]

        # Create a template string to format the values for display
        template = " | ".join(["{}"] * len(column_names))

        for row in rows:
            # Format the row values using the template
            formatted_row = template.format(*row)
            entry_listbox.insert(tk.END, formatted_row)

        for index, column in enumerate(column_names):
            if column == "id" or column == "join_date" or column == "semester" or column == "student_count":
                continue

            label = tk.Label(content, text=column)
            label.grid(row=index + 2, column=0, sticky="we")
            labels.append(label)

            entry = tk.Entry(content)
            entry.grid(row=index + 2, column=1, sticky="we", padx=10, pady=(1, 2))
            entries.append(entry)

        update_button = ttk.Button(content, text="Update", command=update_entry)
        update_button.grid(row=len(column_names) + 2, column=0, pady=10)

        top.mainloop()

    def apply_filter(self):
        # Get the filter value from the entry field
        filter_value = self.filter_entry.get()

        # Get the currently selected tab
        tab_id = self.notebook.select()
        tab_name = self.notebook.tab(tab_id, "text")

        # Clear existing data in the tab
        selected_tab = self.notebook.nametowidget(tab_id)
        treeview = selected_tab.winfo_children()[0]  # Assume the treeview is the first child
        treeview.delete(*treeview.get_children())

        # Get the column names for the selected tab
        column_names = self.tables[tab_name]

        # Fetch data from the database and display it in the treeview
        rows = self.db.get(tab_name)  # Fetch updated data from the database
        for row in rows:
            values = [val if val is not None else "" for val in row]

            # Apply the filter by checking if the filter value exists in any of the row values
            if filter_value.lower() in [str(value).lower() for value in values]:
                treeview.insert("", tk.END, values=values)

    def create_filter_frame(self):
        self.filter_frame = ttk.Frame(self.window)
        self.filter_frame.pack()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = UniManagementApp()
    app.run()
