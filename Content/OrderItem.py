import customtkinter
from Content.OrderSummary import OrderSummary

class OrderItem(customtkinter.CTkFrame):
    def __init__(self, master, item_data, **kwargs):
        super().__init__(master, fg_color="transparent", height=60, **kwargs)
        
        # Quantity
        self.qty_label = customtkinter.CTkLabel(self, text=item_data["quantity"], 
                                    font=customtkinter.CTkFont(size=12, weight="bold"),
                                    width=20)
        self.qty_label.pack(side="left", padx=(0, 5))
        
        # Product info
        self.info_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.info_frame.pack(side="left", fill="both", expand=True, padx=5)
        
        self.name_label = customtkinter.CTkLabel(self.info_frame, text=item_data["name"], 
                                     font=customtkinter.CTkFont(size=12),
                                     justify="left", anchor="w")
        self.name_label.pack(anchor="w")
        
        # Price
        self.price_label = customtkinter.CTkLabel(self, text=item_data["price"], 
                                      font=customtkinter.CTkFont(size=12, weight="bold"))
        self.price_label.pack(side="right", padx=5)
