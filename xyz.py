Msg1 = "WeLcOME"
Msg2 = "GUeSTs"
Msg3 = ""

for i in range(0,len(Msg2)+1):
    if Msg1[i] >= "A" and Msg1[i] <= "M":
        Msg3 = Msg3 + Msg1[i]
    elif Msg1[i] >= "N" and Msg1[i] <= "Z":
        Msg3 = Msg3 + Msg2[i]
    else:
        Msg3 = Msg3 + "+___"

print(Msg3)