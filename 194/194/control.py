import customtkinter as ctk
from main import MainPage
from abstract import AbstractPage
from menu import MenuPage
from conclusion import ConclusionPage


class AppController(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Application")
        self.geometry("1250x700")

        self.frames = {}
        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True)

        for F in (MainPage, AbstractPage, MenuPage , ConclusionPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.show_frame("MainPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = AppController()
    app.mainloop()
