import tkinter as tk
from tkinter import ttk
import os

def create_page(frame):
    # 標題
    lbl_title = tk.Label(frame, text="打開軟體", font=("Arial", 18))
    lbl_title.pack(pady=10)

    # 輸入路徑
    lbl_path = tk.Label(frame, text="請輸入軟體路徑：")
    lbl_path.pack(pady=5)

    entry_path = tk.Entry(frame, width=50)
    entry_path.pack(pady=5)

    # 打開軟體按鈕
    def open_software():
        path = entry_path.get()
        if os.path.isfile(path):
            os.startfile(path)
        else:
            tk.messagebox.showerror("錯誤", "無法找到該文件，請檢查路徑。")

    btn_open = tk.Button(frame, text="打開軟體", command=open_software)
    btn_open.pack(pady=10)

    # 添加擴充區域
    lbl_extension = tk.Label(frame, text="擴充功能：")
    lbl_extension.pack(pady=10)

    def add_path_field():
        lbl_new_path = tk.Label(frame, text="請輸入額外的軟體路徑：")
        lbl_new_path.pack(pady=5)

        entry_new_path = tk.Entry(frame, width=50)
        entry_new_path.pack(pady=5)

        def open_additional_software():
            new_path = entry_new_path.get()
            if os.path.isfile(new_path):
                os.startfile(new_path)
            else:
                tk.messagebox.showerror("錯誤", "無法找到該文件，請檢查路徑。")

        btn_new_open = tk.Button(frame, text="打開額外的軟體", command=open_additional_software)
        btn_new_open.pack(pady=10)

    btn_add_path = tk.Button(frame, text="添加更多路徑", command=add_path_field)
    btn_add_path.pack(pady=10)
