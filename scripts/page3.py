import tkinter as tk
import requests

def create_page(page3):
    label3 = tk.Label(page3, text="這是第三頁")
    label3.pack(pady=10)
    
    def login_and_do_something():
        login_url = "https://httpbin.org/post"  # 測試用的登入 URL
        target_url = "https://httpbin.org/get"  # 測試用的操作 URL
        
        # 測試用的登入憑證
        login_data = {
            'username': 'test_user',
            'password': 'test_pass'
        }
        
        # 創建一個會話
        session = requests.Session()
        
        # 登入
        response = session.post(login_url, data=login_data)
        
        if response.status_code == 200:
            print("登入成功")
            # 在這裡進行登入後的操作，例如訪問其他頁面或執行特定操作
            target_response = session.get(target_url)
            if target_response.status_code == 200:
                print("操作成功")
                # 處理 target_response 的內容
                print(target_response.text)
            else:
                print("操作失敗", target_response.status_code)
        else:
            print("登入失敗", response.status_code)

    login_button = tk.Button(page3, text="自動登入並操作", command=login_and_do_something)
    login_button.pack(pady=10)

# 測試範例的創建
if __name__ == "__main__":
    root = tk.Tk()
    root.title("測試範例")
    page3 = tk.Frame(root)
    page3.pack(fill="both", expand=True)
    create_page3(page3)
    root.mainloop()
