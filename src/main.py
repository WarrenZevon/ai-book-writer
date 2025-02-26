import sys
import tkinter as tk
from gui.main_window import MainWindow

def main():
    root = tk.Tk()
    root.title("AI Book Writing Assistant")
    root.geometry("1200x800")
    
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()