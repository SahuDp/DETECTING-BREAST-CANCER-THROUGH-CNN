import customtkinter as ctk
from tkinter import PhotoImage

class ConclusionPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.canvas = ctk.CTkCanvas(self, width=screen_width, height=screen_height)
        self.canvas.pack(fill="both", expand=True)

        self.background_image = PhotoImage(file=r"images\image3.png")
        self.canvas.create_image(screen_width / 2, screen_height / 2, image=self.background_image)

        back_button = ctk.CTkButton(self, text="Back to Menu", command=lambda: controller.show_frame("MenuPage"))
        back_button.place(relx=0.5, rely=0.9, anchor="center")
