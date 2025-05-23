import customtkinter
from Content.MenuContent import MenuContent
from Content.OrderSection import OrderSection

class MainContent(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="#F0F3F5", corner_radius=15, **kwargs)
        
        # Configure grid
        self.grid_columnconfigure(0, weight=3)  # Menu section
        self.grid_columnconfigure(1, weight=2)  # Order section
        self.grid_rowconfigure(0, weight=1)
        
        # Create menu section (left side)
        self.menu_section = MenuContent(self)
        self.menu_section.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # Create order section (right side)
        self.order_section = OrderSection(self)
        self.order_section.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
