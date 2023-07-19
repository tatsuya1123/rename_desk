import os

def rename_files_to_match(folder1, folder2):
    # フォルダ内のファイルリストを取得
    files1 = os.listdir(folder1)
    files2 = os.listdir(folder2)

    # ファイル数が異なる場合は処理を終了
    if len(files1) != len(files2):
        print('Error: ファイル数が一致しません')
        return

    # ファイル数が同じであれば、ファイル名を一致させる
    for file1, file2 in zip(files1, files2):
        file1_path = os.path.join(folder1, file1)
        file2_path = os.path.join(folder2, file2)
        os.rename(file2_path, file1_path)

    print('ファイル名を一致させました')

# 使用例
folder1 = 'path/to/folder1'
folder2 = 'path/to/folder2'
rename_files_to_match(folder1, folder2)