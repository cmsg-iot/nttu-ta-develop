__state['rules']['gas_leak'] = 0

p_in = __state['data']['pressure_in']
p_out = __state['data']['pressure_out']

if p_out > p_in:
    __state['rules']['gas_leak'] = 1
    print("\ngas leak!", "p_in: " + str(p_in), "p_out: " + str(p_out))
else:
    __state['rules']['gas_leak'] = 0
