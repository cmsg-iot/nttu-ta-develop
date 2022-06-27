# 判斷輸入字串控制 LED 開關

在 `Serial Monitor` 中輸入文字，由程式判斷文字來控制 LED 的開關

## Usage

- 開啟 `cmdControlLed.ino`， 選擇 `Arduino Mbed OS RP2040 Boards` 中的 `Raspberry Pi Pico` 進行燒錄
- 將 `USB to TTL模組` 插入至電腦中的 USB，模組上的 `TX RX` 與 `Raspberry Pi Pico` 上的 `GP1(RX) GP0(TX)` 連接(TX 接 RX，RX 接 TX)
- `Tool/Port(序列阜)` 選擇插入的 USB，開啟 `Serial Monitor(序列阜監控視窗)` 輸入任意字串，觀察結果
