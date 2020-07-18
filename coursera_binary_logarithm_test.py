from coursera_binary_logarithm import binary_logarithm

assert binary_logarithm(0) == 0, "При значении 0 должно выводиться 0, т.к. 2**0 >= 0"
assert binary_logarithm(1) == 0, "При значении 1 должно выводиться 0, т.к. 2**0 >= 1"
assert binary_logarithm(2) == 1, "При значении 2 должно выводиться 1, т.к. 2**1 >= 2"
assert binary_logarithm(3) == 2, "При значении 3 должно выводиться 2, т.к. 2**2 >= 1"

