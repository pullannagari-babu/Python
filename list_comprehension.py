frd = input ("ENter the input")

frds = ["Rolf","Deepa","Krishna"]

frds_low = [name.lower() for name in frds]

if frd.lower() in frds_low:
    print(f"{frd.title()} is one")
