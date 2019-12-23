class Polynomial:

    def __init__(self, *coefficients):
        self.coef = [0]
        if isinstance(coefficients[0], list):
            self.coef=coefficients[0]
        elif isinstance(coefficients[0], dict):
            max_deg=0
            for deg in coefficients[0]:
                if deg>max_deg:
                    max_deg=deg
            self.coef=[0]*(max_deg+1)
            for deg in coefficients[0]:
                self.coef[deg]=coefficients[0][deg]
        elif isinstance(coefficients[0], Polynomial):
            self.coef = coefficients[0].coef
        elif len(coefficients) > 1:
            self.coef= list(coefficients)
        elif isinstance(coefficients[0], int):
            self.coef[0]=coefficients[0]
        while len(self.coef)>1 and self.coef[-1]==0:
            self.coef.pop()
        self.counter = (-1, self.coef[0])


    def __repr__(self):
        outstr = 'Polynomial ['
        for c in self.coef:
            outstr += str(c) + ', '
        return outstr[:-2] + ']'

    def __str__(self):
        outstr = ''
        for i in range(len(self.coef)-1, -1, -1):
            if i>1 and self.coef[i]!=0:
                if outstr=='':
                    outstr += str(self.coef[i])+'x^'+str(i)
                else:
                    if self.coef[i]==1:
                        outstr += ' + ' + 'x^' + str(i)
                    elif self.coef[i] > 0:
                        outstr+=' + '+str(self.coef[i])+'x^'+str(i)
                    elif self.coef[i]==-1:
                        outstr += ' - ' + 'x^' + str(i)
                    else:
                        outstr+=' - '+str(-self.coef[i])+'x^'+str(i)
            if i == 1 and self.coef[i]!=0:
                if outstr == '' :
                    if self.coef[i]==1:
                        outstr='x'
                    else:
                        outstr=str(self.coef[i])+'x'
                else:
                    if self.coef[i] == 1:
                        outstr += ' + ' + 'x'
                    elif self.coef[i] > 0:
                        outstr += ' + ' + str(self.coef[i]) + 'x'
                    elif self.coef[i]==-1:
                        outstr += ' - ' + 'x'
                    else:
                        outstr += ' - ' + str(-self.coef[i]) + 'x'
            if i == 0:
                if outstr=='':
                    outstr=str(self.coef[i])
                elif self.coef[i] > 0:
                    outstr += ' + ' + str(self.coef[i])
                elif self.coef[i] < 0:
                    outstr += ' - ' + str(-self.coef[i])
        return outstr

    def degree(self):
        return len(self.coef)-1

    def __add__(self, other):
        if isinstance(other, int):
            new_coef=self.coef.copy()
            new_coef[0]+=other
            return Polynomial(new_coef)
        if isinstance(other, Polynomial):
            if self.degree()<other.degree():
                new_coef=other.coef.copy()
                for i in range(0, self.degree()+1):
                    new_coef[i]+=self.coef[i]
            else:
                new_coef = self.coef.copy()
                for i in range(0, other.degree() + 1):
                    new_coef[i] += other.coef[i]
            return Polynomial(new_coef)


    def __eq__(self, other):
        ans=1
        if isinstance(other, int):
            if self.degree() == 0 and self.coef[0]==other:
                return 1
            else:
                return 0
        if isinstance(other, Polynomial):
            if self.degree()!=other.degree():
                ans = 0
            else:
                for i in range(0, self.degree()+1):
                    if self.coef[i] != other.coef[i]:
                        ans = 0
            return ans

    def __radd__(self, other):
        return Polynomial.__add__(self, other)

    def __neg__(self):
        if isinstance(self, int):
            return -self
        else:
            new_coef=[0]*(self.degree()+1)
            for i in range(0, self.degree()+1):
                new_coef[i] = - self.coef[i]
            return Polynomial(new_coef)

    def __sub__(self, other):
        return Polynomial.__add__(self, Polynomial.__neg__(other))

    def __rsub__(self, other):
        return Polynomial.__radd__(Polynomial.__neg__(self), other)

    def __call__(self, x):
        ans=0
        for i in range(0, self.degree()+1):
            ans+=self.coef[i]*(x**i)
        return ans

    def der(self, d=1):
        new_coef=self.coef.copy()
        for j in range(0, d):
            for i in range(0, len(new_coef)-1):
                new_coef[i]=(i+1)*new_coef[i+1]
            new_coef.pop()
        return Polynomial(new_coef)

    def __mul__(self, other):
        if isinstance(other, int):
            new_coef=[0]*(self.degree()+1)
            for i in range(0, self.degree()+1):
                new_coef[i] = self.coef[i]*other
            return(Polynomial(new_coef))

        if isinstance(other, Polynomial):
            new_coef=[0]*(self.degree()+other.degree()+1)
            for i in range (0, self.degree()+1):
                for j in range(0, other.degree()+1):
                    new_coef[i+j]+=self.coef[i]*other.coef[j]
            return(Polynomial(new_coef))


    def __rmul__(self, other):
        return Polynomial.__mul__(self, other)

    def __mod__(self, other):
        if isinstance(other, Polynomial):
            new_coef=self.coef.copy()
            if other.degree()==0:
                return Polynomial(0)
            while len(new_coef)>other.degree():
                d=new_coef[-1]/other.coef[-1]
                deg_dif = len(new_coef)-1-other.degree()
                new_coef.pop()
                for i in range(0, other.degree()):
                    new_coef[deg_dif+i] -= other.coef[i]*d
            return Polynomial(new_coef)
        if isinstance(other, int):
            return Polynomial(0)

    def __rmod__(self, other):
        if isinstance(other, Polynomial):
            return self
        else:
            return Polynomial(0)

    def gcd(self, other):
        pol1=self
        pol2=other
        while pol1 % pol2 != 0 or pol2%pol1 != 0:
            if pol1.degree()>=pol2.degree():
                pol1=pol1%pol2
            else:
                pol2=pol2%pol1
        if pol1%pol2 == 0:
            return pol2
        else:
            return pol1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter[0] >= self.degree():
            raise StopIteration
        else:
            i = self.counter[0]+1
            self.counter = (i, self.coef[i])
            return self.counter


class RealPolynomial(Polynomial):
    def find_root(self):
        E = 10**(-10)
        a = 0
        b = 1
        while self.__call__(a)*self.__call__(b) >= 0 and self.__call__(-a)*self.__call__(-b) >= 0:
            if self.__call__(a) == 0:
                return a
            elif self.__call__(-a) == 0:
                return -a
            else:
                a+=1
                b+=1
        if self.__call__(a)*self.__call__(b) > 0:
            a=-a
            b=-b
        xn = a
        while abs(b - a) > 2 * E:
            xn = (a + b) / 2
            if self.__call__(a)*self.__call__(xn) < 0:
                b = xn
            else:
                a = xn
        return (round(xn, 10))


import math

class QuadraticPolynomial(Polynomial):
    def solve(self):
        a = self.coef[2]
        b = self.coef[1]
        c=self.coef[0]
        if a != 0:
            D=b**2-4*a*c
            if D < 0:
                return []
            if D == 0:
                return [-b/2/a]
            if D > 0:
                return [-(b+math.sqrt(D))/2/a, -(b-math.sqrt(D))/2/a]
        if a == 0:
            if b!=0:
                return [-c/b]
            if b == 0:
                if c!=0:
                    return []
                else:
                    return 'Any real number is a solution.'

