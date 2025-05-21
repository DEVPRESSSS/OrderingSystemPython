import customtkinter
from Content.CategorySelector import CategorySelector
from Content.UserTabs import UserTabs

# Search and filter bar component
class SearchBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        
        # Menu icon
        self.menu_icon = customtkinter.CTkLabel(self, text="≡", font=customtkinter.CTkFont(size=20))
        self.menu_icon.pack(side="left", padx=(0, 10))
        
        # Search entry
        self.search_var = customtkinter.StringVar()
        self.search_entry = customtkinter.CTkEntry(self, placeholder_text="Search Product here...", width=300,
                                   fg_color="#F5F5F5", border_color="#E0E0E0")
        self.search_entry.pack(side="left", padx=10)
        
        # Filter icon
        self.filter_icon = customtkinter.CTkLabel(self, text="☰", font=customtkinter.CTkFont(size=20))
        self.filter_icon.pack(side="left", padx=10)