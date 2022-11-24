# mq7 CarbonMonoxide

# 表示箱外一氧化碳濃度的警報狀態
__state['rules']['co_outbox'] = 0

# 箱內 mq7 的一氧化碳數值
VALUE = __state['data']['mq7']

# 觸發警報的閾值
THRESHOLD = 100

# 當偵測數值大於閾值時切換警報狀態
if (VALUE > THRESHOLD):
    __state['rules']['co_outbox'] = 1
    print("\nco_outbox ppm overload: " + str(VALUE))
else:
    __state['rules']['co_outbox'] = 0
