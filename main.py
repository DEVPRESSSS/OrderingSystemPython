import customtkinter
from PIL import Image, ImageTk
import os
from pathlib import Path
from Content.CategorySelector import CategorySelector
from Content.SearchBar import SearchBar
from Content.UserTabs import UserTabs
from Content.MenuContent import MenuContent
from Content.Sidebar import SideBar
from Content.MenuItemCard import MenuItemCard


# Order section component (right side of main content)
class OrderSection(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="white", corner_radius=15, **kwargs)
        
        # Configure grid
        self.grid_rowconfigure(2, weight=1)  # Order items list
        self.grid_columnconfigure(0, weight=1)
        
        # Table header
        self.create_table_header()
        
        # Order type tabs
        self.create_order_tabs()
        
        # Order items list
        self.create_order_items_list()
        
        # Order summary
        self.order_summary = OrderSummary(self)
        self.order_summary.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        
        # Payment methods
        self.payment_methods = PaymentMethods(self)
        self.payment_methods.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
        
        # Place order button
        self.order_btn = customtkinter.CTkButton(self, text="Place Order", 
                                     fg_color="#00B67A", text_color="white",
                                     corner_radius=5, height=40,
                                     font=customtkinter.CTkFont(size=14, weight="bold"))
        self.order_btn.grid(row=5, column=0, padx=20, pady=10, sticky="ew")
        
    def create_table_header(self):
        table_frame = customtkinter.CTkFrame(self, fg_color="transparent", height=50)
        table_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        table_label = customtkinter.CTkLabel(table_frame, text="Table 4", 
                                  font=customtkinter.CTkFont(size=18, weight="bold"))
        table_label.pack(side="left")
        
        time_label = customtkinter.CTkLabel(table_frame, text="Start time", text_color="gray",
                                 font=customtkinter.CTkFont(size=12))
        time_label.pack(side="left", padx=10)
        
        edit_btn = customtkinter.CTkButton(table_frame, text="✎", fg_color="transparent", 
                                text_color="gray", width=20, height=20)
        edit_btn.pack(side="right")
        
    def create_order_tabs(self):
        tabs_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        tabs_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        
        tabs = ["Dine In", "Take Away", "Delivery"]
        for i, tab in enumerate(tabs):
            tab_btn = customtkinter.CTkButton(tabs_frame, text=tab, fg_color="transparent", 
                                   text_color="black" if i == 0 else "gray",
                                   hover_color="#F0F0F0", border_width=0)
            tab_btn.pack(side="left", padx=10)
            
            # Add indicator for active tab
            if i == 0:
                indicator = customtkinter.CTkFrame(tabs_frame, fg_color="#00B67A", height=3, width=60)
                indicator.place(x=10, y=30)
                
    def create_order_items_list(self):
        order_items_frame = customtkinter.CTkScrollableFrame(self, fg_color="transparent")
        order_items_frame.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
        
        # Order items
        order_items = [
            {
                "name": "Original Chees Meat Burger With\nChips (Bien Vegi)",
                "price": "$23.99",
                "quantity": "1x"
            },
            {
                "name": "Fresh Orange Juice With Basil\nSugar (Vegi)",
                "price": "$12.99",
                "quantity": "1x"
            },
            {
                "name": "Meat Sushi Roll With Tuna, Shrimp\nAnd Crab (Non-Vegi)",
                "price": "$9.99",
                "quantity": "1x"
            },
            {
                "name": "Tacos Salsa With Chickens\nGrilled",
                "price": "$16.99",
                "quantity": "1x"
            }
        ]
        
        for item in order_items:
            order_item = OrderItem(order_items_frame, item)
            order_item.pack(fill="x", pady=5)












# Order item component
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


# Order summary component  
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


# Payment methods component
class PaymentMethods(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        
        # Payment methods
        self.methods = ["Cash", "Credit/Debit Card", "Gift Card"]
        
        for method in self.methods:
            method_btn = customtkinter.CTkButton(self, text=method, 
                                      fg_color="#F0F0F0", text_color="black",
                                      hover_color="#E0E0E0", corner_radius=5)
            method_btn.pack(side="left", padx=5, expand=True, fill="x")


# Main content frame containing menu and order sections
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



# Main Application Class
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # Set appearance mode and color theme
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("green")
        
        # Set window size and color
        self.geometry("1000x700")
        self.configure(fg_color="white")
        
        # Configure grid
        self.grid_columnconfigure(0, weight=0)  
        self.grid_columnconfigure(1, weight=1)          
        self.grid_rowconfigure(0, weight=1)
        
        # Center the window on the screen
        self.center_window()
        
        # Title of the window
        self.title("Welcome to Jane Abustan Ordering  System")
        
        # Create a sidebar with fixed width
        self.sidebar = SideBar(
            master=self,
            width=200,  
            corner_radius=8 ,
            fg_color="#ffffff",
            border_color="#DDDDDD",
            border_width=1
        )
        self.sidebar.grid(row=0,
                          column=0,            
                          sticky="nsew",
                          padx=6, 
                          pady=6 )  
        
        # Create a main content area that expands to fill the remaining space
        self.main_content = MainContent(self,
                                        border_color="#DDDDDD",
                                        border_width=1)
        self.main_content.grid(row=0, 
                               column=1, 
                               sticky="nsew", 
                               padx=6, 
                               pady=6)
        
    
            
    # Center the window on the screen
    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        window_width = 1000
        window_height = 700
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")


if __name__ == "__main__":
    app = App()
    app.mainloop()