class ComplexNumber:
    def __init__(self, real=0.0,imag=0.0):
        self.imag = imag
        self.real = real

    def __str__(self):
        str = f"{self.real} + {self.imag}i"
        return str

    def Conjugate(self):
        imag  = self.imag* -1
        print(f"({self.real} + {imag}i)")

ComNum = ComplexNumber(3,5)
ComNum1 = ComNum.Conjugate()
print((ComNum.real,ComNum.imag))
print(ComNum1)