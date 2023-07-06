import tkinter as tk
from tkinter import ttk

from database import Database


class UniManagementApp:
    def __init__(self):
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

        # Add Refresh and Set Filter buttons
        button_frame = ttk.Frame(self.window)
        button_frame.pack(pady=10)

        refresh_button = ttk.Button(button_frame, text="Refresh", command=self.refresh_tab)
        refresh_button.pack(side="left", padx=5)

        filter_button = ttk.Button(button_frame, text="Set Filter", command=self.set_filter)
        filter_button.pack(side="left", padx=5)

        create_button = ttk.Button(button_frame, text="Create entry", command=self.create_entry)
        create_button.pack(side="left", padx=5)

        update_button = ttk.Button(button_frame, text="Update entry", command=self.update_entry)
        update_button.pack(side="left", padx=5)

        delete_button = ttk.Button(button_frame, text="Delete entry", command=self.delete_entry)
        delete_button.pack(side="left", padx=5)

    def tab_changed(self, event):
        selected_tab = event.widget.winfo_children()[event.widget.index("current")]
        tab_id = event.widget.index("current")
        tab_name = event.widget.tab(tab_id, "text")
        self.current_tab = tab_name
        print("Selected tab:", tab_name)

        # Clear existing columns in the tab
        for widget in selected_tab.winfo_children():
            widget.destroy()

        # Get the column names for the selected tab
        column_names = self.tables[tab_name]
        num_columns = len(column_names)

        # Create a canvas for scrolling
        treeview = ttk.Treeview(selected_tab, columns=column_names, show="headings")
        treeview.pack(side="left", fill="both", expand=True)

        for column in column_names:
            treeview.heading(column, text=column)
            treeview.column(column, width=100, anchor="center")

        # Fetch data from memory and display it in the frame
        rows = self.table_data[tab_name]
        for row in rows:
            values = []
            for col, val in enumerate(row):
                if val is None:
                    val = ""
                if col == 0:  # Treat the first element as int
                    val = int(val)
                values.append(val)
            treeview.insert("", tk.END, values=values)

        for col in column_names:
            treeview.heading(col, command=lambda c=col: self.sort_column(treeview, c, False))

    def refresh_tab(self):
        # Get the currently selected tab
        tab_id = self.notebook.select()
        tab_name = self.notebook.tab(tab_id, "text")

        # Perform the refresh operation for the selected tab
        # Fetch the updated data and display it again

        # Clear existing data in the tab
        selected_tab = self.notebook.nametowidget(tab_id)
        for widget in selected_tab.winfo_children():
            widget.destroy()

        # Get the column names for the selected tab
        column_names = self.tables[tab_name]
        num_columns = len(column_names)

        # Create a treeview widget and add data to it
        treeview = ttk.Treeview(selected_tab, columns=column_names, show="headings")
        treeview.pack(side="left", fill="both", expand=True)

        # Configure the treeview columns
        for column in column_names:
            treeview.heading(column, text=column)
            treeview.column(column, width=100, anchor="center")

        rows = self.table_data[tab_name]
        for row in rows:
            values = []
            for col, val in enumerate(row):
                if val is None:
                    val = ""
                values.append(val)
            treeview.insert("", tk.END, values=values)

        # Enable sorting by clicking on column headers
        for col in column_names:
            treeview.heading(col, command=lambda c=col: self.sort_column(treeview, c, False))

    def sort_column(self, treeview, col, reverse):
        """Sort the treeview contents by the specified column."""
        data = [(treeview.set(child, col), child) for child in treeview.get_children("")]
        data.sort(reverse=reverse)

        for index, (_, child) in enumerate(data):
            treeview.move(child, "", index)

        # Reverse sort order for next click on the same column
        treeview.heading(col, command=lambda c=col: self.sort_column(treeview, c, not reverse))

    def set_filter(self):
        # Code for setting a filter on the current tab
        # Implement your logic to set a filter for the data displayed in the tab

        # You can access the currently selected tab using:
        tab_id = self.notebook.select()
        tab_name = self.notebook.tab(tab_id, "text")

        # Use the tab_name to determine the specific tab on which to apply the filter

    def create_entry(self):
        def create_entry():
            values = [entry.get() for entry in entries]
            self.db.filter_query(self.current_tab, columns=self.tables[self.current_tab], query=values)

        entries = []
        top = tk.Toplevel()
        top.wm_title("Create entry in {} table".format(self.current_tab))
        top.wm_minsize(width=600, height=-1)
        top.grid_columnconfigure(0, weight=1)
        top.grid_rowconfigure(0, weight=1)
        top.resizable(False, False)

        content = tk.Frame(top)
        content.grid(column=0, row=0, sticky="nsew")
        content.grid_columnconfigure(2, weight=1)  # Configure column 2 to have weight

        for index, column in enumerate(self.tables[self.current_tab]):
            label = tk.Label(content, text=column)
            label.grid(row=index, column=1)

            entry = tk.Entry(content)
            entry.grid(row=index, column=2, sticky="we", padx=10, pady=(1, 2))
            entries.append(entry)

        button_frame = tk.Frame(top)
        button_frame.grid(row=1, column=0)

        create_button = ttk.Button(button_frame, text="Create", command=lambda: create_entry())
        create_button.pack(side="left", padx=5)

        clear_button = ttk.Button(button_frame, text="Clear", command=None)
        clear_button.pack(side="left", padx=5)

        cancel_button = ttk.Button(button_frame, text="Cancel", command=None)
        cancel_button.pack(side="left", padx=5)

        content.grid(sticky="nsew")

        top.mainloop()

    def update_entry(self):
        None

    def delete_entry(self):
        None

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = UniManagementApp()
    app.run()
