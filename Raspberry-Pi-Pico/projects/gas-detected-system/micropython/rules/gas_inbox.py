# mq2 LPG

# 表示箱內瓦斯濃度的警報狀態
__state['rules']['gas_inbox'] = 0

# 箱內 mq2 的 LPG 數值
VALUE = __state['data']['mq2_LPG']

# 觸發警報的閾值
THRESHOLD = 100

# 當偵測數值大於閾值時切換警報狀態
if (VALUE > THRESHOLD):
    __state['rules']['gas_inbox'] = 1
    print("\ngas_inbox ppm overload: " + str(VALUE))
else:
    __state['rules']['gas_inbox'] = 0
