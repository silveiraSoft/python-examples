#https://www.geeksforgeeks.org/python-how-to-get-function-name/

def fistFuntion():
	print("Called to function: fistFuntion:" + fistFuntion.__name__)

if __name__ == '__main__':
    print("Called library directly")
    fistFuntion()
    
if __name__ == 'mylibrary':
    print("fistFuntion was called, used through another archive")
    fistFuntion()