import customtkinter


#Settings
class SettingsContent(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.main_label = customtkinter.CTkLabel(
            master=self,
            text="This is settings Area",
            font=("Arial", 20)
        )
        self.main_label.pack(expand=True)
