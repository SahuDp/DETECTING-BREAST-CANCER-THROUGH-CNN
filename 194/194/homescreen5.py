import tkinter as tk
from tkinter import PhotoImage, Button
import subprocess 
import os

class SplashScreen(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Splash Screen")
        self.attributes("-fullscreen", True)  # Maximize the splash screen
        self.configure(background="black")  # Set background color

        # Load and display background image for splash screen
        splash_image = PhotoImage(file="images project ui/mainpage.png")
        splash_label = tk.Label(self, image=splash_image, bg="black")
        splash_label.image = splash_image
        splash_label.pack(fill="both", expand=True)

        # Create "Proceed" button
        proceed_button = Button(self, text="Proceed", command=self.close_splash, bg="white", fg="black", font=("Helvetica", 16))
        proceed_button.pack(side="bottom", pady=20)

    def close_splash(self):
        self.destroy()  # Close the splash screen

class MultiScreenApp(tk.Tk):
    def launch_second_app(self):
        # python_executable = os.path.join(os.environ["PYTHON"], "python.exe")
        subprocess.Popen(["python", "app.py"])

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Multi-Screen App")

        # Hide the main window temporarily during splash screen display
        self.withdraw()

        # Create splash screen instance
        self.splash = SplashScreen(self)
        self.wait_window(self.splash)  # Wait for splash screen to be closed

        # Show the main window after splash screen is closed
        self.deiconify()

        # Container to hold all screens
        self.container = tk.Frame(self)
        self.attributes("-fullscreen", True)  # Maximize the splash screen

        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Dictionary to store different screens
        self.frames = {}

        # List of background image filenames for each screen
        self.background_images = [
            "images project ui/mainpage.png",
            "images project ui/about.png",
            "images project ui/abstract.png",
            "images project ui/conclusion.png",
            "images project ui/apschelogo.png"
        ]

        # Create instances of each screen
        for i in range(5):
            frame = ScreenFrame(self.container, self.background_images[i], self)
            self.frames[f"Screen{i+1}"] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the home screen initially
        self.show_frame("Screen1")

    def show_frame(self, page_name):
        # Show a frame corresponding to the given page name
        frame = self.frames[page_name]
        frame.tkraise()

class ScreenFrame(tk.Frame):
    def __init__(self, parent, background_image, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Load background image
        img = PhotoImage(file=background_image)
        self.background_label = tk.Label(self, image=img)
        self.background_label.image = img
        self.background_label.pack(fill="both", expand=True)

        # Create a button to navigate back to the home screen
        back_button = Button(self, text="Back to Home", command=lambda: controller.show_frame("Screen1"), bg="white", fg="black", font=("Helvetica", 12))
        back_button.pack(side="bottom", padx=10, pady=10)

        # Add buttons for navigation based on the screen
        if parent.winfo_children()[0] == self:  # Check if this is the home screen
            # Buttons to navigate to other screens
            button1 = Button(self, text="Go to About", command=lambda: controller.show_frame("Screen2"), bg="white", fg="black", font=("Helvetica", 12))
            button1.pack(side="left", padx=100, pady=10)

            button2 = Button(self, text="Go to Abstract", command=lambda: controller.show_frame("Screen3"), bg="white", fg="black", font=("Helvetica", 12))
            button2.pack(side="left", padx=100, pady=10)

            button3 = Button(self, text="Go to Predictions", command=lambda: controller.launch_second_app(), bg="white", fg="black", font=("Helvetica", 12))
            button3.pack(side="left", padx=100, pady=10)

            button4 = Button(self, text="Go to Conclusion", command=lambda: controller.show_frame("Screen4"), bg="white", fg="black", font=("Helvetica", 12))
            button4.pack(side="left", padx=100, pady=10)
        else:
            # Additional functionality for other screens
            pass

if __name__ == "__main__":
    app = MultiScreenApp()
    app.geometry("1200x800")  # Set window size
    app.mainloop()
