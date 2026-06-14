class ComplexNumber:
    def __init__(self, real=0.0,imag=0.0):
        self.imag = imag
        self.real = real

    def __str__(self):
        if (self.real == 0):
            return f"{self.imag}i"
        elif (self.imag < 0):
            s = f"({self.real}{self.imag}i)"
        else: 
            s = f"({self.real}+{self.imag}i)"
        return s
    
    def __add__(self,other):
        print("I perform additon!")
        resultReal = 0
        resultImag = 0

        resultReal = self.real + other.real
        resultImag = self.imag + other.imag

        ans = ComplexNumber(resultReal,resultImag)
        return ans
    
    def __sub__(self, other):
        print("I perform Subtraction!")
        resultReal = 0
        resultImag = 0

        resultReal = self.real - other.real
        resultImag = self.imag - other.imag

        ans = ComplexNumber(resultReal,resultImag)
        return ans
    
    def __mul__(self, other):
        print("I perform Multiplication!")
        resulReal = 0
        resultImag = 0

        resultReal = self.real * other.real - self.imag * other.imag
        resultImag = self.real * other.imag + other.real * self.imag

        ans = ComplexNumber(resultReal,resultImag)
        return ans
    
    def __truediv__(self, other):
        print("I perform Division!")
        resultReal = 0
        resultImag = 0

        den = other.real**2 + other.imag**2
        ans = self * ComplexNumber((other.real)/den,(-1*other.imag)/den)
        return ans
    
    def __eq__(self, other):
        return (self.real == other.real) and (self.imag == other.imag)

    # def __neq__(self,other):
    #     return (self.real != other.real) and (self.imag != other.imag)

    def Conjugate(self):
        imag  = - self.imag
        if imag < 0:
            return f"({self.real}{imag}i)"
        else:
            return (f"({self.real}+{imag}i)")

ComNum = ComplexNumber(1,-5)
print((ComNum.real,ComNum.imag)) 
print(type(ComNum))
print(ComNum)
print(type(ComNum.Conjugate()))
print(ComNum.Conjugate())
ComNum1 = ComplexNumber(3,4)
ComNum2 = ComplexNumber(3,4)
print(ComNum1+ComNum2)
print(ComNum1-ComNum2)
print(ComNum1*ComNum2)
print((ComNum1/ComNum2))
print((ComNum1==ComNum2))
print(ComNum1!=ComNum2)
