# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import sys
import os
import importlib
import json

# 將 scripts 目錄添加到 sys.path 以便導入其他腳本
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'pages'))

# 創建主應用程序窗口
root = tk.Tk()
root.title("基礎UI介面")
root.geometry("800x600")
root.resizable(False, False)

root.iconbitmap('icon.ico')

# 使用 grid 方法來更精確地控制佈局
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# 創建導航按鈕的 Frame
nav_frame = tk.Frame(root)
nav_frame.grid(row=0, column=0, sticky='ew', padx=20, pady=5)


def open_about():
    # 關於按鈕點擊事件
    tk.messagebox.showinfo("關於", "這是關於頁面")



about_button = tk.Button(nav_frame, text="關於", command=open_about)
about_button.pack(side=tk.LEFT, padx=5)

# 創建 Notebook 小部件
notebook = ttk.Notebook(root)
notebook.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)

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
