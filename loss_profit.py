bp=float(input("enter your buying price = "))
sp=float(input("enter your sold price = "))
profit=sp-bp
loss=bp-sp
if bp>sp:
    print("you are in loss")
    print("loss=",loss)
else:
    print ("you are in profit")
    print("profit=",profit)