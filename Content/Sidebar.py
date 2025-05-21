import customtkinter
from Content.MenuContent import MenuContent
from Content.SettingsContent import SettingsContent

class SideBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        # Remove width from here if specified in kwargs
        super().__init__(master, **kwargs)
        
        # Add some content to the sidebar
        self.label = customtkinter.CTkLabel(self, 
                                            text="Ordering System",)
        self.label.grid(row=0, 
                        column=0, 
                        padx=20, 
                        pady=20)



        #Menu Button
        self.menu_btn = customtkinter.CTkButton(self, text="Menu",
                                               fg_color="#00B67A",
                                               cursor="hand2",
                                               command=self.MenuButtonEvent)
        self.menu_btn.grid(row=1,
                           column=0, 
                           padx=20,                            
                           pady=10)
        
        #Settings Button
        self.settings_btn = customtkinter.CTkButton(self, 
                                                 text="Settings",
                                                 fg_color="#00B67A",
                                                 cursor="hand2",
                                                 command=self.SettingsButtonEvent
                                                 )
        self.settings_btn.grid(row=2, 
                          column=0, 
                          padx=20, 
                          pady=10)
        

        #Logout Button
        self.logout_btn = customtkinter.CTkButton(self, text="Logout",
                                               fg_color="#00B67A",
                                                cursor="hand2" 
                                               )
        self.logout_btn.grid(row=3, 
                          column=0, 
                          padx=20, 
                          pady=10)
        
    #Menu Button Event 
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
                

    #Settings Button Event
    def SettingsButtonEvent(self):
        # Access the main app instance through the master attribute
        app = self.master
        
        # Remove existing main_content
        app.main_content.grid_forget()
        
        # Create new MenuContent as a child of the app, not the sidebar
        app.main_content = SettingsContent(app, fg_color="#ffffff",
                                    corner_radius=8,                                   
                                    border_color="#DDDDDD",
                                    border_width=1)
        app.main_content.grid(row=0, 
                        column=1, 
                        sticky="nsew", 
                        padx=6, 
                        pady=6)
                
