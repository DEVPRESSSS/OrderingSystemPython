import customtkinter

# Category selector component  
class CategorySelector(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        
        self.categories = [
            ("All", "all"),
            ("Breakfast", "breakfast"),
            ("Soups", "soups"),
            ("Pasta", "pasta"),
            ("Main Course", "main_course"),
            ("Burger", "burger")
        ]
        
        for text, icon_name in self.categories:
            category_button = customtkinter.CTkButton(self, text=text, 
                                           fg_color="#F5F5F5", text_color="black",
                                           hover_color="#E0E0E0", corner_radius=15,
                                           width=100, height=70)
            category_button.pack(side="left", padx=5, pady=5)

