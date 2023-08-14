import tkinter as tk
from tkinter_window import TkinterWindow
from data_display import DataDisplay
from ndax_component import NDAXComponent

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CCXT Data Display from NDAX")

        self.ndax_component = NDAXComponent()  # Initialize NDAX API component

        self.data_display = DataDisplay(self.root)  # Create a data display widget
        self.data_display.pack()

        self.tkinter_window = TkinterWindow(self.root)  # Create a Tkinter window widget
        self.tkinter_window.pack()

        self.update_data()  # Start updating data

    def update_data(self):
        # Fetch data from NDAXComponent
        ccxt_data = self.ndax_component.get_ccxt_data()

        # Update DataDisplay widget with the fetched data
        self.data_display.update_data(ccxt_data)

        # Schedule the next data update
        self.root.after(10000, self.update_data)  # Update data every 10 seconds

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
