import customtkinter as ctk
from PIL import Image, ImageTk
import os
from pathlib import Path
import sys

class POSApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure the window
        self.title("CIBU POS")
        self.geometry("1200x800")
        self.configure(fg_color="white")
        
        # Center the window
        self.center_window()
        
        # Set appearance mode
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")
        
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)  # Main content area takes more space
        self.grid_rowconfigure(0, weight=1)
        
        # Load images
        self.load_images()
        
        # Create sidebar
        self.create_sidebar()
        
        # Create main content
        self.create_main_content()
        
    def load_images(self):
        # This function would load all the needed images
        # For prototyping, we'll use placeholder images
        # In a real app, you'd load actual images from files
        
        # Create directory for placeholder images if it doesn't exist
        self.image_dir = Path("placeholder_images")
        self.image_dir.mkdir(exist_ok=True)
        
        # Dictionary to store our images
        self.images = {}
        
        # Function to create and save a colored placeholder image
        def create_placeholder(name, color, size=(100, 100)):
            img = Image.new('RGB', size, color)
            img_path = self.image_dir / f"{name}.png"
            img.save(img_path)
            return str(img_path)
        
        # Create some placeholder food images with different colors
        food_colors = [
            ("tomato_salad", "#FFDDDD"),
            ("burger", "#DDDDAA"),
            ("taco_chicken", "#DDFFDD"),
            ("meat_sushi", "#FFDDFF"),
            ("orange_juice", "#FFEECC"),
            ("cheese_burger", "#EEDDBB"),
            ("fresh_orange", "#FFDDAA"),
            ("meat_sushi_tuna", "#DDFFEE"),
            ("original_cheese", "#FFEEDD"),
        ]
        
        # Create the placeholder images
        for name, color in food_colors:
            create_placeholder(name, color)
        
        # Logo placeholder
        create_placeholder("logo", "#FFFFFF", (50, 50))
        
    def create_sidebar(self):
        # Create sidebar frame
        sidebar = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0, border_width=1, border_color="#EEEEEE")
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_rowconfigure(10, weight=1)  # Push logout to bottom
        
        # Logo and name
        logo_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        logo_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        
        try:
            logo_img = ctk.CTkImage(Image.open("placeholder_images/logo.png"), size=(24, 24))
            logo_label = ctk.CTkLabel(logo_frame, image=logo_img, text="")
            logo_label.pack(side="left", padx=(0, 10))
        except:
            pass
        
        name_label = ctk.CTkLabel(logo_frame, text="CIBU POS", font=ctk.CTkFont(size=16, weight="bold"))
        name_label.pack(side="left")
        
        # Menu button
        menu_button = ctk.CTkButton(sidebar, text="Menu", fg_color="#00B67A", corner_radius=5, 
                                    height=36, font=ctk.CTkFont(size=14, weight="bold"))
        menu_button.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        
        # Other sidebar buttons
        sidebar_buttons = [
            ("Table Services", "table"),
            ("Reservation", "reservation"),
            ("Delivery", "delivery"),
            ("Accounting", "accounting"),
            ("Settings", "settings")
        ]
        
        for i, (text, icon_name) in enumerate(sidebar_buttons):
            button_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
            button_frame.grid(row=i+2, column=0, padx=20, pady=5, sticky="ew")
            
            # Icon (placeholder)
            icon_label = ctk.CTkLabel(button_frame, text="", width=24, height=24)
            icon_label.pack(side="left", padx=(0, 10))
            
            # Button text
            text_label = ctk.CTkLabel(button_frame, text=text, anchor="w", 
                                     font=ctk.CTkFont(size=14))
            text_label.pack(side="left", fill="x", expand=True)
        
        # Logout button at the bottom
        logout_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        logout_frame.grid(row=10, column=0, padx=20, pady=20, sticky="ew")
        
        logout_icon = ctk.CTkLabel(logout_frame, text="", width=24, height=24)
        logout_icon.pack(side="left", padx=(0, 10))
        
        logout_label = ctk.CTkLabel(logout_frame, text="Logout", anchor="w", 
                                   font=ctk.CTkFont(size=14))
        logout_label.pack(side="left", fill="x", expand=True)
        
    def create_main_content(self):
        # Create main content frame
        main_content = ctk.CTkFrame(self, fg_color="#F0F3F5", corner_radius=15)
        main_content.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        # Configure grid for main content
        main_content.grid_columnconfigure(0, weight=3)  # Menu section
        main_content.grid_columnconfigure(1, weight=2)  # Order section
        main_content.grid_rowconfigure(0, weight=1)
        
        # Create menu section (left side)
        self.create_menu_section(main_content)
        
        # Create order section (right side)
        self.create_order_section(main_content)
        
    def create_menu_section(self, parent):
        menu_section = ctk.CTkFrame(parent, fg_color="transparent")
        menu_section.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # Search bar and filter
        search_frame = ctk.CTkFrame(menu_section, fg_color="transparent")
        search_frame.pack(fill="x", padx=10, pady=10)
        
        # Menu icon
        menu_icon = ctk.CTkLabel(search_frame, text="≡", font=ctk.CTkFont(size=20))
        menu_icon.pack(side="left", padx=(0, 10))
        
        # Search entry
        search_var = ctk.StringVar()
        search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search Product here...", width=300,
                                   fg_color="#F5F5F5", border_color="#E0E0E0")
        search_entry.pack(side="left", padx=10)
        
        # Filter icon
        filter_icon = ctk.CTkLabel(search_frame, text="☰", font=ctk.CTkFont(size=20))
        filter_icon.pack(side="left", padx=10)
        
        # Category buttons
        category_frame = ctk.CTkFrame(menu_section, fg_color="transparent")
        category_frame.pack(fill="x", padx=10, pady=10)
        
        categories = [
            ("All", "all"),
            ("Breakfast", "breakfast"),
            ("Soups", "soups"),
            ("Pasta", "pasta"),
            ("Main Course", "main_course"),
            ("Burger", "burger")
        ]
        
        for text, icon_name in categories:
            category_button = ctk.CTkButton(category_frame, text=text, 
                                           fg_color="#F5F5F5", text_color="black",
                                           hover_color="#E0E0E0", corner_radius=15,
                                           width=100, height=70)
            category_button.pack(side="left", padx=5, pady=5)
        
        # Menu items grid
        menu_grid = ctk.CTkFrame(menu_section, fg_color="transparent")
        menu_grid.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Configure grid for menu items
        for i in range(3):  # 3 rows
            menu_grid.grid_rowconfigure(i, weight=1)
        for j in range(3):  # 3 columns
            menu_grid.grid_columnconfigure(j, weight=1)
        
        # Menu items data
        menu_items = [
            {
                "name": "Tomato Avocado Salad\nHealthy Diet",
                "price": "$17.99",
                "image": "tomato_salad",
                "row": 0, "col": 0
            },
            {
                "name": "Original Chees Meat Burger\nWith Chips",
                "price": "$21.89",
                "image": "burger",
                "row": 0, "col": 1
            },
            {
                "name": "Tacos Salsa With Chicken\nGrilled",
                "price": "$16.99",
                "image": "taco_chicken",
                "row": 0, "col": 2
            },
            {
                "name": "Meat Sushi With With Tuna,\nSalmon Grilled",
                "price": "$19.99",
                "image": "meat_sushi",
                "row": 1, "col": 0
            },
            {
                "name": "Fresh Orange Juice With Basil\nSugar Free",
                "price": "$12.99",
                "image": "orange_juice",
                "row": 1, "col": 1
            },
            {
                "name": "Original Chees Burger With\nMeat Chips",
                "price": "$16.99",
                "image": "cheese_burger",
                "row": 1, "col": 2
            }
        ]
        
        # Create menu item cards
        for item in menu_items:
            self.create_menu_card(menu_grid, item)
            
        # Bottom user tabs
        users_frame = ctk.CTkFrame(menu_section, fg_color="transparent")
        users_frame.pack(fill="x", pady=10)
        
        # User tabs
        users = [
            {"initial": "T1", "name": "Jacob Jones", "role": "Waiter - Section 2"},
            {"initial": "T2", "name": "Esther Howard", "role": "Cashier - Kitchen"},
            {"initial": "T3", "name": "Robert Fox", "role": "Barman - Kitchen"}
        ]
        
        for user in users:
            user_tab = ctk.CTkFrame(users_frame, fg_color="#F9F9F9", corner_radius=5)
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
            
    def create_menu_card(self, parent, item):
        # Create a card for menu item
        card = ctk.CTkFrame(parent, fg_color="white", corner_radius=10)
        card.grid(row=item["row"], column=item["col"], padx=10, pady=10, sticky="nsew")
        
        # Food image
        try:
            img_path = f"placeholder_images/{item['image']}.png"
            img = ctk.CTkImage(Image.open(img_path), size=(150, 100))
            img_label = ctk.CTkLabel(card, image=img, text="")
            img_label.pack(pady=(10, 5))
        except:
            img_label = ctk.CTkLabel(card, text="Food Image", fg_color="#F0F0F0", 
                                    width=150, height=100)
            img_label.pack(pady=(10, 5))
        
        # Food info
        info_frame = ctk.CTkFrame(card, fg_color="transparent")
        info_frame.pack(fill="x", padx=10, pady=5, anchor="w")
        
        name_label = ctk.CTkLabel(info_frame, text=item["name"], 
                                 font=ctk.CTkFont(size=12, weight="bold"),
                                 justify="left", anchor="w")
        name_label.pack(anchor="w")
        
        # Price and calories
        price_frame = ctk.CTkFrame(card, fg_color="transparent")
        price_frame.pack(fill="x", padx=10, pady=5)
        
        price_label = ctk.CTkLabel(price_frame, text=item["price"], 
                                  font=ctk.CTkFont(size=14, weight="bold"),
                                  anchor="w")
        price_label.pack(side="left")
        
        calories = ctk.CTkLabel(price_frame, text="400 kcal", 
                               font=ctk.CTkFont(size=10),
                               text_color="gray", anchor="e")
        calories.pack(side="right")
        
        # Add to cart button
        if item["image"] == "burger":  # The burger item has the quantity selector
            quantity_frame = ctk.CTkFrame(card, fg_color="transparent")
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
            add_btn = ctk.CTkButton(card, text="Add to Cart", fg_color="#F0F0F0", 
                                  text_color="black", corner_radius=5,
                                  hover_color="#E0E0E0")
            add_btn.pack(fill="x", padx=10, pady=10)
        
    def create_order_section(self, parent):
        order_section = ctk.CTkFrame(parent, fg_color="white", corner_radius=15)
        order_section.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        order_section.grid_rowconfigure(2, weight=1)  # Order items list
        order_section.grid_columnconfigure(0, weight=1)
        
        # Table number
        table_frame = ctk.CTkFrame(order_section, fg_color="transparent", height=50)
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
        
        # Order type tabs
        tabs_frame = ctk.CTkFrame(order_section, fg_color="transparent")
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
        
        # Order items list
        order_items_frame = ctk.CTkScrollableFrame(order_section, fg_color="transparent")
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
            self.create_order_item(order_items_frame, item)
        
        # Order summary
        summary_frame = ctk.CTkFrame(order_section, fg_color="transparent")
        summary_frame.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        
        # Subtotal
        subtotal_frame = ctk.CTkFrame(summary_frame, fg_color="transparent")
        subtotal_frame.pack(fill="x", pady=2)
        
        subtotal_label = ctk.CTkLabel(subtotal_frame, text="Sub Total", 
                                     font=ctk.CTkFont(size=14))
        subtotal_label.pack(side="left")
        
        subtotal_value = ctk.CTkLabel(subtotal_frame, text="$63.96", 
                                     font=ctk.CTkFont(size=14))
        subtotal_value.pack(side="right")
        
        # Tax
        tax_frame = ctk.CTkFrame(summary_frame, fg_color="transparent")
        tax_frame.pack(fill="x", pady=2)
        
        tax_label = ctk.CTkLabel(tax_frame, text="Tax 5%", 
                               font=ctk.CTkFont(size=14))
        tax_label.pack(side="left")
        
        tax_value = ctk.CTkLabel(tax_frame, text="$3.75", 
                                font=ctk.CTkFont(size=14))
        tax_value.pack(side="right")
        
        # Total
        total_frame = ctk.CTkFrame(summary_frame, fg_color="transparent")
        total_frame.pack(fill="x", pady=5)
        
        total_label = ctk.CTkLabel(total_frame, text="Total Amount", 
                                  font=ctk.CTkFont(size=16, weight="bold"))
        total_label.pack(side="left")
        
        total_value = ctk.CTkLabel(total_frame, text="$67.71", 
                                  font=ctk.CTkFont(size=16, weight="bold"))
        total_value.pack(side="right")
        
        # Payment methods
        payment_frame = ctk.CTkFrame(order_section, fg_color="transparent")
        payment_frame.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
        
        # Payment icons
        methods = ["Cash", "Credit/Debit Card", "Gift Card"]
        
        for method in methods:
            method_btn = ctk.CTkButton(payment_frame, text=method, 
                                      fg_color="#F0F0F0", text_color="black",
                                      hover_color="#E0E0E0", corner_radius=5)
            method_btn.pack(side="left", padx=5, expand=True, fill="x")
        
        # Place order button
        order_btn = ctk.CTkButton(order_section, text="Place Order", 
                                 fg_color="#00B67A", text_color="white",
                                 corner_radius=5, height=40,
                                 font=ctk.CTkFont(size=14, weight="bold"))
        order_btn.grid(row=5, column=0, padx=20, pady=10, sticky="ew")
        
    def create_order_item(self, parent, item):
        # Create an order item row
        item_frame = ctk.CTkFrame(parent, fg_color="transparent", height=60)
        item_frame.pack(fill="x", pady=5)
        
        # Quantity
        qty_label = ctk.CTkLabel(item_frame, text=item["quantity"], 
                                font=ctk.CTkFont(size=12, weight="bold"),
                                width=20)
        qty_label.pack(side="left", padx=(0, 5))
        
        # Product info
        info_frame = ctk.CTkFrame(item_frame, fg_color="transparent")
        info_frame.pack(side="left", fill="both", expand=True, padx=5)
        
        name_label = ctk.CTkLabel(info_frame, text=item["name"], 
                                 font=ctk.CTkFont(size=12),
                                 justify="left", anchor="w")
        name_label.pack(anchor="w")
        
        # Price
        price_label = ctk.CTkLabel(item_frame, text=item["price"], 
                                  font=ctk.CTkFont(size=12, weight="bold"))
        price_label.pack(side="right", padx=5)
        
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
    app = POSApp()
    app.mainloop()