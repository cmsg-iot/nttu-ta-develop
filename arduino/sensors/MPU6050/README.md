# MPU6050

使用 Pico 讀取 MPU6050 資料，以 JSON 格式輸出於 `Serial Monitor` 中

## Usage

- 下載 [jrowberg/i2cdevlib](https://github.com/jrowberg/i2cdevlib)，解壓縮後複製 `I2Cdev` 與 `MPU6050` 資料夾放在 `Arduino/libraries` 底下
- 下載 Arduino Json Library [bblanchon/ArduinoJson](https://github.com/bblanchon/ArduinoJson)，解壓縮後放在 `Arduino/libraries` 底下
- 開啟 `MPU6050.ino`， 選擇 `Arduino Mbed OS RP2040 Boards` 中的 `Raspberry Pi Pico` 進行燒錄
- 開啟 `Serial Monitor` 觀察輸出數據
