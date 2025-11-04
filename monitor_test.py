from monitor import Monitor

m1 = Monitor("Tester", 1920, 1080)
m2 = Monitor("Other Tester", 200, 400)
m3 = Monitor("Identical Tester With a Different Name", 1920, 1080)

assert m1.get_resolution() == (1920, 1080), "get_resolution"
assert m1.get_total_pixels() == 1920 * 1080, "get_total_pixels"
assert m1 != m2, "__eq__ False"
assert m1 == m3, "__eq__ True"
