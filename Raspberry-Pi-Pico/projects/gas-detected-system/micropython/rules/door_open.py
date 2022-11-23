# door state
__state['rules']['door_open'] = 0

VALUE = __state['data']['hall']

if (VALUE == 1):
    __state['rules']['door_open'] = 1
    print("\ndoor are opened!")
else:
    __state['rules']['door_open'] = 0
