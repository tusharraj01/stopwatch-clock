import tkinter as tk
import time

class StopwatchClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch / Clock")
        self.root.geometry("400x300")
        
        # Variables for stopwatch
        self.running = False
        self.start_time = None
        self.elapsed_time = 0

        # Label for Stopwatch Time
        self.stopwatch_label = tk.Label(self.root, text="00:00:00.000", font=("Helvetica", 30))
        self.stopwatch_label.pack(pady=20)

        # Buttons for stopwatch control
        self.start_button = tk.Button(self.root, text="Start", font=("Helvetica", 12), command=self.start_stopwatch)
        self.start_button.pack(side=tk.LEFT, padx=20, pady=10)
        
        self.stop_button = tk.Button(self.root, text="Stop", font=("Helvetica", 12), command=self.stop_stopwatch)
        self.stop_button.pack(side=tk.LEFT, padx=20, pady=10)
        
        self.reset_button = tk.Button(self.root, text="Reset", font=("Helvetica", 12), command=self.reset_stopwatch)
        self.reset_button.pack(side=tk.LEFT, padx=20, pady=10)

        # Label for Current Time
        self.clock_label = tk.Label(self.root, text="Current Time", font=("Helvetica", 14))
        self.clock_label.pack(pady=10)
        
        self.time_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.time_label.pack(pady=5)
        
        # Start the clock update loop
        self.update_clock()

    def start_stopwatch(self):
        """Starts or pauses the stopwatch"""
        if not self.running:
            if self.start_time is None:  # If we haven't started yet
                self.start_time = time.time() - self.elapsed_time
            else:
                self.start_time = time.time() - self.elapsed_time  # Continue from the elapsed time
            self.running = True
            self.start_button.config(text="Pause")  # Change button text to "Pause"
            self.update_stopwatch()
        else:
            self.elapsed_time = time.time() - self.start_time  # Pause the stopwatch and store elapsed time
            self.running = False
            self.start_button.config(text="Start")  # Change button text to "Start"

    def stop_stopwatch(self):
        """Stops the stopwatch without resetting"""
        self.running = False
        self.elapsed_time = time.time() - self.start_time
        self.start_button.config(text="Start")  # Change button text to "Start"

    def reset_stopwatch(self):
        """Resets the stopwatch to 00:00:00.000"""
        self.elapsed_time = 0
        self.start_time = None
        self.running = False
        self.stopwatch_label.config(text="00:00:00.000")
        self.start_button.config(text="Start")  # Ensure button is "Start" after reset
        
    def update_stopwatch(self):
        """Updates the stopwatch display every millisecond"""
        if self.running:
            elapsed = time.time() - self.start_time
            hours = int(elapsed // 3600)
            minutes = int((elapsed % 3600) // 60)
            seconds = int(elapsed % 60)
            milliseconds = int((elapsed % 1) * 1000)  # Get milliseconds by multiplying the fractional part by 1000
            self.stopwatch_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}")
            self.root.after(10, self.update_stopwatch)  # Update every 10 milliseconds

    def update_clock(self):
        """Updates the current time display every second"""
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_clock)  # Update every second

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchClockApp(root)
    root.mainloop()
