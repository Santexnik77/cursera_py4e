hrs = input("Enter Hours:")
rt = input("Enter rate:")
hf = float(hrs)
rf = float(rt)
if (hf > 40):
    pay = 40 * rf + (hf - 40) * rf * 1.5
else:
    pay = hf * rf
print(pay) 
