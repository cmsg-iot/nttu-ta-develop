# door state

# 開關門的警報狀態
__state['rules']['door_open'] = 0

# 磁簧開關狀態
VALUE = __state['data']['hall']

# 當磁簧開關分開時，電流經過GPIO，切換警報狀態為1
# 當磁簧開關接觸時，電流接地，切換警報狀態為0
if (VALUE == 1):
    __state['rules']['door_open'] = 1
    print("\ndoor are opened!")
else:
    __state['rules']['door_open'] = 0
