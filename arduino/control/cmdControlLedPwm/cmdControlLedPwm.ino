// 定義GPIO腳位
#define LED_RED_PIN 2
#define LED_YELLOW_PIN 3
#define LED_GREEN_PIN 4

char char_from_read;          // 儲存從 Serial 讀取的字元
String string_from_char = ""; // 由讀取的字元組成的字串
int loop_delay = 50;          // 每次迴圈間隔時間
int pwm = 0;                  // PWM輸出

bool fade_flag_red = false;
bool fade_flag_yellow = false;
bool fade_flag_green = false;

int brightness_red = 0; // LED亮度變數
int fadeAmount_red = 5; //亮度變化變數
int brightness_yellow = 0;
int fadeAmount_yellow = 5;
int brightness_green = 0;
int fadeAmount_green = 5;

// 設定Pico第二個Hardware Serial 輸出腳位，用來跟ESP8266通訊
// 若想直接從Pico原本的USB Serial輸出，將 setup 後面的 Serial2 改成 Serial 便會以預設(USB Serial)輸出
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

            // 判斷字串控制LED亮度
            if (string_from_char.substring(0, 6) == "red on")
            {
                pwm = string_from_char.substring(7).toInt();
                analogWrite(LED_RED_PIN, pwm);
            }
            else if (string_from_char == "red off")
            {
                brightness_red = 0;
                analogWrite(LED_RED_PIN, LOW);
            }
            else if (string_from_char.substring(0, 9) == "yellow on")
            {
                pwm = string_from_char.substring(10).toInt();
                analogWrite(LED_YELLOW_PIN, pwm);
            }
            else if (string_from_char == "yellow off")
            {
                brightness_yellow = 0;
                analogWrite(LED_YELLOW_PIN, LOW);
            }
            else if (string_from_char.substring(0, 8) == "green on")
            {
                pwm = string_from_char.substring(9).toInt();
                analogWrite(LED_GREEN_PIN, pwm);
            }
            else if (string_from_char == "green off")
            {
                brightness_green = 0;
                analogWrite(LED_GREEN_PIN, LOW);
            }
            else if (string_from_char == "red fade on")
            {
                fade_flag_red = true;
            }
            else if (string_from_char == "red fade off")
            {
                fade_flag_red = false;
            }
            else if (string_from_char == "yellow fade on")
            {
                fade_flag_yellow = true;
            }
            else if (string_from_char == "yellow fade off")
            {
                fade_flag_yellow = false;
            }
            else if (string_from_char == "green fade on")
            {
                fade_flag_green = true;
            }
            else if (string_from_char == "green fade off")
            {
                fade_flag_green = false;
            }

            string_from_char = ""; // 釋放 string_from_char 記憶體
        }
    }

    if (fade_flag_red)
    {
        analogWrite(LED_RED_PIN, brightness_red);
        brightness_red += fadeAmount_red;
        if (brightness_red <= 0 || brightness_red >= 255)
        {
            fadeAmount_red = -fadeAmount_red;
        }
    }

    if (fade_flag_yellow)
    {
        analogWrite(LED_YELLOW_PIN, brightness_yellow);
        brightness_yellow += fadeAmount_yellow;
        if (brightness_yellow <= 0 || brightness_yellow >= 255)
        {
            fadeAmount_yellow = -fadeAmount_yellow;
        }
    }

    if (fade_flag_green)
    {
        analogWrite(LED_GREEN_PIN, brightness_green);
        brightness_green += fadeAmount_green;
        if (brightness_green <= 0 || brightness_green >= 255)
        {
            fadeAmount_green = -fadeAmount_green;
        }
    }

    string_from_char = ""; // 釋放 string_from_char 記憶體
    delay(loop_delay);     // 等待下一次執行
}