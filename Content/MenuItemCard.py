import customtkinter
from PIL import Image, ImageTk


# Menu item card component
class MenuItemCard(customtkinter.CTkFrame):
    def __init__(self, master, item_data, **kwargs):
        super().__init__(master, fg_color="white", corner_radius=10, **kwargs)
        
        self.item_data = item_data
        
        self.img_label = customtkinter.CTkLabel(self, text="Food Image", fg_color="#F0F0F0", 
                                    width=150, height=100)
        self.img_label.pack(pady=(10, 5))
        
        try:
            if "image_path" in item_data:
                img = customtkinter.CTkImage(Image.open(item_data["image_path"]), size=(150, 100))
                self.img_label.configure(image=img, text="")
        except:
            pass
        
        # Food info
        self.info_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.info_frame.pack(fill="x", padx=10, pady=5, anchor="w")
        
        self.name_label = customtkinter.CTkLabel(self.info_frame, text=item_data["name"], 
                                     font=customtkinter.CTkFont(size=12, weight="bold"),
                                     justify="left", anchor="w")
        self.name_label.pack(anchor="w")
        
        # Price and calories
        self.price_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.price_frame.pack(fill="x", padx=10, pady=5)
        
        self.price_label = customtkinter.CTkLabel(self.price_frame, text=item_data["price"], 
                                      font=customtkinter.CTkFont(size=14, weight="bold"),
                                      anchor="w")
        self.price_label.pack(side="left")
        
        self.calories = customtkinter.CTkLabel(self.price_frame, text=item_data.get("calories", "400 kcal"), 
                                   font=customtkinter.CTkFont(size=10),
                                   text_color="gray", anchor="e")
        self.calories.pack(side="right")
        
        # Add to cart button or quantity selector
        self.create_action_button()
        
    def create_action_button(self):
        # If this is the burger item with quantity selector
        if self.item_data.get("has_quantity_selector", False):
            quantity_frame = customtkinter.CTkFrame(self, fg_color="transparent")
            quantity_frame.pack(fill="x", padx=10, pady=10)
            
            minus_btn = customtkinter.CTkButton(quantity_frame, text="-", fg_color="#F0F0F0", 
                                     text_color="black", width=30, height=30,
                                     corner_radius=15)
            minus_btn.pack(side="left")
            
            qty_label = customtkinter.CTkLabel(quantity_frame, text="1", width=30)
            qty_label.pack(side="left", padx=10)
            
            plus_btn = customtkinter.CTkButton(quantity_frame, text="+", fg_color="#00B67A", 
                                    text_color="white", width=30, height=30,
                                    corner_radius=15)
            plus_btn.pack(side="left")
        else:
            add_btn = customtkinter.CTkButton(self, text="Add to Cart", fg_color="#F0F0F0", 
                                  text_color="black", corner_radius=5,
                                  hover_color="#E0E0E0")
            add_btn.pack(fill="x", padx=10, pady=10)
