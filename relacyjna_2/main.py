import tkinter as tk
from tkinter import ttk
import re
import tkinter.font as tk_font

from database import Database


class ToolTip(tk.Toplevel):
    def __init__(self, parent, text, x, y):
        tk.Toplevel.__init__(self, parent)
        self.wm_overrideredirect(True)
        self.wm_geometry(f"+{x}+{y + 20}")
        self.label = tk.Label(self, text=text, background="#FFFFDD", relief="solid", borderwidth=1)
        self.label.pack()

    def show(self):
        self.lift()


class UniManagementApp:
    def __init__(self):
        self.filter_entry = []

        self.current_tab = None
        self.db = Database()
        self.tables = {}
        self.table_data = {}  # Store table data in memory

        for key in self.db.get_keys():
            self.tables[key] = self.db.get_column(key)
            self.table_data[key] = self.db.get(key)  # Fetch table data and store in memory

        self.window = tk.Tk()
        self.window.title("Uni management db")
        self.window.minsize(width=1024, height=-1)

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

        label = tk.Label(button_frame, text="WARNING, TABLES TAKE TIME TO UPDATE!!!")
        label.config(font=("TkDefaultFont", 12, "bold"), fg="red")
        label.pack()

        refresh_button = ttk.Button(button_frame, text="Refresh", command=self.refresh_tab)
        refresh_button.pack(side="left", padx=5)

        create_button = ttk.Button(button_frame, text="Create entry", command=self.create_entry)
        create_button.pack(side="left", padx=5)

        update_button = ttk.Button(button_frame, text="Update entry", command=self.create_update_popup)
        update_button.pack(side="left", padx=5)

        delete_button = ttk.Button(button_frame, text="Delete entry", command=self.create_delete_popup)
        delete_button.pack(side="left", padx=5)

    def tab_changed(self, event):
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

        # Set the stretch attribute of each column to True
        for col in column_names:
            treeview.column(col, stretch=True)

        # Fetch data from memory and display it in the frame
        rows = self.table_data[tab_name]
        for row in rows:
            values = [val if val is not None else "" for val in row]
            treeview.insert("", tk.END, values=values)

        # Adjust column widths to fit the content
        for col in column_names:
            treeview.column(col, width=tk_font.Font().measure(col))  # Set initial width based on the column name

            # Iterate through rows to determine the required width for each column
            for row in rows:
                value = row[column_names.index(col)]
                width = tk_font.Font().measure(value)
                if width > treeview.column(col, "width"):
                    treeview.column(col, width=width)

        self.refresh_tab()

    def refresh_tab(self):
        # Get the currently selected tab
        tab_id = self.notebook.select()
        tab_name = self.notebook.tab(tab_id, "text")

        self.table_data[self.current_tab] = self.db.get(self.current_tab)
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
            self.db.create_entry(tab, keys, query=values)
            self.refresh_tab()

        tab = self.current_tab
        labels = []
        entries = []
        top = tk.Toplevel()
        top.title("Create entry in {} table".format(self.current_tab))
        top.wm_minsize(width=600, height=-1)
        top.grid_columnconfigure(0, weight=1)

        content = tk.Frame(top)
        content.grid(row=0, column=0, sticky="we", padx=10, pady=(1, 2), columnspan=2)
        content.grid_columnconfigure(1, weight=1)  # Configure column 0 to have weight

        for index, column in enumerate(self.tables[self.current_tab]):
            if column == "id" or column == "join_date" or column == "semester" or column == "student_count":
                continue

            label = tk.Label(content, text=column)
            label.grid(row=index, column=0)
            labels.append(label)

            entry = tk.Entry(content)
            entry.grid(row=index, column=1, sticky="we", padx=10, pady=(1, 2))
            entries.append(entry)

        button_frame = tk.Frame(top)
        button_frame.grid(row=1, column=0, columnspan=2)

        create_button = ttk.Button(button_frame, text="Create", command=create_entry)
        create_button.pack(side="left", padx=5)

        content.grid(sticky="nsew")

        top.mainloop()

    def create_delete_popup(self):
        def delete_entry():
            selected_entry = entry_listbox.get(tk.ACTIVE)
            if selected_entry:
                self.db.delete_entry(tab, selected_entry)
                self.refresh_tab()
            top.destroy()

        tab = self.current_tab
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
                self.db.update_entry(tab, selected_entry, columns, values)
                self.refresh_tab()
            top.destroy()

        tab = self.current_tab
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
            if column == "id" or column == "join_date" or column == "semester" or column == "student_count" or column == "staff_count" or column == "occupancy":
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

    def show_tooltip(self, event, treeview, column):
        x, y, _, _ = treeview.bbox(treeview.identify_row(event.y))
        item = treeview.item(treeview.identify_row(event.y))
        value = item["values"][column]

        tooltip = ToolTip(treeview, text=value, x=x, y=y)
        tooltip.show()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = UniManagementApp()
    app.run()
