__state['rules']['gas_leak'] = 0

p_in = pressure_in.getValue()
p_out = pressure_out.getValue()

if p_in < 10000 == 1 or p_out > p_in:
    __state['rules']['gas_leak'] = 1
    print("gas leak!")
else:
    print("gas normal")
