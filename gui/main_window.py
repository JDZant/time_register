# main_window.py
import sys
import tkinter as tk

sys.path.append('/home/jos/projects/personal/time_register/')  # Add this line before your import

from app.main import run_time_registration


class MainWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Time Registration")

        self.start_time = tk.StringVar()

        self.start_time_label = tk.Label(self, text="Start time")
        self.start_time_label.grid(row=1, column=0, padx=10, pady=10)

        self.start_time_input = tk.Entry(self, textvariable=self.start_time)
        self.start_time_input.grid(row=1, column=1, padx=10, pady=10)

        self.start_button = tk.Button(self, text="Start time registration", command=self.start_process)
        self.start_button.grid(row=2, column=1, padx=10, pady=10)

    def start_process(self):
        start_time = self.start_time.get()
        run_time_registration(start_time)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    app.grid()
    root.mainloop()
