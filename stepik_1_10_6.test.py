from stepik_1_10_6 import main

result = main(2000)
assert result == "Високосный", "result should be 'Високосный' with value 2000"
result = main(2001)
assert result == "Обычный", "result should be 'Обычный' with value 2001"
