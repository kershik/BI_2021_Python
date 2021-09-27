
amount = int(input("Amount:"))
from_unit = input("From (s, min, h, d, wk):")
to_unit = input("To (s, min, h, d, wk):")

s = {
    "s": lambda amount: amount,
    "min": lambda amount: amount/60,
    "h": lambda amount: amount/3600,
    "d": lambda amount: amount/(3600*24),
    "wk": lambda amount: amount/(3600*24*7) 
}

min = {
    "s": lambda amount: amount*60,
    "min": lambda amount: amount,
    "h": lambda amount: amount/60,
    "d": lambda amount: amount/(60*24),
    "wk": lambda amount: amount/(60*24*7)
}

h = {
    "s": lambda amount: amount*3600,
    "min": lambda amount: amount*60,
    "h": lambda amount: amount,
    "d": lambda amount: amount/24,
    "wk": lambda amount: amount/(24*7) 
}

d = {
    "s": lambda amount: amount*3600*24,
    "min": lambda amount: amount*60*24,
    "h": lambda amount: amount*24,
    "d": lambda amount: amount,
    "wk": lambda amount: amount/7 
}

wk = {
    "s": lambda amount: amount*3600*24*7,
    "min": lambda amount: amount*60*24*7,
    "h": lambda amount: amount*24*7,
    "d": lambda amount: amount*7,
    "wk": lambda amount: amount
}

from_unit_dict = {
    "s": s,
    "min": min,
    "h": h,
    "d": d,
    "wk": wk
}
 

print(from_unit_dict[from_unit][to_unit](amount))
