hf = input("Hours:")
rf = input("rate:")
hrs = float(hf)
rt = float(rf)

def computepay(hrs, rt):
    if (hrs > 40):
        a = 40 * rt + (hrs - 40) * rt * 1.5
    else:
        a = hrs + rt
    return a

p = computepay(hrs,rt)
print(p)
