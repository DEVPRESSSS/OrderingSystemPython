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
from Content.MainContent import MainContent



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