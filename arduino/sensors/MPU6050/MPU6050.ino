#include <ArduinoJson.h>
#include "I2Cdev.h"
#include "MPU6050.h"

// Arduino Wire library is required if I2Cdev I2CDEV_ARDUINO_WIRE implementation
// is used in I2Cdev.h
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
#include "Wire.h"
#endif

// 建立 MPU6050 物件
MPU6050 accelgyro;

// int16_t(typedef signed short) 表示有號的短整數，範圍介於 -32,768 ~ 32,768
int16_t ax, ay, az;
int16_t gx, gy, gz;

// 設定Pico第二個Hardware Serial 輸出腳位，用來跟ESP8266通訊
UART Serial2(0, 1, NC, NC);

// 定義json物件，長度為1024byte
DynamicJsonDocument data(1024);

// 取消註解 "OUTPUT_READABLE_ACCELGYRO"，能讓輸出的資料變成字串顯示，方便閱讀，不便於格式化，且速度較慢，建議在測試顯示資料中使用
#define OUTPUT_READABLE_ACCELGYRO

// 取消註解 "OUTPUT_BINARY_ACCELGYRO"，能讓輸出的資料變成Binary， 幾乎無法閱讀，但方便格式化，且速度非常快，建議在實際應用時使用
//#define OUTPUT_BINARY_ACCELGYRO

// 板上LED燈狀態
bool blinkState = false;

void setup()
{
// join I2C bus (I2Cdev library doesn't do this automatically)
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    Wire.begin();
#elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
    Fastwire::setup(400, true);
#endif

    Serial2.begin(38400); // 設定baud

    // 初始化裝置
    Serial2.println("Initializing I2C devices...");
    accelgyro.initialize();

    // 驗證連接
    Serial2.println("Testing device connections...");
    Serial2.println(accelgyro.testConnection() ? "MPU6050 connection successful" : "MPU6050 connection failed");

    // 使用以下程式碼可以調整 accel/gyro 的偏移量
    /*
    Serial.println("Updating internal sensor offsets...");
    // -76	-2359	1688	0	0	0
    Serial.print(accelgyro.getXAccelOffset()); Serial.print("\t"); // -76
    Serial.print(accelgyro.getYAccelOffset()); Serial.print("\t"); // -2359
    Serial.print(accelgyro.getZAccelOffset()); Serial.print("\t"); // 1688
    Serial.print(accelgyro.getXGyroOffset()); Serial.print("\t"); // 0
    Serial.print(accelgyro.getYGyroOffset()); Serial.print("\t"); // 0
    Serial.print(accelgyro.getZGyroOffset()); Serial.print("\t"); // 0
    Serial.print("\n");
    accelgyro.setXGyroOffset(220);
    accelgyro.setYGyroOffset(76);
    accelgyro.setZGyroOffset(-85);
    Serial.print(accelgyro.getXAccelOffset()); Serial.print("\t"); // -76
    Serial.print(accelgyro.getYAccelOffset()); Serial.print("\t"); // -2359
    Serial.print(accelgyro.getZAccelOffset()); Serial.print("\t"); // 1688
    Serial.print(accelgyro.getXGyroOffset()); Serial.print("\t"); // 0
    Serial.print(accelgyro.getYGyroOffset()); Serial.print("\t"); // 0
    Serial.print(accelgyro.getZGyroOffset()); Serial.print("\t"); // 0
    Serial.print("\n");
    */
}

void loop()
{
    // 讀取原始 accel/gyro 感測資料
    accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

    // 也能使用以下程式分別取得 accel/gyro 資料
    // accelgyro.getAcceleration(&ax, &ay, &az);
    // accelgyro.getRotation(&gx, &gy, &gz);

// 以字串輸出於 Serial Monitor(JSON格式)
#ifdef OUTPUT_READABLE_ACCELGYRO
    // display tab-separated accel/gyro x/y/z values
    //        Serial2.print("a/g:\t");
    //        Serial2.print(ax); Serial2.print("\t");
    //        Serial2.print(ay); Serial2.print("\t");
    //        Serial2.print(az); Serial2.print("\t");
    //        Serial2.print(gx); Serial2.print("\t");
    //        Serial2.print(gy); Serial2.print("\t");
    //        Serial2.println(gz);
    data["ax"] = ax;
    data["ay"] = ay;
    data["az"] = az;
    data["gx"] = gx;
    data["gy"] = gy;
    data["gz"] = gz;
    //        serializeJson(data, Serial2);
    serializeJsonPretty(data, Serial2);
#endif

// 以 Binary 輸出
#ifdef OUTPUT_BINARY_ACCELGYRO
    Serial.write((uint8_t)(ax >> 8));
    Serial.write((uint8_t)(ax & 0xFF));
    Serial.write((uint8_t)(ay >> 8));
    Serial.write((uint8_t)(ay & 0xFF));
    Serial.write((uint8_t)(az >> 8));
    Serial.write((uint8_t)(az & 0xFF));
    Serial.write((uint8_t)(gx >> 8));
    Serial.write((uint8_t)(gx & 0xFF));
    Serial.write((uint8_t)(gy >> 8));
    Serial.write((uint8_t)(gy & 0xFF));
    Serial.write((uint8_t)(gz >> 8));
    Serial.write((uint8_t)(gz & 0xFF));
#endif

    blinkState = !blinkState;              // 切換LED燈狀態
    digitalWrite(LED_BUILTIN, blinkState); // LED燈閃爍
    delay(300);                            // 等待300毫秒
}