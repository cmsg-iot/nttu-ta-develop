# 在 SerialMonitor 輸入字串並得到 Echo 回覆

在 `SerialMonitor` 輸入任意字串，`SerialMonitor` 回傳同樣的字串

## Usage

- 開啟 `sendSerialGetEcho.ino`， `Tool(工具)/Board(開發板)` 選擇 `Arduino Mbed OS RP2040 Boards` 中的 `Raspberry Pi Pico` 進行燒錄
- 將 `USB to TTL模組` 插入至電腦中的 USB，模組上的 `TX RX` 與 `Raspberry Pi Pico` 上的 `GP1(RX) GP0(TX)` 連接(TX 接 RX，RX 接 TX)
- `Tool/Port(序列阜)` 選擇插入的 USB，開啟 `Serial Monitor(序列阜監控視窗)` 輸入任意字串，觀察結果
