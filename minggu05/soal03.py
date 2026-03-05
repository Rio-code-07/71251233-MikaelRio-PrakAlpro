celcius_fahrenheit = lambda  suhu : (9/5) * suhu + 32
celcius_reamur = lambda suhu : 0.8 * suhu

suhu1 = 100
print(f"Input C = {suhu1}. Output F = {celcius_fahrenheit(suhu1):.0f}.")

suhu2 = 80
print(f"Input C = {suhu2}. Output R = {celcius_reamur(suhu2):.0f}.")

suhu3 = 0 
print(f"Input = {suhu3}. Output F = {celcius_fahrenheit(suhu3):.0f}.")