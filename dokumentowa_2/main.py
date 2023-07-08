from io import BytesIO
from tkinter import ttk, filedialog, messagebox
import tkinter as tk
from mongoengine import DoesNotExist
from database import Database, Client, Drink, Meal, Order, Delivery, Picture
from PIL import Image, ImageTk


class WindowClient:
    def __init__(self):
        self.tabs = []
        self.window = tk.Tk()
        self.window.title("Restaurant database")
        self.window.minsize(1024, 600)
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=(2, 3))
        self.tabs.append(self.add_tab(Drink, "Drinks"))
        self.tabs.append(self.add_tab(Meal, "Meals"))
        self.tabs.append(self.add_tab(Order, "Orders"))
        self.tabs.append(self.add_tab(Delivery, "Deliveries"))

    def add_tab(self, obj_class, tab_name):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=tab_name)

        # Retrieve data from the database
        data = obj_class.objects()

        # Create a treeview widget to display the data
        treeview = ttk.Treeview(tab)
        treeview.pack(fill=tk.BOTH, expand=True)

        # Define the columns in the treeview
        if obj_class == Drink:
            treeview["columns"] = ("id", "name", "type", "price", "picture")
            treeview.column("#0", width=0, stretch=tk.NO)  # Hide the first column
            treeview.heading("id", text="ID")
            treeview.heading("name", text="Name")
            treeview.heading("type", text="Type")
            treeview.heading("price", text="Price")
            treeview.heading("picture", text="Picture")
        elif obj_class == Meal:
            treeview["columns"] = ("id", "name", "description", "price", "picture")
            treeview.column("#0", width=0, stretch=tk.NO)  # Hide the first column
            treeview.heading("id", text="ID")
            treeview.heading("name", text="Name")
            treeview.heading("description", text="Description")
            treeview.heading("price", text="Price")
            treeview.heading("picture", text="Picture")
        elif obj_class == Order:
            treeview["columns"] = ("id", "client", "dateOfOrder", "dateOfDelivery", "status")
            treeview.column("#0", width=0, stretch=tk.NO)  # Hide the first column
            treeview.heading("id", text="ID")
            treeview.heading("client", text="Client")
            treeview.heading("dateOfOrder", text="Order Date")
            treeview.heading("dateOfDelivery", text="Delivery Date")
            treeview.heading("status", text="Status")
        elif obj_class == Delivery:
            treeview["columns"] = ("id", "name", "company")
            treeview.column("#0", width=0, stretch=tk.NO)  # Hide the first column
            treeview.heading("id", text="ID")
            treeview.heading("name", text="Name")
            treeview.heading("company", text="Company")

        # Populate the treeview with data
        for item in data:
            if obj_class == Drink:
                picture_names = [p.name for p in item.picture] if item.picture else []
                picture_name = ", ".join(picture_names)
                treeview.insert("", tk.END, text="", values=(item.id, item.name, item.type, item.price, picture_name))
            elif obj_class == Meal:
                picture_names = [p.name for p in item.picture] if item.picture else []
                picture_name = ", ".join(picture_names)
                treeview.insert("", tk.END, text="", values=(item.id, item.name, item.type, item.price, picture_name))
            elif obj_class == Order:
                client_name = item.client.name if item.client else ""
                treeview.insert("", tk.END, text="",
                                values=(item.id, client_name, item.dateOfOrder, item.dateOfDelivery, item.status))
            elif obj_class == Delivery:
                treeview.insert("", tk.END, text="", values=(item.id, item.name, item.company))

        # Add scrollbar to the treeview
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=treeview.yview)
        treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create buttons for CRUD operations (Create, Update, Delete)
        create_button = ttk.Button(tab, text="Create", command=self.create_object)
        create_button.pack(side=tk.LEFT, padx=5, pady=5, anchor="s")

        update_button = ttk.Button(tab, text="Update", command=lambda: self.update_object(treeview, obj_class))
        update_button.pack(side=tk.LEFT, padx=5, pady=5, anchor="s")

        delete_button = ttk.Button(tab, text="Delete", command=lambda: self.delete_object(treeview, obj_class))
        delete_button.pack(side=tk.LEFT, padx=5, pady=5, anchor="s")

        # Bind a function to display the selected object's picture
        treeview.bind("<Double-Button-1>", lambda event: self.display_picture(event, treeview, obj_class))

        return tab

    def display_picture(self, event, treeview, obj_class):
        selected_item = treeview.focus()
        values = treeview.item(selected_item)["values"]
        picture_name = values[-1]  # Assuming picture column is the last column

        if picture_name:
            # Fetch the picture object from the database based on its name
            picture = Picture.objects(name=picture_name).first()

            if picture:
                # Display the picture in a new window
                picture_window = tk.Toplevel()
                picture_window.title("Picture")
                image = Image.open(BytesIO(picture.picture))
                photo = ImageTk.PhotoImage(image)
                label = tk.Label(picture_window, image=photo)
                label.image = photo
                label.pack()

    def create_object(self):
        current_tab = self.notebook.tab(self.notebook.select(), "text")
        if current_tab == "Drinks":
            form_window = tk.Toplevel()
            form_window.title("Create Drink")
            form_window.minsize(480, -1)
            drink_name_label = ttk.Label(form_window, text="Drink Name:")
            drink_name_label.pack()
            drink_name_entry = ttk.Entry(form_window)
            drink_name_entry.pack()
            drink_type_label = ttk.Label(form_window, text="Drink Type:")
            drink_type_label.pack()
            drink_type_entry = ttk.Entry(form_window)
            drink_type_entry.pack()
            drink_price_label = ttk.Label(form_window, text="Drink Price:")
            drink_price_label.pack()
            drink_price_entry = ttk.Entry(form_window)
            drink_price_entry.pack()
            picture_label = ttk.Label(form_window, text="Picture:")
            picture_label.pack()
            picture_path_label = ttk.Label(form_window, text="")
            picture_path_label.pack()

            def select_picture():
                file_path = filedialog.askopenfilename()
                picture_path_label.config(text=file_path)

            picture_button = ttk.Button(form_window, text="Select Picture", command=select_picture)
            picture_button.pack()

            def submit_form():
                drink_name = drink_name_entry.get()
                drink_type = drink_type_entry.get()
                drink_price = float(drink_price_entry.get())
                picture_path = picture_path_label.cget("text")

                drink = Drink(name=drink_name, type=drink_type, price=drink_price)

                if picture_path:
                    with open(picture_path, "rb") as f:
                        picture_data = f.read()
                    picture = Picture(name=drink_name, picture=picture_data)
                    picture.save()
                    drink.picture = [picture]
                    drink.save()

                form_window.destroy()

            submit_button = ttk.Button(form_window, text="Submit", command=submit_form)
            submit_button.pack()

        elif current_tab == "Meals":
            form_window = tk.Toplevel()
            form_window.title("Create Meal")
            form_window.minsize(480, -1)
            meal_name_label = ttk.Label(form_window, text="Meal Name:")
            meal_name_label.pack()
            meal_name_entry = ttk.Entry(form_window)
            meal_name_entry.pack()
            meal_price_label = ttk.Label(form_window, text="Meal Price:")
            meal_price_label.pack()
            meal_price_entry = ttk.Entry(form_window)
            meal_price_entry.pack()
            picture_label = ttk.Label(form_window, text="Picture:")
            picture_label.pack()
            picture_path_label = ttk.Label(form_window, text="")
            picture_path_label.pack()

            def select_picture():
                file_path = filedialog.askopenfilename()
                picture_path_label.config(text=file_path)

            picture_button = ttk.Button(form_window, text="Select Picture", command=select_picture)
            picture_button.pack()

            def submit_form():
                meal_name = meal_name_entry.get()
                meal_price = float(meal_price_entry.get())
                picture_path = picture_path_label.cget("text")

                meal = Meal(name=meal_name, price=meal_price)

                if picture_path:
                    with open(picture_path, "rb") as f:
                        picture_data = f.read()
                    picture = Picture(name=meal_name, picture=picture_data)
                    picture.save()
                    meal.picture = [picture]
                meal.save()

                form_window.destroy()

            submit_button = ttk.Button(form_window, text="Submit", command=submit_form)
            submit_button.pack()

        elif current_tab == "Orders":
            form_window = tk.Toplevel()
            form_window.title("Create Order")
            form_window.minsize(480, -1)
            client_id_label = ttk.Label(form_window, text="Client ID:")
            client_id_label.pack()
            client_id_entry = ttk.Entry(form_window)
            client_id_entry.pack()
            drinks_label = ttk.Label(form_window, text="Drinks (Name:Quantity):")
            drinks_label.pack()
            drinks_entry = ttk.Entry(form_window)
            drinks_entry.pack()
            meals_label = ttk.Label(form_window, text="Meals (Name:Quantity):")
            meals_label.pack()
            meals_entry = ttk.Entry(form_window)
            meals_entry.pack()
            order_date_label = ttk.Label(form_window, text="Order Date (YYYY-MM-DD HH:MM:SS):")
            order_date_label.pack()
            order_date_entry = ttk.Entry(form_window)
            order_date_entry.pack()
            delivery_date_label = ttk.Label(form_window, text="Delivery Date (YYYY-MM-DD HH:MM:SS):")
            delivery_date_label.pack()
            delivery_date_entry = ttk.Entry(form_window)
            delivery_date_entry.pack()
            status_label = ttk.Label(form_window, text="Status:")
            status_label.pack()
            status_entry = ttk.Entry(form_window)
            status_entry.pack()

            def submit_form():
                client_id = client_id_entry.get()
                drinks = drinks_entry.get()
                meals = meals_entry.get()
                order_date = order_date_entry.get()
                delivery_date = delivery_date_entry.get()
                status = status_entry.get()

                try:
                    client = Client.objects.get(id=client_id)
                except DoesNotExist:
                    messagebox.showerror("Error", f"Client with ID {client_id} does not exist.")
                    return

                order = Order(client=client, dateOfOrder=order_date, dateOfDelivery=delivery_date, status=status)

                drinks = drinks.split(",")
                for drink in drinks:
                    drink_data = drink.strip().split(":")
                    if len(drink_data) != 2:
                        messagebox.showerror("Error", f"Invalid drink format: {drink}.")
                        return

                    drink_name, quantity = drink_data
                    try:
                        drink_obj = Drink.objects.get(name=drink_name)
                        order.drinks.append(drink_obj)
                        order.drinks[-1].quantity = int(quantity)
                    except DoesNotExist:
                        messagebox.showerror("Error", f"Drink with name {drink_name} does not exist.")
                        return

                meals = meals.split(",")
                for meal in meals:
                    meal_data = meal.strip().split(":")
                    if len(meal_data) != 2:
                        messagebox.showerror("Error", f"Invalid meal format: {meal}.")
                        return

                    meal_name, quantity = meal_data
                    try:
                        meal_obj = Meal.objects.get(name=meal_name)
                        order.meals.append(meal_obj)
                        order.meals[-1].quantity = int(quantity)
                    except DoesNotExist:
                        messagebox.showerror("Error", f"Meal with name {meal_name} does not exist.")
                        return

                order.save()

                form_window.destroy()

            submit_button = ttk.Button(form_window, text="Submit", command=submit_form)
            submit_button.pack()

        elif current_tab == "Deliveries":
            form_window = tk.Toplevel()
            form_window.title("Create Delivery")
            form_window.minsize(480, -1)
            delivery_name_label = ttk.Label(form_window, text="Delivery Name:")
            delivery_name_label.pack()
            delivery_name_entry = ttk.Entry(form_window)
            delivery_name_entry.pack()
            company_label = ttk.Label(form_window, text="Company:")
            company_label.pack()
            company_entry = ttk.Entry(form_window)
            company_entry.pack()
            order_id_label = ttk.Label(form_window, text="Order ID:")
            order_id_label.pack()
            order_id_entry = ttk.Entry(form_window)
            order_id_entry.pack()

            def submit_form():
                delivery_name = delivery_name_entry.get()
                company = company_entry.get()
                order_id = order_id_entry.get()

                try:
                    order = Order.objects.get(id=order_id)
                except DoesNotExist:
                    messagebox.showerror("Error", f"Order with ID {order_id} does not exist.")
                    return

                delivery = Delivery(name=delivery_name, company=company)
                delivery.order.append(order)
                delivery.save()

                form_window.destroy()

            submit_button = ttk.Button(form_window, text="Submit", command=submit_form)
            submit_button.pack()

    def update_object(self, treeview, obj_class):
        selected_item = treeview.focus()
        values = treeview.item(selected_item)["values"]
        item_id = values[0]  # Assuming ID column is the first column

        if obj_class == Drink:
            form_window = tk.Toplevel()
            form_window.title("Update Drink")
            form_window.minsize(480, -1)
            drink_name_label = ttk.Label(form_window, text="Updated Drink Name:")
            drink_name_label.pack()
            drink_name_entry = ttk.Entry(form_window)
            drink_name_entry.pack()
            drink_type_label = ttk.Label(form_window, text="Updated Drink Type:")
            drink_type_label.pack()
            drink_type_entry = ttk.Entry(form_window)
            drink_type_entry.pack()
            drink_price_label = ttk.Label(form_window, text="Updated Drink Price:")
            drink_price_label.pack()
            drink_price_entry = ttk.Entry(form_window)
            drink_price_entry.pack()
            picture_label = ttk.Label(form_window, text="Updated Picture:")
            picture_label.pack()
            picture_path_label = ttk.Label(form_window, text="")
            picture_path_label.pack()

            def select_picture():
                file_path = filedialog.askopenfilename()
                picture_path_label.config(text=file_path)

            picture_button = ttk.Button(form_window, text="Select Picture", command=select_picture)
            picture_button.pack()

            def submit_form():
                drink_name = drink_name_entry.get()
                drink_type = drink_type_entry.get()
                drink_price = float(drink_price_entry.get())
                picture_path = picture_path_label.cget("text")

                # Retrieve the drink object from the database
                try:
                    drink = Drink.objects.get(id=item_id)
                except DoesNotExist:
                    messagebox.showerror("Error", f"Drink with ID {item_id} does not exist.")
                    return

                # Update the drink object with the new values
                drink.name = drink_name
                drink.type = drink_type
                drink.price = drink_price

                if picture_path:
                    # If a new picture is selected, update the picture field
                    with open(picture_path, "rb") as f:
                        picture_data = f.read()
                    picture = Picture(name=drink_name, picture=picture_data)
                    picture.save()
                    drink.picture = [picture]

                # Save the updated drink object
                drink.save()

                form_window.destroy()

            submit_button = ttk.Button(form_window, text="Submit", command=submit_form)
            submit_button.pack()

        elif obj_class == Meal:
            form_window = tk.Toplevel()
            form_window.title("Update Meal")
            form_window.minsize(480, -1)
            meal_name_label = ttk.Label(form_window, text="Updated Meal Name:")
            meal_name_label.pack()
            meal_name_entry = ttk.Entry(form_window)
            meal_name_entry.pack()
            meal_price_label = ttk.Label(form_window, text="Updated Meal Price:")
            meal_price_label.pack()
            meal_price_entry = ttk.Entry(form_window)
            meal_price_entry.pack()
            picture_label = ttk.Label(form_window, text="Updated Picture:")
            picture_label.pack()
            picture_path_label = ttk.Label(form_window, text="")
            picture_path_label.pack()

            def select_picture():
                file_path = filedialog.askopenfilename()
                picture_path_label.config(text=file_path)

            picture_button = ttk.Button(form_window, text="Select Picture", command=select_picture)
            picture_button.pack()

            def submit_form():
                meal_name = meal_name_entry.get()
                meal_price = float(meal_price_entry.get())
                picture_path = picture_path_label.cget("text")

                # Retrieve the meal object from the database
                try:
                    meal = Meal.objects.get(id=item_id)
                except DoesNotExist:
                    messagebox.showerror("Error", f"Meal with ID {item_id} does not exist.")
                    return

                # Update the meal object with the new values
                meal.name = meal_name
                meal.price = meal_price

                if picture_path:
                    # If a new picture is selected, update the picture field
                    with open(picture_path, "rb") as f:
                        picture_data = f.read()
                    picture = Picture(name=meal_name, picture=picture_data)
                    picture.save()
                    meal.picture = [picture]

                # Save the updated meal object
                meal.save()

                form_window.destroy()

            submit_button = ttk.Button(form_window, text="Submit", command=submit_form)
            submit_button.pack()

        elif obj_class == Order:
            form_window = tk.Toplevel()
            form_window.title("Update Order")
            form_window.minsize(480, -1)
            status_label = ttk.Label(form_window, text="Updated Status:")
            status_label.pack()
            status_entry = ttk.Entry(form_window)
            status_entry.pack()

            def submit_form():
                status = status_entry.get()

                # Retrieve the order object from the database
                try:
                    order = Order.objects.get(id=item_id)
                except DoesNotExist:
                    messagebox.showerror("Error", f"Order with ID {item_id} does not exist.")
                    return

                # Update the order object with the new status
                order.status = status

                # Save the updated order object
                order.save()

                form_window.destroy()

            submit_button = ttk.Button(form_window, text="Submit", command=submit_form)
            submit_button.pack()

        elif obj_class == Delivery:
            form_window = tk.Toplevel()
            form_window.title("Update Delivery")
            form_window.minsize(480, -1)
            name_label = ttk.Label(form_window, text="Updated Delivery Name:")
            name_label.pack()
            name_entry = ttk.Entry(form_window)
            name_entry.pack()
            company_label = ttk.Label(form_window, text="Updated Company:")
            company_label.pack()
            company_entry = ttk.Entry(form_window)
            company_entry.pack()

            def submit_form():
                name = name_entry.get()
                company = company_entry.get()

                # Retrieve the delivery object from the database
                try:
                    delivery = Delivery.objects.get(id=item_id)
                except DoesNotExist:
                    messagebox.showerror("Error", f"Delivery with ID {item_id} does not exist.")
                    return

                # Update the delivery object with the new values
                delivery.name = name
                delivery.company = company

                # Save the updated delivery object
                delivery.save()

                form_window.destroy()

            submit_button = ttk.Button(form_window, text="Submit", command=submit_form)
            submit_button.pack()

    def delete_object(self, treeview, obj_class):
        selected_item = treeview.focus()
        values = treeview.item(selected_item)["values"]
        item_id = values[0]  # Assuming ID column is the first column

        if obj_class == Drink:
            confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete this drink?")
            if confirm:
                try:
                    drink = Drink.objects.get(id=item_id)
                    drink.delete()
                except DoesNotExist:
                    messagebox.showerror("Error", f"Drink with ID {item_id} does not exist.")

        elif obj_class == Meal:
            confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete this meal?")
            if confirm:
                try:
                    meal = Meal.objects.get(id=item_id)
                    meal.delete()
                except DoesNotExist:
                    messagebox.showerror("Error", f"Meal with ID {item_id} does not exist.")

        elif obj_class == Order:
            confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete this order?")
            if confirm:
                try:
                    order = Order.objects.get(id=item_id)
                    order.delete()
                except DoesNotExist:
                    messagebox.showerror("Error", f"Order with ID {item_id} does not exist.")

        elif obj_class == Delivery:
            confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete this delivery?")
            if confirm:
                try:
                    delivery = Delivery.objects.get(id=item_id)
                    delivery.delete()
                except DoesNotExist:
                    messagebox.showerror("Error", f"Delivery with ID {item_id} does not exist.")

        # Refresh the treeview to reflect the changes
        treeview.delete(*treeview.get_children())

        # Retrieve the updated data from the database
        data = obj_class.objects()

        # Populate the treeview with the updated data
        for item in data:
            if obj_class == Drink:
                picture_names = [p.name for p in item.picture] if item.picture else []
                picture_name = ", ".join(picture_names)
                treeview.insert("", tk.END, text="", values=(item.id, item.name, item.type, item.price, picture_name))
            elif obj_class == Meal:
                picture_names = [p.name for p in item.picture] if item.picture else []
                picture_name = ", ".join(picture_names)
                treeview.insert("", tk.END, text="", values=(item.id, item.name, item.type, item.price, picture_name))
            elif obj_class == Order:
                client_name = item.client.name if item.client else ""
                treeview.insert("", tk.END, text="",
                                values=(item.id, client_name, item.dateOfOrder, item.dateOfDelivery, item.status))
            elif obj_class == Delivery:
                treeview.insert("", tk.END, text="", values=(item.id, item.name, item.company))

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    db = Database()
    app = WindowClient()
    app.run()
