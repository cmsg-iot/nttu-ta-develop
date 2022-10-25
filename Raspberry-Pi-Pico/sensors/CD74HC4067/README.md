# CD74HC4067 16 路多工類比轉數位模組

以 4 個 GPIO 選擇取得 16 個 ADC 輸入訊號

## Usage

- 將 S0~S3 連接至 pi pico 上的 4 個 GPIO (2,3,4,5 除外，這些腳位有時會有額外輸出)
- 將 SIG 連接至 pi pico 上的 ADC(範例使用 ADC0)
- 從 pi pico 上供應 3.3V 及 GND 至模組
- 執行 main.py
- 測試拉一條 3.3V 接上模組其中 1 個輸入，檢查輸出為 65535 表示正常
