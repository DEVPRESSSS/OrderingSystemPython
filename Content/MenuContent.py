import customtkinter as ctk
from Content.SearchBar import SearchBar
from Content.CategorySelector import CategorySelector
from Content.UserTabs import UserTabs
from Content.MenuItemCard import MenuItemCard


# Menu section component (left side of main content)
class MenuContent(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
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
