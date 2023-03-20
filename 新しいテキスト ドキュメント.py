import configparser
import zipfile
import os
import sys

def zipdir(path, zipname):
    config = configparser.ConfigParser()
    config.read('setting.ini')
    password = config.get('Archive', 'password')

    zipf = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file), file, zipfile.ZIP_DEFLATED)
    zipf.setpassword(password.encode())
    zipf.close()

if __name__ == '__main__':
    # コマンドライン引数からフォルダとzipファイル名を取得する
    args = sys.argv
    path = args[1]
    zipname = args[2]
    
    # フォルダをzip圧縮する
    zipdir(path, zipname)
    