// 引入所需套件
#include <AM2320.h>
#include <ArduinoJson.h>

// 建立sensor物件
AM2320 sensor;

// 設定Pico第二個Hardware Serial 輸出腳位，用來跟ESP8266通訊
UART Serial2(0, 1, NC, NC);

// 定義json物件，長度為1024byte
DynamicJsonDocument data(1024);

// 板上LED燈狀態
bool blinkState = false;

void setup()
{
    Serial2.begin(115200); // 設定baud
    sensor.begin();        // sensor 初始化
}

void loop()
{
    // sensor.measure() 代表感測器狀態
    // - true 表示資料完整且獲取成功
    // - false 表示感測器未準備或CRC驗證錯誤
    //   使用 getErrorCode() 檢查錯誤訊息
    if (sensor.measure())
    {
        data["temp"] = round2(sensor.getTemperature()); // 取得溫度數值，存放在 temp 這個 key 中
        data["hum"] = round2(sensor.getHumidity());     // 取得濕度數值，存放在 hum 這個 key 中
        serializeJsonPretty(data, Serial2);             // 顯示 data 於 Serial Monitor
    }
    else
    {                                          // 發生錯誤
        int errorCode = sensor.getErrorCode(); // 錯誤代碼

        switch (errorCode)
        {
        case 1:
            data["error"] = "ERR: Sensor is offline"; // 感測器未準備
            break;
        case 2:
            data["error"] = "ERR: CRC validation failed."; // CRC驗證錯誤
            break;
        }
        serializeJson(data, Serial2); // 顯示 data 於 Serial Monitor
    }
    data.clear(); // 釋放 data 記憶體

    blinkState = !blinkState;              // 切換LED燈狀態
    digitalWrite(LED_BUILTIN, blinkState); // LED燈閃爍
    delay(1000);                           // 等待500毫秒
}

double round2(double value)
{
    return (int)(value * 100 + 0.5) / 100.0;
}