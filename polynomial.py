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
        while self.coef[-1]==0 and len(self.coef)>1:
            self.coef.pop()

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
            if i == 0 and self.coef[i]!=0:
                if outstr=='':
                    outstr=str(self.coef[i])
                elif self.coef[i] > 0:
                    outstr += ' + ' + str(self.coef[i])
                else:
                    outstr += ' - ' + str(-self.coef[i])
        return outstr

    def degree(self):
        return len(self.coef)-1

    def __add__(self, other):
        if isinstance(other, int):
            new_coef=self.coef.copy()
            new_coef[0]+=other
            return Polynomial(new_coef)
        if isinstance(other, Polynomial) and isinstance(self, Polynomial):
            if self.degree()<other.degree():
                new_coef=other.coef.copy()
                for i in range(0, self.degree()+1):
                    new_coef[i]+=self.coef[i]
            else:
                new_coef = self.coef.copy()
                for i in range(0, other.degree() + 1):
                    new_coef[i] += other.coef[i]
            return Polynomial(new_coef)
        if isinstance(self, int) and isinstance(other, Polynomial):
            new_coef=other.coef.copy()
            new_coef[0]+=self
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
        return Polynomial.__add__(other, self)

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
        return Polynomial.__radd__(other, Polynomial.__neg__(self))

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
            new_coef=self.coef.copy()
            for c in new_coef:
                c *= other
        if isinstance(other, Polynomial):


  #  def __rmul__(self, other):

   # def __mod__(self, other):

    #def __rmod__(self, other):

#    def gcd(self, other):

 #   def __iter__(self):

  #  def __next__(self):


#class RealPolynomial(Polynomial):
 #   def find_root(self):


#class QuadraticPolynomial(Polynomial):
 #   def solve(self):
