def plas(a, b):
	return (a + b)
def sum(a, b):
	return a - b
def mult(a, b):
	return a * b
def div(a, b):
	return a / b
def powr(a, b):
	return pow(a,  b)

nam_1 = float(input("plesse intre frste namber: "))
oprator = input("enter oprator: ")
nam_2 = float(input("plesse intre secnde namber: "))

if (oprator == '+' ):
	print(plas(nam_1, nam_2))
elif (oprator == '-' ):
	print(sum(nam_1, nam_2))
elif (oprator == '*' ):
	print(mult(nam_1, nam_2))
elif (oprator == '/' ):
	print(div(nam_1, nam_2))
elif (oprator == '^'):
	print(pow(nam_1, nam_2))
else : print("eror")
