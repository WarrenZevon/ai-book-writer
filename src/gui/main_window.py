import tkinter as tk
from tkinter import ttk, messagebox
from core.book_manager import BookManager
from core.ai_generator import AIGenerator

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.book_manager = BookManager()
        self.ai_generator = AIGenerator()
        
        self.setup_ui()
        
    def setup_ui(self):
        # Create main container
        self.main_container = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Outline
        self.outline_frame = ttk.Frame(self.main_container)
        self.main_container.add(self.outline_frame)
        self.setup_outline_panel()
        
        # Right panel - Content
        self.content_frame = ttk.Frame(self.main_container)
        self.main_container.add(self.content_frame)
        self.setup_content_panel()
        
    def setup_outline_panel(self):
        # Outline header
        header = ttk.Frame(self.outline_frame)
        header.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(header, text="Book Outline").pack(side=tk.LEFT)
        ttk.Button(header, text="New Chapter").pack(side=tk.RIGHT)
        
        # Outline tree
        self.outline_tree = ttk.Treeview(self.outline_frame)
        self.outline_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
    def setup_content_panel(self):
        # Content tools
        tools = ttk.Frame(self.content_frame)
        tools.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(tools, text="Generate Content").pack(side=tk.LEFT)
        ttk.Button(tools, text="Save").pack(side=tk.LEFT, padx=5)
        
        # Generated options
        self.options_frame = ttk.Frame(self.content_frame)
        self.options_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create three text areas for options
        self.option_texts = []
        for i in range(3):
            frame = ttk.LabelFrame(self.options_frame, text=f"Option {i+1}")
            frame.pack(fill=tk.BOTH, expand=True, pady=5)
            
            text = tk.Text(frame, height=10)
            text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
            self.option_texts.append(text)
            
            btn_frame = ttk.Frame(frame)
            btn_frame.pack(fill=tk.X, padx=5, pady=5)
            ttk.Button(btn_frame, text="Select").pack(side=tk.LEFT)
            ttk.Button(btn_frame, text="Regenerate").pack(side=tk.LEFT, padx=5)
    
    def generate_content(self):
        # To be implemented
        pass
    
    def save_content(self):
        # To be implemented
        pass
    
    def select_option(self, option_index):
        # To be implemented
        pass