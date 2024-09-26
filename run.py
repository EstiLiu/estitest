import os
import json
import subprocess

# 讀取json檔案
with open("C:/Users/Esti.Liu/Desktop/mobile FirstTMS script/Data.json", "r") as file:  # 修改為你的檔案路徑
    data = json.load(file)

# 動態選擇 SIT 或 UAT
environment = input("請輸入環境 (SIT 或 UAT): ").upper() 
if environment == "SIT":
    target_url = data["SIT_url"]
    target_id = data["SIT_id"]
    target_pw = data["SIT_pw"]
    print(f"正在訪問 SIT 環境，網址為: {target_url}")
elif environment == "UAT":
    target_url = data["UAT_url"]
    target_id = data["UAT_id"]
    target_pw = data["UAT_pw"]
    print(f"正在訪問 UAT 環境，網址為: {target_url}")
else:
    print("無效的環境選擇，請選擇 SIT 或 UAT")
    exit()

# # 選擇環境，這裡可以根據需要選擇 SIT 或 UAT(你可以通過條件動態設置)
#target_url = url_data["SIT_url"]  #URL
#target_id = url_data["UAT_ID"] #使用者ID

# 設置環境變量
os.environ["TARGET_url"] = target_url
os.environ["TARGET_id"] = target_id
os.environ["TARGET_pw"] = target_pw

# 打開並運行 FirstTMS_mobile_HomePage.py 腳本
script_path = r"C:/Users/Esti.Liu/Desktop/mobile FirstTMS script/FirstTMS_mobile_HomePage.py"  # 修改為你的實際路徑

# 使用 subprocess 模塊來執行腳本
try:
    result = subprocess.run(["python", script_path], check=True, capture_output=True, text=True)
    print("腳本執行成功！輸出如下：")
    print(result.stdout)  # 輸出腳本的標準輸出
except subprocess.CalledProcessError as e:
    print("腳本執行失敗，錯誤如下：")
    print(e.stderr)  # 輸出腳本的錯誤訊息