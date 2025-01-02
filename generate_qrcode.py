import os, sys
import qrcode
import pandas as pd
from tqdm import tqdm
from PIL import Image

def generate_hongchuang1(data: dict, output_file: str):
    """
    样式1: 根据输入数据生成二维码, 内容为拼接的访问链接

    参数：
        data (dict): 包含以下键值对的字典：
            - certificate: 证书编号
            - systemOrder: 系统单号
            - serial: 序号
            - entrust: 委托单号
            - unit: 证书单位
            - calibration: 校准日期
            - device: 仪器名称
            - factory: 出厂编号
            - management: 管理编号
        output_file (str): 保存二维码的文件路径（支持 PNG、JPEG 等格式）。
    """

    base_url = "https://hongchuang-1320385567.cos.ap-guangzhou.myqcloud.com/hongchuang1.html"
    query_params = "&".join([f"{key}={value}" for key, value in data.items() if value])
    full_url = f"{base_url}?{query_params}"
    qr = qrcode.QRCode(border=0)
    qr.add_data(full_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    img = img.resize((121, 121), Image.Resampling.LANCZOS)
    img.save(output_file)

    return None


def generate_hongchuang2(data: dict, output_file: str):
    """
    样式2: 根据输入数据生成二维码, 内容为拼接的访问链接

    参数：
        data (dict): 包含以下键值对的字典：
            - certificateUnit: 证书单位
            - instrumentName: 仪器名称
            - serialNumber: 出厂编号
            - assetNumber: 管理编号
            - calibrationDate: 校准日期
        output_file (str): 保存二维码的文件路径（支持 PNG、JPEG 等格式）。
    """

    base_url = "https://hongchuang-1320385567.cos.ap-guangzhou.myqcloud.com/hongchuang2.html"
    full_url = f"{base_url}?{'&'.join(f'{k}={v}' for k, v in data.items() if v)}"
    qr = qrcode.QRCode(border=0)
    qr.add_data(full_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    img = img.resize((121, 121), Image.Resampling.LANCZOS)
    img.save(output_file)

    return None


def generate_hongchuang3(data: dict, output_file: str):
    """
    样式3: 根据输入数据生成二维码, 内容为拼接的访问链接

    参数：
        data (dict): 包含以下键值对的字典：
            - certificateUnit: 证书单位
            - certificateNumber: 证书编号
            - certificateType: 证书类型
            - instrumentName: 仪器名称
            - model: 规格型号
            - serialNumber: 出厂编号
            - assetNumber: 资产编号
            - manufacturer: 制造厂商
            - calibrationDate: 检/校日期
            - calibrationPersonnel: 校准/检定员
        output_file (str): 保存二维码的文件路径（支持 PNG、JPEG 等格式）。
    """
    base_url = "https://hongchuang-1320385567.cos.ap-guangzhou.myqcloud.com/hongchuang3.html"
    full_url = f"{base_url}?{'&'.join(f'{k}={v}' for k, v in data.items() if v)}"

    qr = qrcode.QRCode(border=0)
    qr.add_data(full_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    img = img.resize((121, 121), Image.Resampling.LANCZOS)
    img.save(output_file)

    return None


def generate_hongchuang4(data: dict, output_file: str):
    """
    样式4: 根据输入数据生成二维码, 内容为拼接的访问链接

    参数：
        data (dict): 包含以下键值对的字典：
            - company: 公司名称
            - device: 设备名称
            - serial: 出厂编号
            - management: 管理编号
            - calibration: 检/校日期
            - certificate: 证书编号
        output_file (str): 保存二维码的文件路径（支持 PNG、JPEG 等格式）。
    """
    base_url = "https://hongchuang-1320385567.cos.ap-guangzhou.myqcloud.com/hongchuang4.html"
    full_url = f"{base_url}?{'&'.join(f'{k}={v}' for k, v in data.items() if v)}"

    qr = qrcode.QRCode(border=0)
    qr.add_data(full_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    img = img.resize((121, 121), Image.Resampling.LANCZOS)
    img.save(output_file)

    return None


if __name__ == '__main__':
    file_name = "二维码.xlsx"
    if not os.path.exists(file_name):
        print(f"缺失文件: {file_name}")
        sys.exit(1)
    try:
        data_frame = pd.read_excel(file_name)
        print(f"成功读取文件: {file_name}")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        sys.exit(1)

    print("请选择生成网页样式：（1 or 2 or 3 or 4）")
    choice = input("输入样式编号：").strip()
    data = {}

    if choice == '1':
        os.makedirs("style1_qrcodes", exist_ok=True)

        column_mapping = {
            "certificate": "证书编号",
            "systemOrder": "系统单号",
            "serial": "序号",
            "entrust": "委托单号",
            "unit": "证书单位",
            "calibration": "校准日期",
            "device": "仪器名称",
            "factory": "出厂编号",
            "management": "管理编号"
        }

        for index, row in tqdm(data_frame.iterrows(), total=len(data_frame), desc="生成二维码"):
            data = {k: row[v] for k, v in column_mapping.items() if pd.notna(row[v]) and row[v] != ""}
            certificate_number = row["证书编号"]
            generate_hongchuang1(data, f"style1_qrcodes/qrcode_{certificate_number}.png")

    if choice == '2':
        os.makedirs("style2_qrcodes", exist_ok=True)

        column_mapping = {
            "certificateUnit": "证书单位",
            "instrumentName": "仪器名称",
            "serialNumber": "出厂编号",
            "assetNumber": "管理编号",
            "calibrationDate": "校准日期",
            "certificate": "证书编号"
        }

        for index, row in tqdm(data_frame.iterrows(), total=len(data_frame), desc="生成二维码"):
            data = {k: row[v] for k, v in column_mapping.items() if pd.notna(row[v]) and row[v] != ""}
            certificate_number = row["证书编号"]
            generate_hongchuang2(data, f"style2_qrcodes/qrcode_{certificate_number}.png")

    if choice == '3':
        os.makedirs("style3_qrcodes", exist_ok=True)

        column_mapping = {
            "certificateUnit": "证书单位",
            "certificateNumber": "证书编号",
            "certificateType": "证书类型",
            "instrumentName": "仪器名称",
            "model": "规格型号",
            "serialNumber": "出厂编号",
            "assetNumber": "资产编号",
            "manufacturer": "制造厂商",
            "calibrationDate": "检/校日期",
            "calibrationPersonnel": "校准/检定员"
        }

        for index, row in tqdm(data_frame.iterrows(), total=len(data_frame), desc="生成二维码"):
            data = {k: row[v] for k, v in column_mapping.items() if pd.notna(row[v]) and row[v] != ""}
            certificate_number = row["证书编号"]
            generate_hongchuang3(data, f"style3_qrcodes/qrcode_{certificate_number}.png")

    if choice == '4':
        os.makedirs("style4_qrcodes", exist_ok=True)

        column_mapping = {
            "company": "公司名称",
            "device": "设备名称",
            "serial": "出厂编号",
            "management": "管理编号",
            "calibration": "检/校日期",
            "certificate": "证书编号"
        }

        for index, row in tqdm(data_frame.iterrows(), total=len(data_frame), desc="生成二维码"):
            data = {k: row[v] for k, v in column_mapping.items() if pd.notna(row[v]) and row[v] != ""}
            certificate_number = row["证书编号"]
            generate_hongchuang4(data, f"style4_qrcodes/qrcode_{certificate_number}.png")

    print("二维码生成结束!")
    input("按任意键退出...")