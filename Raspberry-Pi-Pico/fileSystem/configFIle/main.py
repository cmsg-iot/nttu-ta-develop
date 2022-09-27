# 先在 Thonny 中建立新檔案並命名 default.txt,

import os # 引入 os 模組

# 載入預設設定檔內容至 defaultConfig 變數中
f = open('default.txt','r')
defaultConfig = f.read()
f.close()

# 處理換行, tempConfig 內容為 ['bright=50', 'cycle=10']
tempConfig = defaultConfig.split( )

# 重新定義 defaultConfig 為空字典
defaultConfig = {}

# 以 v 表示 tempConfig 中的單一內容
for v in tempConfig:
    # 處理字串，第一次迴圈時 temp 內容為 ['bright','50']
    temp = v.split('=')
    print(temp)
    
    # 將 temp[0] 作為 key, temp[1] 作為值儲存於 defaultConfig 中, 第一次迴圈後內容為 {'bright':'50'} 
    defaultConfig[temp[0]] = temp[1]


# 取得所有設定檔內容
# 輸出 {'bright':'50','cycle':'10'} 
print(defaultConfig)

# 以對應key取得內容
# 輸出 50
print(defaultConfig['bright'])

# 輸出 10
print(defaultConfig['cycle'])
