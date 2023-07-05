import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from tkinter import Scrollbar
from database import Database


class UniManagementApp:
    def __init__(self):
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

    def tab_changed(self, event):
        selected_tab = event.widget.winfo_children()[event.widget.index("current")]
        tab_id = event.widget.index("current")
        tab_name = event.widget.tab(tab_id, "text")
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

    def sort_column(self, treeview, col, reverse):
        """Sort the treeview contents by the specified column."""
        data = [(treeview.set(child, col), child) for child in treeview.get_children("")]
        data.sort(reverse=reverse)

        for index, (_, child) in enumerate(data):
            treeview.move(child, "", index)

        # Reverse sort order for next click on the same column
        treeview.heading(col, command=lambda c=col: self.sort_column(treeview, c, not reverse))

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = UniManagementApp()
    app.run()
