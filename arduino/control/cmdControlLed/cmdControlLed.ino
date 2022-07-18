// 定義GPIO腳位
#define LED_RED_PIN 2
#define LED_YELLOW_PIN 3
#define LED_GREEN_PIN 4

char char_from_read;          // 儲存從 Serial 讀取的字元
String string_from_char = ""; // 由讀取的字元組成的字串
int loop_delay = 300;         // 每次迴圈間隔時間

// 設定Pico第二個 Hardware Serial 通訊腳位，用來跟ESP8266通訊
// 若想直接從Pico原本的 USB Serial 通訊，將 setup 後面的 Serial2 改成 Serial 便會以預設(USB Serial)通訊
UART Serial2(0, 1, NC, NC);

void setup()
{
    Serial2.begin(115200);        // 設定 baud
    pinMode(LED_RED_PIN, OUTPUT); // 設定 LED_RED_PIN 為輸出腳位
    while (Serial2.read() >= 0)   // 初始化
    {
    }
    Serial2.setTimeout(50); // 設定 Serial 最大等待時間(毫秒)
}

void loop()
{
    // 當 Serial 有輸入資料時不斷執行
    while (Serial2.available() > 0)
    {
        // 從 Serial 讀取輸入字元
        char_from_read = Serial2.read();

        if (char_from_read != '\n' && char_from_read != '\r')
        {
            // 未遇到換行符號前，將讀取的字元加入到字串中
            string_from_char += char_from_read;
        }
        else
        {
            // string_from_char 為輸入的完整字串
            Serial2.println(string_from_char);

            // 判斷字串控制LED開關
            if (string_from_char == "red on")
            {
                digitalWrite(LED_RED_PIN, HIGH);
            }
            else if (string_from_char == "red off")
            {
                digitalWrite(LED_RED_PIN, LOW);
            }
            else if (string_from_char == "yellow on")
            {
                digitalWrite(LED_YELLOW_PIN, HIGH);
            }
            else if (string_from_char == "yellow off")
            {
                digitalWrite(LED_YELLOW_PIN, LOW);
            }
            else if (string_from_char == "green on")
            {
                digitalWrite(LED_GREEN_PIN, HIGH);
            }
            else if (string_from_char == "green off")
            {
                digitalWrite(LED_GREEN_PIN, LOW);
            }
            string_from_char = ""; // 釋放 string_from_char 記憶體
        }
    }
    string_from_char = ""; // 釋放 string_from_char 記憶體
    delay(loop_delay);     // 等待下一次執行
}