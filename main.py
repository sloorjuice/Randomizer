import random, time
import tkinter as tk

class Main:
    def __init__(self) -> None:
        # Creating the window.
        # Setting the Title and Size.
        self.window = tk.Tk()
        self.windowTitle = self.window.title("Randomizer")
        self.window.geometry("600x400")
        
        # Setting Variables for the listed items and Text Field Variable.
        self.item_labels = []
        self.is_listed = False
        self.text_var=tk.StringVar()
        
        # Loading all the items in the external file and saves them in a variable.
        self.item_list = self.load_items()
        
        # Creating Buttons.
        self.add_button = tk.Button(self.window, text='Add', width=19, command=self.add_item).grid(row=0, column=1)
        self.remove_button = tk.Button(self.window, text='Remove', width=19, command=self.remove_item).grid(row=0, column=2)
        self.list_button = tk.Button(self.window, text='List', width=19, command=self.list_items).grid(row=1, column=0)
        self.rand_button = tk.Button(self.window, text='Randomize', width=19, command=self.random_button).grid(row=1, column=1)
        self.quit_button = tk.Button(self.window, text='Quit', width=19, command=(quit)).grid(row=0, column=4)
        
        # Creating Text Field.
        text_entry = tk.Entry(self.window,textvariable = self.text_var, font=('calibre',10,'normal'))
        text_entry.grid(row=0,column=0)
        
        # Selecting a random item if items available.
        if self.item_list: random_item = random.choice(self.item_list) 
        else: random_item = "No items available"
        
        # Create the label for the random item.
        self.random_label = tk.Label(self.window, text=f"Random item: {random_item}")
        self.random_label.grid(column=2, row=1)
        
        tk.mainloop()
        
    def add_item(self):
        """Code for the add button"""
        # Gets text in the text field and saves it to the external file
        item=self.text_var.get()
        self.text_var.set("") # Clearing the text field
        self.item_list.append(item)
        self.save_item() 
    
    def list_items(self): 
        """Code for the list button"""
        # Checks if items are already listed.
        if not self.is_listed: 
            column_width = 8  # Number of items that are displayed per column .
            for index, item in enumerate(self.item_list): # Loops through all the items in the list
                # Sets the correct spot in the column and row.
                starting_row = 4
                column_index = index // column_width 
                row_index = index % column_width + starting_row
                
                # Creates the labels for the items.
                label = tk.Label(self.window, text=f"{item}")
                label.grid(column=column_index, row=row_index)
                self.item_labels.append(label) # Adds them to a list of labels.
            self.is_listed = True
        else:
            for item in self.item_labels:
                item.destroy() # Destroys the labels if they're already displayed.
            self.is_listed = False
        
    
    def remove_item(self):
        """Code for the remove button"""
        #Removes the item in the text field from the list of items
        self.remove_selected_item(self.text_var.get())
        self.text_var.set("")
        
        
        
    def random_button(self):
        """Code for the random button"""
        # Removes the previously generated random item
        self.random_label.destroy() 
        
        # Selecting a random item if items available.
        if self.item_list: random_item = random.choice(self.item_list) 
        else: random_item = "No items available"
        
        # Create the label for the random item.
        self.random_label = tk.Label(self.window, text=f"Random Brainrot: {random_item}")
        self.random_label.grid(column=2, row=1)

    def save_item(self):
        """Saves any new items in the list"""
        with open("items.txt", "w") as file:
            for item in self.item_list:
                file.write(item + "\n")

    def remove_selected_item(self, item):
        """Removes a selected item from the external file"""
        if item in self.item_list:
            self.item_list.remove(item)
        self.save_item()

    def load_items(self):
        """Loads all items in the external file"""
        try:
            with open("items.txt", "r") as file:
                return file.read().splitlines()
        except FileNotFoundError:
            return []

if __name__ == "__main__":
    main = Main()

