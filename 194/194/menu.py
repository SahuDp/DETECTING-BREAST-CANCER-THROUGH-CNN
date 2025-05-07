import customtkinter as ctk
from tkinter import PhotoImage

class MenuPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        #ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.canvas = ctk.CTkCanvas(self, width=screen_width, height=screen_height)
        self.canvas.pack(fill="both", expand=True)

        self.background_image = PhotoImage(file=r"images\image4.png")
        self.canvas.create_image(screen_width / 2, screen_height / 2, image=self.background_image)

        self.Home_button = ctk.CTkButton(self, text="Home", command=lambda: controller.show_frame("MainPage"), width=100, height=40)
        self.Home_button.place(relx=0.2, rely=0.52, anchor="center")
        
        self.Abstract_button = ctk.CTkButton(self, text="Abstract", command=lambda: controller.show_frame("AbstractPage"), width=100, height=40)
        self.Abstract_button.place(relx=0.4, rely=0.52, anchor="center")
        
        self.proceed_button = ctk.CTkButton(self, text="Detection",command=lambda: model(), width=100, height=40)
        self.proceed_button.place(relx=0.6, rely=0.52, anchor="center")

        self.Conclusion_button = ctk.CTkButton(self, text="Conclusion", command=lambda: controller.show_frame("ConclusionPage"), width=100, height=40)
        self.Conclusion_button.place(relx=0.8, rely=0.52, anchor="center")
        
        def model():
            import subprocess
            subprocess.Popen(["python", "app.py"])
            #import app
            # app.mode()
