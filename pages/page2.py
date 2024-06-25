# page2.py
import tkinter as tk
from feature1 import print_log

def create_page(page2):
    log_text = tk.Text(page2, height=10, width=80)
    log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    # 按鈕點擊事件處理程序
    def on_log_click():
        log_message = print_log()
        log_text.insert(tk.END, log_message + "\n")

    log_button = tk.Button(page2, text="打印日志", command=on_log_click)
    log_button.pack(pady=10)
