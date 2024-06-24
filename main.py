# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, ttk
import sys
import os

# 將 scripts 目錄添加到 sys.path 以便導入其他腳本
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

from page1 import create_page1
from page2 import create_page2
from page3 import create_page3

# 創建主應用程序窗口
root = tk.Tk()
root.title("基礎UI介面")
root.geometry("800x600")
root.resizable(False, False)

root.iconbitmap('icon.ico')

# 創建 Notebook 小部件
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# 創建第一個頁面
page1 = ttk.Frame(notebook)
notebook.add(page1, text="第一頁")
create_page1(page1)

# 創建第二個頁面
page2 = ttk.Frame(notebook)
notebook.add(page2, text="第二頁")
create_page2(page2)

# 創建第三個頁面
page3 = ttk.Frame(notebook)
notebook.add(page3, text="第三頁")
create_page3(page3)

root.mainloop()
