from stepik_1_12_2 import intervals

assert intervals(-12), "-12 should be True"
assert not intervals(-15), "-15 should be False"
assert intervals(11), "11 should be True"
assert intervals(12), "12 should be True"
assert not intervals(14), "14 should be False"
assert not intervals(17), "17 should be False"
assert intervals(19), "19 should be True"
assert intervals(20), "20 should be True"
