# mq7 CarbonMonoxide
__state['rules']['co_outbox'] = 0

VALUE = __state['data']['mq7']
THRESHOLD = 200

if (VALUE > THRESHOLD):
    __state['rules']['co_outbox'] = 1
    print("\nco_outbox ppm overload: " + str(VALUE))
else:
    __state['rules']['co_outbox'] = 0
