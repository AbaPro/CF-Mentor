import tkinter as tk
import time

class StopWatch(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.start_time = None

    def create_widgets(self):
        self.time_label = tk.Label(self, text="00:00:00", font=("Helvetica", 30))
        self.time_label.pack(pady=20)
        self.start_button = tk.Button(self, text="Start", command=self.start_timer, font=("Helvetica", 16))
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.stop_button = tk.Button(self, text="Stop", command=self.stop_timer, font=("Helvetica", 16))
        self.stop_button.pack(side=tk.LEFT, padx=10)
        self.reset_button = tk.Button(self, text="Reset", command=self.reset_timer, font=("Helvetica", 16))
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def start_timer(self):
        self.start_time = time.time()
        self.update_timer()

    def stop_timer(self):
        self.after_cancel(self.timer)
        self.start_time = None

    def reset_timer(self):
        self.stop_timer()
        self.time_label.config(text="00:00:00")

    def update_timer(self):
        if self.start_time is not None:
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            hours = int(elapsed_time / 3600)
            minutes = int((elapsed_time - hours*3600) / 60)
            seconds = int(elapsed_time - hours*3600 - minutes*60)
            time_string = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
            self.time_label.config(text=time_string)
        self.timer = self.after(1000, self.update_timer)

root = tk.Tk()
root.title("Stopwatch")
root.geometry("300x150")
stopwatch = StopWatch(root)
stopwatch.pack()
root.mainloop()