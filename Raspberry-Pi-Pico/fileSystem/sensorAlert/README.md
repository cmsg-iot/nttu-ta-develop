# 感測器警報

設定目標感測腳位閾值，超過時啟動LED燈或蜂鳴器，並紀錄一筆Log資料(每10秒一次)，Log中包含狀況描述

在 Pi Pico 中，其 ADC 為 12bit, 輸出範圍應為2的12次方 0~ 4095，而在 micropython 中使用 ADC().read_u16()讀取ADC值時，已經將其轉換為 0 ~ 65535, 故以micropython輸出為主，0 ~ 65535 表示 0 ~ 3.3V。


# 參考資料
- https://how2electronics.com/how-to-use-adc-in-raspberry-pi-pico-adc-example-code/
- http://wiki.csie.ncku.edu.tw/embedded/ADC