import customtkinter    


class OrderSummary(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        
        # Subtotal
        self.subtotal_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.subtotal_frame.pack(fill="x", pady=2)
        
        self.subtotal_label = customtkinter.CTkLabel(self.subtotal_frame, text="Sub Total", 
                                         font=customtkinter.CTkFont(size=14))
        self.subtotal_label.pack(side="left")
        
        self.subtotal_value = customtkinter.CTkLabel(self.subtotal_frame, text="$63.96", 
                                         font=customtkinter.CTkFont(size=14))
        self.subtotal_value.pack(side="right")
        
        # Tax
        self.tax_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.tax_frame.pack(fill="x", pady=2)
        
        self.tax_label = customtkinter.CTkLabel(self.tax_frame, text="Tax 5%", 
                                   font=customtkinter.CTkFont(size=14))
        self.tax_label.pack(side="left")
        
        self.tax_value = customtkinter.CTkLabel(self.tax_frame, text="$3.75", 
                                    font=customtkinter.CTkFont(size=14))
        self.tax_value.pack(side="right")
        
        # Total
        self.total_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.total_frame.pack(fill="x", pady=5)
        
        self.total_label = customtkinter.CTkLabel(self.total_frame, text="Total Amount", 
                                      font=customtkinter.CTkFont(size=16, weight="bold"))
        self.total_label.pack(side="left")
        
        self.total_value = customtkinter.CTkLabel(self.total_frame, text="$67.71", 
                                      font=customtkinter.CTkFont(size=16, weight="bold"))
        self.total_value.pack(side="right")
