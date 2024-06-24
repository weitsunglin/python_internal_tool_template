# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, ttk
import sys
import os

# 將 scripts 目錄添加到 sys.path 以便導入其他腳本
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))
from feature1 import print_log

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

label1 = tk.Label(page1, text="請輸入您的名字：")
label1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

entry1 = tk.Entry(page1)
entry1.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

# 按鈕點擊事件處理程序
def on_submit_click():
    name = entry1.get()
    if name:
        messagebox.showinfo("歡迎", "你好，{}!".format(name))
    else:
        messagebox.showwarning("警告", "名字不能為空！")

submit_button1 = tk.Button(page1, text="提交", command=on_submit_click)
submit_button1.grid(row=1, column=0, padx=5, pady=5)

# 創建第二個頁面
page2 = ttk.Frame(notebook)
notebook.add(page2, text="第二頁")

log_text = tk.Text(page2, height=10, width=80)
log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# 按鈕點擊事件處理程序
def on_log_click():
    log_message = print_log()
    log_text.insert(tk.END, log_message + "\n")

log_button = tk.Button(page2, text="打印日志", command=on_log_click)
log_button.pack(pady=10)

# 創建第三個頁面
page3 = ttk.Frame(notebook)
notebook.add(page3, text="第三頁")

label3 = tk.Label(page3, text="這是第三頁")
label3.pack(pady=10)

root.mainloop()
