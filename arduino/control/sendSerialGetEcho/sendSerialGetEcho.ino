char char_from_read;          // 儲存從 Serial 讀取的字元
String string_from_char = ""; // 由讀取的字元組成的字串
int loop_delay = 300;         // 每次迴圈間隔時間

void setup()
{
    Serial.begin(115200);         // 設定 baud
    pinMode(LED_RED_PIN, OUTPUT); // 設定 LED_RED_PIN 為輸出腳位
    while (Serial.read() >= 0)    // 初始化
    {
    }
    Serial.setTimeout(50); // 設定 Serial 最大等待時間(毫秒)
}

void loop()
{
    // 當 Serial 有輸入資料時不斷執行
    while (Serial.available() > 0)
    {
        // 從 Serial 讀取輸入字元
        char_from_read = Serial.read();

        if (char_from_read != '\n' && char_from_read != '\r')
        {
            // 未遇到換行符號前，將讀取的字元加入到字串中
            string_from_char += char_from_read;
        }
        else
        {
            // string_from_char 為輸入的完整字串
            // 印出輸入的字串
            Serial.println(string_from_char);
            string_from_char = ""; // 釋放 string_from_char 記憶體
        }
    }
    string_from_char = ""; // 釋放 string_from_char 記憶體
    delay(loop_delay);     // 等待下一次執行
}