import json
import random
import string
import re

# 從 JSON 檔案讀取資料
def load_data(file_path):
    with open(file_path, "r") as json_file:
        return json.load(json_file)

# 生成隨機美國醫生執照號碼
def generate_license_number():
    return "MD-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=8))

# 刪除文字中的多餘空白
def remove_extra_spaces(text):
    if not isinstance(text, str):
        return ""
    return re.sub(r'\s+', ' ', text).strip()

# 將篩選後的資料儲存為 JSON 檔案
def save_filtered_data(datas, output_path):
    filtered_datas = []
    for data in datas:
        filtered_data = {
            "name": remove_extra_spaces(data.get("name", "")),
            "specialization": remove_extra_spaces(data.get("specialization", "")),
            "phone": remove_extra_spaces(data.get("phone", "")),
            "department": remove_extra_spaces(data.get("department", "")),
            "license_number": generate_license_number()
        }
        filtered_datas.append(filtered_data)
    with open(output_path, "w") as json_file:
        json.dump(filtered_datas, json_file, indent=4)

# 主程式
if __name__ == "__main__":
    input_file = "doctors_data.json"  # 輸入的 JSON 檔案路徑
    output_file = "filtered_data.json"  # 輸出的 JSON 檔案路徑

    datas = load_data(input_file)
    save_filtered_data(datas, output_file)

    print(f"資料已成功從 {input_file} 篩選並儲存到 {output_file}")
