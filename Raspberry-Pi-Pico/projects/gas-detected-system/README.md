# 智能燃器系統

感測瓦斯桶重量、空氣溫度濕度、瓦斯洩漏偵測、管線洩漏偵測

## 安裝

1. 將 [micropython](./micropython/) 中的檔案上傳至 `Raspberry Pi Pico` 中

2. 依照下圖線路配置元件後執行 ![gas_sys](./gas_system_bb.png)

3. 開啟網頁編輯器 http://web.sgiot.com.tw

4. 參考 [網頁參數檔](https://github.com/cmsg-iot/cmsg-iot.github.io/tree/main/json) 將 [gas-system.json](./web/gas-system.json) 檔案匯入並開啟

5. 連上 ESP8266 Wi-Fi (預設 wifi 名稱 NTTU_AP)

6. 使用 `Create WS`，輸入 `10.10.10.10` 位址後，待左上狀態顯示綠燈表示已連接

7. 點擊 `RUN` 按鈕即可看到完整系統網頁

## 腳位配置一覽

|          名稱           |                      對應腳位                      |
| :---------------------: | :------------------------------------------------: |
|     UART to ESP8266     |              TX= `GPIO0`, RX= `GPIO1`              |
|    重量感測器(hx711)    |          d_out= `GPIO4`, pd_sck= `GPIO5`           |
|    16 路 ADC 多工器     | s0= `GPIO6`, s1= `GPIO7`, s2= `GPIO8`, s3= `GPIO9` |
|        磁簧開關         |                      `GPIO10`                      |
|         蜂鳴器          |                      `GPIO11`                      |
|         加熱器          |                      `GPIO12`                      |
|       開啟 電動閥       |                      `GPIO13`                      |
|       關閉 電動閥       |                      `GPIO14`                      |
|   空氣溫濕度(AM2320)    |            scl= `GPIO17` sda= `GPIO16`             |
|    一氧化碳偵測(MQ7)    |               ADC 多工器 channel `0`               |
| 可燃氣體偵測-箱內 (MQ2) |               ADC 多工器 channel `1`               |
| 可燃氣體偵測-箱外 (MQ2) |               ADC 多工器 channel `2`               |
|        進口壓力         |               ADC 多工器 channel `3`               |
|        出口壓力         |               ADC 多工器 channel `4`               |
