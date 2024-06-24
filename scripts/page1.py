# page1.py
import tkinter as tk
from tkinter import messagebox

def create_page1(page1):
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
