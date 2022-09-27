# 在 Thonny 的 Shell 中練習以下程式，並觀察結果

import os # 引入 os 模組

# 韌體版本資訊
os.uname()

# 取得檔案系統詳細資訊
os.statvfs('/')

# 取得單一檔案或資料夾全部詳細資訊, 以 main.py 為例
os.stat('main.py')

# 檔案型態，16384 表示資料夾，32768 表示檔案
os.stat('main.py')[0]

# 檔案內容大小，單位為 byte
os.stat('main.py')[6]

# 檔案修改UTC時間
os.stat('main.py')[7]
os.stat('main.py')[8]
os.stat('main.py')[9]

# 取得目前所在路徑
# 輸出 '/'
os.getcwd()

# ----------------- #

# 下面有操作新增或移除時，可至 File -> Open -> Raspberry Pi Pico 查看檔案狀態

# 建立新資料夾
os.mkdir('newdirectory')

# 切換至其他路徑並再次查看目前所在路徑
os.chdir('newdirectory')

# 輸出 '/newdirectory'
os.getcwd()

# 返回上一層資料夾
os.chdir('..')

# 輸出 '/'
os.getcwd()

# 取得目前所在路徑底下所有檔案及資料夾名稱
# 輸出 ['main.py', 'newdirectory']
os.listdir()

# 修改檔案/資料夾名稱
os.rename('newdirectory','dir')

# 輸出 ['main.py', 'dir']
os.listdir()

# 刪除資料夾
os.rmdir('dir')

# 輸出 ['main.py']
os.listdir()

# 新增檔案, 格式為 open(檔案名稱,打開方式), w 表示 write
f = open('hello.txt','w')

# 寫入文字
f.write('Hello, world!')

# 關閉檔案
f.close()

# 查看目前路徑，多出 hello.txt 檔案
# 輸出 ['hello.txt', 'main.py']
os.listdir()

# 讀取檔案內容, 使用 read 方法打開
f = open('hello.txt','r')

# 取得檔案內容
# 輸出 'Hello, world!'
f.read()

# 關閉檔案
f.close()