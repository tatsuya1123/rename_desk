import tkinter as tk
from tkinter import filedialog
import os

def select_folders():
    root = tk.Tk()
    root.withdraw()

    folder1 = filedialog.askdirectory(title='Select Folder 1')
    folder2 = filedialog.askdirectory(title='Select Folder 2')

    print('Folder 1:', folder1)
    print('Folder 2:', folder2)

    # 選択したフォルダを処理する操作をここに追加する
    # フォルダ内のファイルリストを取得
    files1 = os.listdir(folder1)
    files2 = os.listdir(folder2)
    print(len(files1))
    print(len(files2))

    # ファイル数が異なる場合は処理を終了
    if len(files1) != len(files2):
        print('Error: ファイル数が一致しません')
        return

    # ファイル数が同じであれば、ファイル名を一致させる
    for file1, file2 in zip(files1, files2):
        print("okokokf" + file1)
        file1_name = os.path.basename(file1)
        file2_name, _ = os.path.splitext(file2)

        print("-----------------------------")
        file1_path = os.path.join(folder1, file1)
        print(file1_path)
        file2_path = os.path.join(folder2, file2)
        print(file2_path)
        print("------------------------------")
        new_file_path = os.path.join(folder2, file1_name)
        print(new_file_path)
        os.rename(file2_path, new_file_path)

    print('ファイル名を一致させました')

select_folders()