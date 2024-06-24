import tkinter as tk
from tkinter import ttk, messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def create_page(frame):
    # 标题
    lbl_title = tk.Label(frame, text="发送邮件", font=("Arial", 18))
    lbl_title.pack(pady=10)

    # 输入 Gmail 账户
    lbl_email = tk.Label(frame, text="请输入您的 Gmail 地址：")
    lbl_email.pack(pady=5)

    entry_email = tk.Entry(frame, width=50)
    entry_email.pack(pady=5)

    # 输入密码
    lbl_password = tk.Label(frame, text="请输入您的 Gmail 密码：")
    lbl_password.pack(pady=5)

    entry_password = tk.Entry(frame, show='*', width=50)
    entry_password.pack(pady=5)

    # 输入收件人
    lbl_to = tk.Label(frame, text="请输入收件人邮箱地址：")
    lbl_to.pack(pady=5)

    entry_to = tk.Entry(frame, width=50)
    entry_to.pack(pady=5)

    # 输入主题
    lbl_subject = tk.Label(frame, text="请输入邮件主题：")
    lbl_subject.pack(pady=5)

    entry_subject = tk.Entry(frame, width=50)
    entry_subject.pack(pady=5)

    # 输入邮件内容
    lbl_body = tk.Label(frame, text="请输入邮件内容：")
    lbl_body.pack(pady=5)

    entry_body = tk.Text(frame, height=10, width=50)
    entry_body.pack(pady=5)

    # 发送邮件按钮
    def send_email():
        email = entry_email.get()
        password = entry_password.get()
        to_email = entry_to.get()
        subject = entry_subject.get()
        body = entry_body.get("1.0", tk.END)

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            text = msg.as_string()
            server.sendmail(email, to_email, text)
            server.quit()
            messagebox.showinfo("成功", "邮件发送成功！")
        except Exception as e:
            messagebox.showerror("错误", f"无法发送邮件：{e}")

    btn_send = tk.Button(frame, text="发送邮件", command=send_email)
    btn_send.pack(pady=10)

    # 添加扩充区域
    lbl_extension = tk.Label(frame, text="扩充功能：")
    lbl_extension.pack(pady=10)

    def add_email_field():
        lbl_new_to = tk.Label(frame, text="请输入额外的收件人邮箱地址：")
        lbl_new_to.pack(pady=5)

        entry_new_to = tk.Entry(frame, width=50)
        entry_new_to.pack(pady=5)

        def send_additional_email():
            new_to_email = entry_new_to.get()
            email = entry_email.get()
            password = entry_password.get()
            subject = entry_subject.get()
            body = entry_body.get("1.0", tk.END)

            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = new_to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, new_to_email, text)
                server.quit()
                messagebox.showinfo("成功", "邮件发送成功！")
            except Exception as e:
                messagebox.showerror("错误", f"无法发送邮件：{e}")

        btn_new_send = tk.Button(frame, text="发送额外邮件", command=send_additional_email)
        btn_new_send.pack(pady=10)

    btn_add_email = tk.Button(frame, text="添加更多收件人", command=add_email_field)
    btn_add_email.pack(pady=10)
