# mq2 LPG
__state['rules']['gas_inbox'] = 0

VALUE = __state['data']['mq2_LPG']
THRESHOLD = 200

if (VALUE > THRESHOLD):
    __state['rules']['gas_inbox'] = 1
    print("\ngas_inbox ppm overload: " + str(VALUE))
else:
    __state['rules']['gas_inbox'] = 0
