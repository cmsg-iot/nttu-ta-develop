# 將 ADC 量測到的數值轉換為壓力值，依據不同感測器感測範圍輸入對應 kpa，單位 kg/cm2
# 例： 1 mpa = 1000 kpa = 10 kg/cm2
def transferPressureFromADC(adc, kpa):
    baseVoltage = 3.3
    voltage = ((adc / 65535) * baseVoltage) - 0.5
    if voltage < 0:
        voltage = 0
    ratioOfSensorRange = kpa / 400
    result = voltage * ratioOfSensorRange
    result = float(f"{result:.2f}")
    return result


# 瓦斯洩漏的警報狀態
__state['rules']['gas_leak'] = 0

# 電動閥狀態
valveState = __state['data']['valveState']

# 進口壓力感測(電動閥 -> 調壓閥)
p_in = transferPressureFromADC(__state['data']['pressure_in'], 1000)

# 出口壓力感測(調壓閥 -> 瓦斯爐)
p_out = transferPressureFromADC(__state['data']['pressure_out'], 200)

# 進口壓力閾值
P_IN_THRESHOLD = 0.15

# 出口壓力閾值
P_OUT_THRESHOLD = 0.05

print(p_in, p_out)

# 預設管線中已有瓦斯的情況下，且電動閥是關閉的狀況下
# 當出口端慢慢漏氣至閾值以下，且調壓閥出口壓力低於正常值時，表示管線發生洩漏
if (valveState == 0) and (p_in <= P_IN_THRESHOLD) and (p_out < P_OUT_THRESHOLD):
    __state['rules']['gas_leak'] = 1
    print("\ngas leak!", "p_in: " + str(p_in), "p_out: " + str(p_out))
else:
    __state['rules']['gas_leak'] = 0
