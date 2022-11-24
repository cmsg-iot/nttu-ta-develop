ruleStates = __state['rules']

# 警報數量閾值
threshOfAlert = 0

for v in ruleStates:
    threshOfAlert += ruleStates[v]

print(threshOfAlert)

# 當有任一個警報狀態為1時， 開啟蜂鳴器
if threshOfAlert > 0:
    buzzer.setValue(1)
else:
    buzzer.setValue(0)
