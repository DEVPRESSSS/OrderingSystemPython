import customtkinter
from Content.OrderItem import OrderItem
from Content.OrderSummary import OrderSummary
from Content.PaymentMethods import PaymentMethods


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
