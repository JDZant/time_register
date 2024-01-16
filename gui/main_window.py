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

        # start time
        self.start_time = tk.StringVar(None, '08:30')

        # durations
        self.preparation_duration = tk.IntVar(None, 30)
        self.standup_duration = tk.IntVar(None, 30)
        self.time_registration_duration = tk.IntVar(None, 15)

        # labels
        self.start_time_label = tk.Label(self, text="Start time (H:M)")
        self.preparation_duration_label = tk.Label(self, text="Preparation duration (min)")
        self.standup_duration_label = tk.Label(self, text="Standup duration (min)")
        self.time_registration_duration_label = tk.Label(self, text="Time registration duration (min)")

        # inputs
        self.start_time_input = tk.Entry(self, textvariable=self.start_time)
        self.preparation_duration_input = tk.Entry(self, textvariable=self.preparation_duration)
        self.standup_duration_input = tk.Entry(self, textvariable=self.standup_duration)
        self.time_registration_duration_input = tk.Entry(self, textvariable=self.time_registration_duration)

        # buttons
        self.start_button = tk.Button(self, text="Start", command=self.start_process)

        # positioning
        self.start_time_label.grid(row=1, column=0, padx=10, pady=10)
        self.start_time_input.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

        self.preparation_duration_label.grid(row=2, column=0, padx=10, pady=10)
        self.preparation_duration_input.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

        self.standup_duration_label.grid(row=3, column=0, padx=10, pady=10)
        self.standup_duration_input.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

        self.time_registration_duration_label.grid(row=4, column=0, padx=10, pady=10)
        self.time_registration_duration_input.grid(row=4, column=1, padx=10, pady=10,
                                                   sticky='ew')

        # Place the start button on the same row as the last input, but in the next column
        self.start_button.grid(row=5, column=1, padx=10, pady=10, columnspan=2, sticky='ew')

    def start_process(self):
        user_config = {
            'start_time': self.start_time.get(),
            'preparation_duration': self.preparation_duration.get(),
            'standup_duration': self.standup_duration.get(),
            'time_registration_duration': self.time_registration_duration.get()
        }

        run_time_registration(user_config)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    app.grid()
    root.mainloop()
