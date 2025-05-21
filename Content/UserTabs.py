import customtkinter

# User tabs component
class UserTabs(customtkinter.CTkFrame):
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
        user_tab = customtkinter.CTkFrame(self, fg_color="#F9F9F9", corner_radius=5)
        user_tab.pack(side="left", padx=10, pady=5)
        
        initial = customtkinter.CTkLabel(user_tab, text=user["initial"], 
                              fg_color="#FFD700", text_color="black",
                              width=30, height=30, corner_radius=15)
        initial.pack(side="left", padx=10, pady=10)
        
        user_info = customtkinter.CTkFrame(user_tab, fg_color="transparent")
        user_info.pack(side="left", padx=5, pady=10)
        
        name_label = customtkinter.CTkLabel(user_info, text=user["name"], 
                                 font=customtkinter.CTkFont(size=12, weight="bold"),
                                 anchor="w")
        name_label.pack(anchor="w")
        
        role_label = customtkinter.CTkLabel(user_info, text=user["role"], 
                                 font=customtkinter.CTkFont(size=10),
                                 text_color="gray", anchor="w")
        role_label.pack(anchor="w")

