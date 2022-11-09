# mq2_2 LPG
__state['rules']['gas_outbox'] = 0

VALUE = __state['data']['mq2_2_LPG']
THRESHOLD = 200

if (VALUE > THRESHOLD):
    __state['rules']['gas_outbox'] = 1
    print("\ngas_outbox ppm overload: " + str(VALUE))
else:
    __state['rules']['gas_outbox'] = 0
