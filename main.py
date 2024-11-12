import random, time
import tkinter as tk

class Main:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.windowTitle = self.window.title("Randomizer")
        self.window.geometry("600x400")
        
        self.textVar=tk.StringVar()

        self.item_list = self.load_items()
        
        self.quitButton = tk.Button(self.window, text='Quit', width=19, command=(quit)).grid(row=0, column=0)
        
        Text_entry = tk.Entry(self.window,textvariable = self.textVar, font=('calibre',10,'normal'))
        Text_entry.grid(row=1,column=0)
        
        self.addButton = tk.Button(self.window, text='Add', width=19, command=self.addItem).grid(row=2, column=0)
        self.removeButton = tk.Button(self.window, text='Remove', width=19, command=self.removeItem).grid(row=3, column=0)
        self.listButton = tk.Button(self.window, text='List', width=19, command=self.listItems).grid(row=4, column=0)
        self.randButton = tk.Button(self.window, text='Randomize', width=19, command=self.randomButton).grid(row=5, column=0)
        
        self.Randomlabel = tk.Label(self.window, text=f"Random item: {random.choice(self.item_list)}")
        self.Randomlabel.grid(column=1, row=4)
        
        
        tk.mainloop()
        
    def addItem(self):
        Item=self.textVar.get()
        self.textVar.set("")
        self.item_list.append(Item)
        self.save_item()
    
    def listItems(self): 
        for index, item in enumerate(self.item_list):
            label = tk.Label(self.window, text=f"{item}")
            label.grid(column=index % 5, row=4 + index // 5)
    
    def removeItem(self):
        """Removes the item in the text field from the list of items"""
        self.remove_item(self.textVar.get())
        self.textVar.set("")
        
    def randomButton(self):
        self.Randomlabel.destroy()
        self.Randomlabel = tk.Label(self.window, text=f"Random item: {random.choice(self.item_list)}")
        self.Randomlabel.grid(column=1, row=5)

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

