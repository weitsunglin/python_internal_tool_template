# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import sys
import os
import importlib
import json

# 將 scripts 目錄添加到 sys.path 以便導入其他腳本
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

# 創建主應用程序窗口
root = tk.Tk()
root.title("基礎UI介面")
root.geometry("800x600")
root.resizable(False, False)

root.iconbitmap('icon.ico')

# 創建 Notebook 小部件
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# 加載配置文件
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# 動態加載頁面
for page in config["pages"]:
    module_name = page["module"]
    page_name = page["name"]
    
    module = importlib.import_module(module_name)
    page_frame = ttk.Frame(notebook)
    notebook.add(page_frame, text=page_name)
    module.create_page(page_frame)

root.mainloop()
