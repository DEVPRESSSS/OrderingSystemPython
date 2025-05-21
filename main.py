import customtkinter

class SideBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        # Remove width from here if specified in kwargs
        super().__init__(master, **kwargs)
        
        # Add some content to the sidebar
        self.label = customtkinter.CTkLabel(self, 
                                            text="POS System",)
        self.label.grid(row=0, 
                        column=0, 
                        padx=20, 
                        pady=20)



        #Buttons in the sidebar
        self.button1 = customtkinter.CTkButton(self, text="Menu",
                                               fg_color="#00B67A",
                                               cursor="hand2",
                                               command=self.MenuButtonEvent)
        self.button1.grid(row=1,
                           column=0, 
                           padx=20,                            
                           pady=10)
        
        self.button2 = customtkinter.CTkButton(self, 
                                                 text="Accounting",
                                                 fg_color="#00B67A",
                                                 cursor="hand2")
        self.button2.grid(row=2, 
                          column=0, 
                          padx=20, 
                          pady=10)
        
        self.button3 = customtkinter.CTkButton(self, text="Logout",
                                               fg_color="#00B67A",
                                                cursor="hand2" 
                                               )
        self.button3.grid(row=3, 
                          column=0, 
                          padx=20, 
                          pady=10)
        

    def MenuButtonEvent(self):
        # Access the main app instance through the master attribute
        app = self.master
        
        # Remove existing main_content
        app.main_content.grid_forget()
        
        # Create new MenuContent as a child of the app, not the sidebar
        app.main_content = MenuContent(app, fg_color="#ffffff",
                                    corner_radius=8,                                   
                                    border_color="#DDDDDD",
                                    border_width=1)
        app.main_content.grid(row=0, 
                        column=1, 
                        sticky="nsew", 
                        padx=6, 
                        pady=6)
                


#Menu Content Class that will be display all the Menu items
class MenuContent(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.main_label = customtkinter.CTkLabel(
            master=self,
            text="Menu Content Area",
            font=("Arial", 20)
        )
        self.main_label.pack(expand=True)


#Dashboard Class
class MainContent(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.main_label = customtkinter.CTkLabel(
            master=self,
            text="Main Content Area",
            font=("Arial", 20)
        )
        self.main_label.pack(expand=True)


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
        self.title("Welcome")
        
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
        self.main_content = MainContent(self, fg_color="#ffffff",
                                        corner_radius=8,                                   
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