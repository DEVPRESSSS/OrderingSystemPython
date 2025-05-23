import customtkinter
import os
from PIL import Image
from main import App
import hashlib
from mysql.connector import Error
from ConnectionString.ConnectionDb import DatabaseConnection


class LoginApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # Initialize database connection
        self.db = DatabaseConnection()
        self.db.connect()  # Connect to database on initialization

        # Configure appearance
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("green")
        
        # Configure window
        self.title("Ordering System - Login")
        self.geometry("900x600")
        self.resizable(False, False)
        
        # Center window on screen
        self.center_window()
        
        # Create main frame
        self.main_frame = customtkinter.CTkFrame(self, fg_color="white", corner_radius=0)
        self.main_frame.pack(fill="both", expand=True)
        
        # Create split layout (left for branding, right for login)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        
        # Left side - Branding area
        self.branding_frame = customtkinter.CTkFrame(self.main_frame, fg_color="#00B67A", corner_radius=0)
        self.branding_frame.grid(row=0, column=0, sticky="nsew")
        
        # Logo and branding text
        self.logo_label = customtkinter.CTkLabel(
            self.branding_frame, 
            text="ORDER PRO", 
            font=customtkinter.CTkFont(family="Arial", size=32, weight="bold"),
            text_color="white"
        )
        self.logo_label.pack(pady=(150, 10))
        
        self.slogan_label = customtkinter.CTkLabel(
            self.branding_frame, 
            text="Streamline Your Ordering Process", 
            font=customtkinter.CTkFont(family="Arial", size=16),
            text_color="white"
        )
        self.slogan_label.pack(pady=(0, 20))
        
        # Right side - Login area
        self.login_frame = customtkinter.CTkFrame(self.main_frame, fg_color="white", corner_radius=0)
        self.login_frame.grid(row=0, column=1, sticky="nsew")
        
        # Login form container
        self.form_frame = customtkinter.CTkFrame(self.login_frame, fg_color="white", corner_radius=15, border_width=1, border_color="#DDDDDD")
        self.form_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.7, relheight=0.7)
        
        # Welcome text
        self.welcome_label = customtkinter.CTkLabel(
            self.form_frame, 
            text="Welcome Back", 
            font=customtkinter.CTkFont(family="Arial", size=24, weight="bold"),
            text_color="#333333"
        )
        self.welcome_label.pack(pady=(40, 5))
        
        self.login_label = customtkinter.CTkLabel(
            self.form_frame, 
            text="Login to your account", 
            font=customtkinter.CTkFont(family="Arial", size=14),
            text_color="#666666"
        )
        self.login_label.pack(pady=(0, 30))
        
        # Username field
        self.username_frame = customtkinter.CTkFrame(self.form_frame, fg_color="transparent")
        self.username_frame.pack(fill="x", padx=30, pady=(10, 5))
        
        self.username_label = customtkinter.CTkLabel(
            self.username_frame, 
            text="Username", 
            anchor="w",
            font=customtkinter.CTkFont(family="Arial", size=12),
            text_color="#333333"
        )
        self.username_label.pack(anchor="w", padx=5)
        
        self.username_entry = customtkinter.CTkEntry(
            self.username_frame,
            placeholder_text="Enter your username",
            height=40,
            corner_radius=8,
            border_width=1,
            border_color="#DDDDDD",
            fg_color="white"
        )
        self.username_entry.pack(fill="x", pady=(5, 0))
        
        # Password field
        self.password_frame = customtkinter.CTkFrame(self.form_frame, fg_color="transparent")
        self.password_frame.pack(fill="x", padx=30, pady=(15, 5))
        
        self.password_label = customtkinter.CTkLabel(
            self.password_frame, 
            text="Password", 
            anchor="w",
            font=customtkinter.CTkFont(family="Arial", size=12),
            text_color="#333333"
        )
        self.password_label.pack(anchor="w", padx=5)
        
        self.password_entry = customtkinter.CTkEntry(
            self.password_frame,
            placeholder_text="Enter your password",
            height=40,
            corner_radius=8,
            border_width=1,
            border_color="#DDDDDD",
            fg_color="white",
            show="•"
        )
        self.password_entry.pack(fill="x", pady=(5, 0))
        
        # Remember me and forgot password
        self.options_frame = customtkinter.CTkFrame(self.form_frame, fg_color="transparent")
        self.options_frame.pack(fill="x", padx=30, pady=(5, 0))
        
        self.remember_var = customtkinter.StringVar(value="off")
        self.remember_checkbox = customtkinter.CTkCheckBox(
            self.options_frame,
            text="Remember me",
            variable=self.remember_var,
            onvalue="on",
            offvalue="off",
            checkbox_height=20,
            checkbox_width=20,
            corner_radius=4,
            font=customtkinter.CTkFont(family="Arial", size=12),
            text_color="#666666",
            fg_color="#00B67A",
            hover_color="#009966"
        )
        self.remember_checkbox.pack(side="left")
        
        self.forgot_button = customtkinter.CTkButton(
            self.options_frame,
            text="Forgot Password?",
            font=customtkinter.CTkFont(family="Arial", size=12),
            text_color="#00B67A",
            fg_color="transparent",
            hover_color="#F0F0F0",
            cursor="hand2",
            width=20,
            height=20,
            command=self.forgot_password
        )
        self.forgot_button.pack(side="right")
        
        # Login button
        self.login_button = customtkinter.CTkButton(
            self.form_frame,
            text="Login",
            font=customtkinter.CTkFont(family="Arial", size=14, weight="bold"),
            text_color="white",
            fg_color="#00B67A",
            hover_color="#009966",
            cursor="hand2",
            corner_radius=8,
            height=45,
            command=self.login
        )
        self.login_button.pack(fill="x", padx=30, pady=(30, 0))
        
        # Don't have an account
        self.signup_frame = customtkinter.CTkFrame(self.form_frame, fg_color="transparent")
        self.signup_frame.pack(pady=(15, 0))
        
        self.signup_label = customtkinter.CTkLabel(
            self.signup_frame,
            text="Don't have an account?",
            font=customtkinter.CTkFont(family="Arial", size=12),
            text_color="#666666"
        )
        self.signup_label.pack(side="left")
        
        self.signup_button = customtkinter.CTkButton(
            self.signup_frame,
            text="Sign Up",
            font=customtkinter.CTkFont(family="Arial", size=12, weight="bold"),
            text_color="#00B67A",
            fg_color="transparent",
            hover_color="#F0F0F0",
            cursor="hand2",
            width=20,
            command=self.signup
        )
        self.signup_button.pack(side="left", padx=(5, 0))
    
    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        window_width = 900
        window_height = 600
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            self.show_error("Please enter both username and password.")
            return
        
        user_data = self.authenticate_user(username, password)
        if user_data:
            print(f"User authenticated: {user_data}")
            if user_data['roleID'] == 'User-101':
                self.open_main_app(user_data)
            else:

                self.show_error("Access denied. Admins only.")
        else:
            self.show_error("Invalid username or password.")
    
    def show_error(self, message):
        error_window = customtkinter.CTkToplevel(self)
        error_window.title("Error")
        error_window.geometry("300x150")
        error_window.resizable(False, False)
        
        # Center the error window
        error_window.update_idletasks()
        width = error_window.winfo_width()
        height = error_window.winfo_height()
        x = (error_window.winfo_screenwidth() // 2) - (width // 2)
        y = (error_window.winfo_screenheight() // 2) - (height // 2)
        error_window.geometry(f"{width}x{height}+{x}+{y}")
        
        frame = customtkinter.CTkFrame(error_window)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        label = customtkinter.CTkLabel(
            frame,
            text=message,
            font=customtkinter.CTkFont(family="Arial", size=14)
        )
        label.pack(pady=(20, 10))
        
        button = customtkinter.CTkButton(
            frame,
            text="OK",
            font=customtkinter.CTkFont(family="Arial", size=12),
            fg_color="#00B67A",
            hover_color="#009966",
            command=error_window.destroy
        )
        button.pack(pady=(10, 20))
        
        error_window.transient(self)
        error_window.grab_set()
        self.wait_window(error_window)
    
    def forgot_password(self):
        print("Forgot password clicked")
    
    def signup(self):
        print("Sign up clicked")
    
    def open_main_app(self, user_data=None):
        print("Opening main application")
        self.withdraw() 
        
        # Pass user_data to main app if needed
        main_app = App()  # Modify App class to accept user_data if needed
    
        def on_main_app_close():
            main_app.destroy()
            self.db.disconnect()  # Close database connection
            self.destroy()  
        
        main_app.protocol("WM_DELETE_WINDOW", on_main_app_close)
        main_app.mainloop()

    def authenticate_user(self, username, password):
        """Authenticate user credentials against database"""

        # Check if database connection exists and is active
        if not self.db.connection or not self.db.connection.is_connected():
            if not self.db.connect():
                print("Failed to connect to database")
                return None
        
        try:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            
            query = "SELECT userID, username, roleID FROM appuser WHERE username = %s AND password = %s"
            self.db.cursor.execute(query, (username, hashed_password))
            result = self.db.cursor.fetchone()
            
            if result:
                return {
                    'userID': result[0],
                    'username': result[1],
                    'roleID': result[2]
                }
            

            return None
            
        except Error as e:
            print(f"Error during authentication: {e}")
            return None

    def __del__(self):
        """Destructor to ensure database connection is closed"""
        if hasattr(self, 'db') and self.db:
            self.db.disconnect()

    
if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()