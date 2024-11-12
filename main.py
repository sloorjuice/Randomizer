import random, time
import tkinter as tk

class Main:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.windowTitle = self.window.title("Randomizer")
        self.window.geometry("600x400")
        self.itemLabels = []
        self.textVar=tk.StringVar()
        self.isListed = False

        self.item_list = self.load_items()
        
        self.quitButton = tk.Button(self.window, text='Quit', width=19, command=(quit)).grid(row=0, column=4)
        
        Text_entry = tk.Entry(self.window,textvariable = self.textVar, font=('calibre',10,'normal'))
        Text_entry.grid(row=0,column=0)
        
        self.addButton = tk.Button(self.window, text='Add', width=19, command=self.addItem).grid(row=0, column=1)
        self.removeButton = tk.Button(self.window, text='Remove', width=19, command=self.removeItem).grid(row=0, column=2)
        self.listButton = tk.Button(self.window, text='List', width=19, command=self.listItems).grid(row=1, column=0)
        self.randButton = tk.Button(self.window, text='Randomize', width=19, command=self.randomButton).grid(row=1, column=1)
        
        self.Randomlabel = tk.Label(self.window, text=f"Random item: {random.choice(self.item_list)}")
        self.Randomlabel.grid(column=2, row=1)
        
        
        tk.mainloop()
        
    def addItem(self):
        Item=self.textVar.get()
        self.textVar.set("")
        self.item_list.append(Item)
        self.save_item()
    
    def listItems(self): 
        if not self.isListed:
            column_width = 8  # Desired column width
            for index, item in enumerate(self.item_list):
                column_index = index // column_width
                row_index = index % column_width + 4  # Starting row is 5
                label = tk.Label(self.window, text=f"{item}")
                label.grid(column=column_index, row=row_index)
                self.itemLabels.append(label)
            self.isListed = True
        else:
            for item in self.itemLabels:
                item.destroy()
            self.isListed = False
        
    
    def removeItem(self):
        """Removes the item in the text field from the list of items"""
        self.remove_item(self.textVar.get())
        self.textVar.set("")
        
    def randomButton(self):
        self.Randomlabel.destroy()
        self.Randomlabel = tk.Label(self.window, text=f"Random item: {random.choice(self.item_list)}")
        self.Randomlabel.grid(column=2, row=1)

    def save_item(self):
        with open("items.txt", "w") as file:
            for item in self.item_list:
                file.write(item + "\n")

    def remove_item(self, item):
        if item in self.item_list:
            self.item_list.remove(item)
        self.save_item()

    def load_items(self):
        try:
            with open("items.txt", "r") as file:
                return file.read().splitlines()
        except FileNotFoundError:
            return []

if __name__ == "__main__":
    main = Main()

