import os
import pandas as pd


def get_file_list(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append([root, file])
    return file_list


def save_to_excel(file_list, excel_file):
    df = pd.DataFrame(file_list, columns=["Папка", "Имя файла"])
    df["Расширение файла"] = df["Имя файла"].str.split(".", expand=True)[1]
    df.index += 1
    df.to_excel(excel_file, index_label="Номер строки")

try:
    file_list = get_file_list(os.getcwd())
    save_to_excel(file_list, "result.xlsx")
except Exception as ex:
    print(ex)
