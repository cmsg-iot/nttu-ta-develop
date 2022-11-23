ruleStates = __state['rules']
threshOfAlert = 0

for v in ruleStates:
    threshOfAlert += ruleStates[v]

print(threshOfAlert)

if threshOfAlert > 0:
    buzzer.setValue(1)
else:
    buzzer.setValue(0)
