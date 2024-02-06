fh = open("output50.txt", "w")

fh.write("# conversion of celcius to fahrenhit" + "\n")

a = int(input("Enter the value in degree celcius :"))

fh.write(str(a) + "c" + "\n")

f = 9 * (a / 5) + 32

fh.write(str(f) + "F"+'\n')


fh.write("# conversion of celcius to fernhit" + "\n")

b = int(input("Enter the value in degree fahrenhit :"))

cl = (b - 32) * (5 / 9)

fh.write(str(b) + "f" + "\n")

fh.write(str(cl) + "c" + "\n")

fh.close