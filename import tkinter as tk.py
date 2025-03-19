import tkinter as tk
from tkinter import messagebox

class WristbandUI:
    def _init_(self, master):
        self.master = master
        master.title("AI-Powered Wristband")

        # Create frames
        self.data_frame = tk.Frame(master, bg="gray")
        self.data_frame.pack(fill="x")

        self.analysis_frame = tk.Frame(master, bg="gray")
        self.analysis_frame.pack(fill="x")

        self.button_frame = tk.Frame(master, bg="gray")
        self.button_frame.pack(fill="x")

        # Create labels and entries
        tk.Label(self.data_frame, text="Anxiety Level:").pack(side="left")
        self.anxiety_level_entry = tk.Entry(self.data_frame, width=10)
        self.anxiety_level_entry.pack(side="left")

        tk.Label(self.data_frame, text="Mood:").pack(side="left")
        self.mood_entry = tk.Entry(self.data_frame, width=10)
        self.mood_entry.pack(side="left")

        tk.Label(self.data_frame, text="Sleep Quality:").pack(side="left")
        self.sleep_quality_entry = tk.Entry(self.data_frame, width=10)
        self.sleep_quality_entry.pack(side="left")

        tk.Label(self.data_frame, text="Heart Rate:").pack(side="left")
        self.heart_rate_entry = tk.Entry(self.data_frame, width=10)
        self.heart_rate_entry.pack(side="left")

        tk.Label(self.data_frame, text="Blood Pressure:").pack(side="left")
        self.blood_pressure_entry = tk.Entry(self.data_frame, width=10)
        self.blood_pressure_entry.pack(side="left")

        # Create analysis label
        self.analysis_label = tk.Label(self.analysis_frame, text="", wraplength=400)
        self.analysis_label.pack(fill="x")

        # Create buttons
        self.update_button = tk.Button(self.button_frame, text="Update", command=self.update_data)
        self.update_button.pack(side="left")

        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.master.destroy)
        self.exit_button.pack(side="left")

    def update_data(self):
        # Get user input
        anxiety_level = int(self.anxiety_level_entry.get())
        mood = self.mood_entry.get()
        sleep_quality = int(self.sleep_quality_entry.get())
        heart_rate = int(self.heart_rate_entry.get())
        blood_pressure = int(self.blood_pressure_entry.get())

        # Analyze data using AI algorithm
        mental_health_status = self.analyze_data(anxiety_level, mood, sleep_quality, heart_rate, blood_pressure)

        # Display analysis result
        self.analysis_label.config(text=f"Mental Health Status: {mental_health_status}")

        # Display alert message if at risk
        if mental_health_status == "at risk":
            messagebox.showwarning("Alert", "You are at risk! Please take immediate action to reduce your anxiety level and improve your mood.")

        # Display precautions if safe
        elif mental_health_status == "stable":
            messagebox.showinfo("Precautions", "You are safe! To maintain your mental health, consider practicing relaxation techniques, such as deep breathing, meditation, or yoga. Also, make sure to get enough sleep and exercise regularly.")

    def analyze_data(self, anxiety_level, mood, sleep_quality, heart_rate, blood_pressure):
        # Simplified AI logic to determine mental health status
        if anxiety_level > 5 or mood == "sad" or sleep_quality < 5:
            return "at risk"
        elif heart_rate > 100 or blood_pressure > 140:
            return "alert"
        else:
            return "stable"

# Create the root window
root = tk.Tk()

# Create an instance of the WristbandUI class
my_gui = WristbandUI(root)

# Start the GUI event loop
root.mainloop()