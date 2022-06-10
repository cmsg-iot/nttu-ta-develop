// 引入所需套件
#include <ArduinoJson.h>

// 設定Pico第二個Hardware Serial 輸出腳位，用來跟ESP8266通訊
UART Serial2(0, 1, NC, NC);

// 定義json物件，長度為1024byte
DynamicJsonDocument data(1024);

// 板上LED燈狀態
bool blinkState = false;

void setup()
{
    Serial2.begin(115200); // 設定baud
    pinMode(A0, INPUT);    // 設定腳位A0為輸入腳位
}

void loop()
{
    data["gas"] = analogRead(A0);       // 讀取A0類比輸入值，存放到 gas 這個 key 中
    serializeJsonPretty(data, Serial2); // 顯示 data 於 Serial Monitor
    data.clear();                       // 釋放 data 記憶體

    blinkState = !blinkState;              // 切換LED燈狀態
    digitalWrite(LED_BUILTIN, blinkState); // LED燈閃爍
    delay(100);                            // 等待100毫秒
}