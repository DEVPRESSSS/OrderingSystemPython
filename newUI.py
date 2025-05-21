import customtkinter as ctk
from PIL import Image, ImageTk
import os
from pathlib import Path

# Sidebar component
class SideBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="#FFFFFF", corner_radius=0, border_width=1, 
                         border_color="#EEEEEE", **kwargs)
        
        # Configure grid
        self.grid_rowconfigure(10, weight=2) 
        
        # Logo and name
        self.create_logo_section()
        
        # Menu button
        self.menu_button = ctk.CTkButton(self, text="Menu", fg_color="#00B67A", corner_radius=5, 
                                    height=36, font=ctk.CTkFont(size=14, weight="bold"))
        
        self.menu_button.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        
        # Other sidebar buttons
        self.create_sidebar_buttons()
        
        # Logout button at the bottom
        self.create_logout_button()
        
    def create_logo_section(self):

        logo_frame = ctk.CTkFrame(self, fg_color="transparent")
        logo_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        
        name_label = ctk.CTkLabel(logo_frame, text="CIBU POS", font=ctk.CTkFont(size=16, weight="bold"))
        name_label.pack(side="left")

        
    def create_sidebar_buttons(self):

        sidebar_buttons = [
            ("Table Services", "table"),
            ("Reservation", "reservation"),
            ("Delivery", "delivery"),
            ("Accounting", "accounting"),
            ("Settings", "settings")
        ]
        
        for i, (text, icon_name) in enumerate(sidebar_buttons):
            button_frame = ctk.CTkFrame(self, fg_color="transparent")
            button_frame.grid(row=i+2, column=0, padx=20, pady=5, sticky="ew")
            
            # Icon placeholder
            icon_label = ctk.CTkLabel(button_frame, text="", width=24, height=24)
            icon_label.pack(side="left", padx=(0, 10))
            
            # Button text
            text_label = ctk.CTkLabel(button_frame, text=text, anchor="w", 
                                     font=ctk.CTkFont(size=14))
            text_label.pack(side="left", fill="x", expand=True)

            



    def create_logout_button(self):
        logout_frame = ctk.CTkFrame(self, fg_color="transparent")
        logout_frame.grid(row=10, column=0, padx=20, pady=20, sticky="ew")
        
        logout_icon = ctk.CTkLabel(logout_frame, text="", width=24, height=24)
        logout_icon.pack(side="left", padx=(0, 10))
        
        logout_label = ctk.CTkLabel(logout_frame, text="Logout", anchor="w", 
                                   font=ctk.CTkFont(size=14))
        logout_label.pack(side="left", fill="x", expand=True)



# Search and filter bar component
class SearchBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        
        # Menu icon
        self.menu_icon = ctk.CTkLabel(self, text="≡", font=ctk.CTkFont(size=20))
        self.menu_icon.pack(side="left", padx=(0, 10))
        
        # Search entry
        self.search_var = ctk.StringVar()
        self.search_entry = ctk.CTkEntry(self, placeholder_text="Search Product here...", width=300,
                                   fg_color="#F5F5F5", border_color="#E0E0E0")
        self.search_entry.pack(side="left", padx=10)
        
        # Filter icon
        self.filter_icon = ctk.CTkLabel(self, text="☰", font=ctk.CTkFont(size=20))
        self.filter_icon.pack(side="left", padx=10)


# Category selector component  
class CategorySelector(ctk.CTkFrame):
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
            category_button = ctk.CTkButton(self, text=text, 
                                           fg_color="#F5F5F5", text_color="black",
                                           hover_color="#E0E0E0", corner_radius=15,
                                           width=100, height=70)
            category_button.pack(side="left", padx=5, pady=5)



# Menu item card component
class MenuItemCard(ctk.CTkFrame):
    def __init__(self, master, item_data, **kwargs):
        super().__init__(master, fg_color="white", corner_radius=10, **kwargs)
        
        self.item_data = item_data
        
        self.img_label = ctk.CTkLabel(self, text="Food Image", fg_color="#F0F0F0", 
                                    width=150, height=100)
        self.img_label.pack(pady=(10, 5))
        
        try:
            if "image_path" in item_data:
                img = ctk.CTkImage(Image.open(item_data["image_path"]), size=(150, 100))
                self.img_label.configure(image=img, text="")
        except:
            pass
        
        # Food info
        self.info_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.info_frame.pack(fill="x", padx=10, pady=5, anchor="w")
        
        self.name_label = ctk.CTkLabel(self.info_frame, text=item_data["name"], 
                                     font=ctk.CTkFont(size=12, weight="bold"),
                                     justify="left", anchor="w")
        self.name_label.pack(anchor="w")
        
        # Price and calories
        self.price_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.price_frame.pack(fill="x", padx=10, pady=5)
        
        self.price_label = ctk.CTkLabel(self.price_frame, text=item_data["price"], 
                                      font=ctk.CTkFont(size=14, weight="bold"),
                                      anchor="w")
        self.price_label.pack(side="left")
        
        self.calories = ctk.CTkLabel(self.price_frame, text=item_data.get("calories", "400 kcal"), 
                                   font=ctk.CTkFont(size=10),
                                   text_color="gray", anchor="e")
        self.calories.pack(side="right")
        
        # Add to cart button or quantity selector
        self.create_action_button()
        
    def create_action_button(self):
        # If this is the burger item with quantity selector
        if self.item_data.get("has_quantity_selector", False):
            quantity_frame = ctk.CTkFrame(self, fg_color="transparent")
            quantity_frame.pack(fill="x", padx=10, pady=10)
            
            minus_btn = ctk.CTkButton(quantity_frame, text="-", fg_color="#F0F0F0", 
                                     text_color="black", width=30, height=30,
                                     corner_radius=15)
            minus_btn.pack(side="left")
            
            qty_label = ctk.CTkLabel(quantity_frame, text="1", width=30)
            qty_label.pack(side="left", padx=10)
            
            plus_btn = ctk.CTkButton(quantity_frame, text="+", fg_color="#00B67A", 
                                    text_color="white", width=30, height=30,
                                    corner_radius=15)
            plus_btn.pack(side="left")
        else:
            add_btn = ctk.CTkButton(self, text="Add to Cart", fg_color="#F0F0F0", 
                                  text_color="black", corner_radius=5,
                                  hover_color="#E0E0E0")
            add_btn.pack(fill="x", padx=10, pady=10)


# User tabs component
class UserTabs(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        
        self.users = [
            {"initial": "T1", "name": "Jacob Jones", "role": "Waiter - Section 2"},
            {"initial": "T2", "name": "Esther Howard", "role": "Cashier - Kitchen"},
            {"initial": "T3", "name": "Robert Fox", "role": "Barman - Kitchen"}
        ]
        
        for user in self.users:
            self.create_user_tab(user)
            
    def create_user_tab(self, user):
        user_tab = ctk.CTkFrame(self, fg_color="#F9F9F9", corner_radius=5)
        user_tab.pack(side="left", padx=10, pady=5)
        
        initial = ctk.CTkLabel(user_tab, text=user["initial"], 
                              fg_color="#FFD700", text_color="black",
                              width=30, height=30, corner_radius=15)
        initial.pack(side="left", padx=10, pady=10)
        
        user_info = ctk.CTkFrame(user_tab, fg_color="transparent")
        user_info.pack(side="left", padx=5, pady=10)
        
        name_label = ctk.CTkLabel(user_info, text=user["name"], 
                                 font=ctk.CTkFont(size=12, weight="bold"),
                                 anchor="w")
        name_label.pack(anchor="w")
        
        role_label = ctk.CTkLabel(user_info, text=user["role"], 
                                 font=ctk.CTkFont(size=10),
                                 text_color="gray", anchor="w")
        role_label.pack(anchor="w")


# Menu section component (left side of main content)
class MenuSection(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        
        # Search bar
        self.search_bar = SearchBar(self)
        self.search_bar.pack(fill="x", padx=10, pady=10)
        
        # Category selector
        self.category_selector = CategorySelector(self)
        self.category_selector.pack(fill="x", padx=10, pady=10)
        
        # Menu items grid
        self.menu_grid = ctk.CTkFrame(self, fg_color="transparent")
        self.menu_grid.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Configure grid for menu items
        for i in range(3):  # 3 rows
            self.menu_grid.grid_rowconfigure(i, weight=1)
        for j in range(3):  # 3 columns
            self.menu_grid.grid_columnconfigure(j, weight=1)
        
        # Add menu items
        self.create_menu_items()
        
        # User tabs at bottom
        self.user_tabs = UserTabs(self)
        self.user_tabs.pack(fill="x", pady=10)
        
    def create_menu_items(self):
        # Menu items data
        menu_items = [
            {
                "name": "Tomato Avocado Salad\nHealthy Diet",
                "price": "$17.99",
                "row": 0, "col": 0
            },
            {
                "name": "Original Chees Meat Burger\nWith Chips",
                "price": "$21.89",
                "has_quantity_selector": True,
                "row": 0, "col": 1
            },
            {
                "name": "Tacos Salsa With Chicken\nGrilled",
                "price": "$16.99",
                "row": 0, "col": 2
            },
            {
                "name": "Meat Sushi With With Tuna,\nSalmon Grilled",
                "price": "$19.99",
                "row": 1, "col": 0
            },
            {
                "name": "Fresh Orange Juice With Basil\nSugar Free",
                "price": "$12.99",
                "row": 1, "col": 1
            },
            {
                "name": "Original Chees Burger With\nMeat Chips",
                "price": "$16.99",
                "row": 1, "col": 2
            }
        ]
        
        # Create menu item cards
        for item in menu_items:
            card = MenuItemCard(self.menu_grid, item)
            card.grid(row=item["row"], column=item["col"], padx=10, pady=10, sticky="nsew")


# Order item component
class OrderItem(ctk.CTkFrame):
    def __init__(self, master, item_data, **kwargs):
        super().__init__(master, fg_color="transparent", height=60, **kwargs)
        
        # Quantity
        self.qty_label = ctk.CTkLabel(self, text=item_data["quantity"], 
                                    font=ctk.CTkFont(size=12, weight="bold"),
                                    width=20)
        self.qty_label.pack(side="left", padx=(0, 5))
        
        # Product info
        self.info_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.info_frame.pack(side="left", fill="both", expand=True, padx=5)
        
        self.name_label = ctk.CTkLabel(self.info_frame, text=item_data["name"], 
                                     font=ctk.CTkFont(size=12),
                                     justify="left", anchor="w")
        self.name_label.pack(anchor="w")
        
        # Price
        self.price_label = ctk.CTkLabel(self, text=item_data["price"], 
                                      font=ctk.CTkFont(size=12, weight="bold"))
        self.price_label.pack(side="right", padx=5)


# Order summary component  
class OrderSummary(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        
        # Subtotal
        self.subtotal_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.subtotal_frame.pack(fill="x", pady=2)
        
        self.subtotal_label = ctk.CTkLabel(self.subtotal_frame, text="Sub Total", 
                                         font=ctk.CTkFont(size=14))
        self.subtotal_label.pack(side="left")
        
        self.subtotal_value = ctk.CTkLabel(self.subtotal_frame, text="$63.96", 
                                         font=ctk.CTkFont(size=14))
        self.subtotal_value.pack(side="right")
        
        # Tax
        self.tax_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.tax_frame.pack(fill="x", pady=2)
        
        self.tax_label = ctk.CTkLabel(self.tax_frame, text="Tax 5%", 
                                   font=ctk.CTkFont(size=14))
        self.tax_label.pack(side="left")
        
        self.tax_value = ctk.CTkLabel(self.tax_frame, text="$3.75", 
                                    font=ctk.CTkFont(size=14))
        self.tax_value.pack(side="right")
        
        # Total
        self.total_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.total_frame.pack(fill="x", pady=5)
        
        self.total_label = ctk.CTkLabel(self.total_frame, text="Total Amount", 
                                      font=ctk.CTkFont(size=16, weight="bold"))
        self.total_label.pack(side="left")
        
        self.total_value = ctk.CTkLabel(self.total_frame, text="$67.71", 
                                      font=ctk.CTkFont(size=16, weight="bold"))
        self.total_value.pack(side="right")


# Payment methods component
class PaymentMethods(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        
        # Payment methods
        self.methods = ["Cash", "Credit/Debit Card", "Gift Card"]
        
        for method in self.methods:
            method_btn = ctk.CTkButton(self, text=method, 
                                      fg_color="#F0F0F0", text_color="black",
                                      hover_color="#E0E0E0", corner_radius=5)
            method_btn.pack(side="left", padx=5, expand=True, fill="x")


# Order section component (right side of main content)
class OrderSection(ctk.CTkFrame):
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
        self.order_btn = ctk.CTkButton(self, text="Place Order", 
                                     fg_color="#00B67A", text_color="white",
                                     corner_radius=5, height=40,
                                     font=ctk.CTkFont(size=14, weight="bold"))
        self.order_btn.grid(row=5, column=0, padx=20, pady=10, sticky="ew")
        
    def create_table_header(self):
        table_frame = ctk.CTkFrame(self, fg_color="transparent", height=50)
        table_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        table_label = ctk.CTkLabel(table_frame, text="Table 4", 
                                  font=ctk.CTkFont(size=18, weight="bold"))
        table_label.pack(side="left")
        
        time_label = ctk.CTkLabel(table_frame, text="Start time", text_color="gray",
                                 font=ctk.CTkFont(size=12))
        time_label.pack(side="left", padx=10)
        
        edit_btn = ctk.CTkButton(table_frame, text="✎", fg_color="transparent", 
                                text_color="gray", width=20, height=20)
        edit_btn.pack(side="right")
        
    def create_order_tabs(self):
        tabs_frame = ctk.CTkFrame(self, fg_color="transparent")
        tabs_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        
        tabs = ["Dine In", "Take Away", "Delivery"]
        for i, tab in enumerate(tabs):
            tab_btn = ctk.CTkButton(tabs_frame, text=tab, fg_color="transparent", 
                                   text_color="black" if i == 0 else "gray",
                                   hover_color="#F0F0F0", border_width=0)
            tab_btn.pack(side="left", padx=10)
            
            # Add indicator for active tab
            if i == 0:
                indicator = ctk.CTkFrame(tabs_frame, fg_color="#00B67A", height=3, width=60)
                indicator.place(x=10, y=30)
                
    def create_order_items_list(self):
        order_items_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
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


# Main content frame containing menu and order sections
class MainContent(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="#F0F3F5", corner_radius=15, **kwargs)
        
        # Configure grid
        self.grid_columnconfigure(0, weight=3)  # Menu section
        self.grid_columnconfigure(1, weight=2)  # Order section
        self.grid_rowconfigure(0, weight=1)
        
        # Create menu section (left side)
        self.menu_section = MenuSection(self)
        self.menu_section.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # Create order section (right side)
        self.order_section = OrderSection(self)
        self.order_section.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")


# Main application class
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Set appearance mode and color theme
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")
        
        # Set window size and color
        self.geometry("1200x800")
        self.configure(fg_color="white")
        
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.grid_rowconfigure(0, weight=1)
        
        # Center the window on the screen
        self.center_window()
        
        # Set title
        self.title("CIBU POS System")
        
        # Create sidebar
        self.sidebar = SideBar(self)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        # Create main content
        self.main_content = MainContent(self)
        self.main_content.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        window_width = 1200
        window_height = 800
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")


# Run the application
if __name__ == "__main__":
    app = App()
    app.mainloop()