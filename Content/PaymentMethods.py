import customtkinter

class PaymentMethods(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        
        self.methods = ["Cash", "Credit/Debit Card", "Gift Card"]
        
        for method in self.methods:
            method_btn = customtkinter.CTkButton(self, text=method, 
                                      fg_color="#F0F0F0", text_color="black",
                                      hover_color="#E0E0E0", corner_radius=5)
            method_btn.pack(side="left", padx=5, expand=True, fill="x")