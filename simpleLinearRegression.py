import decimal

class SimpleLinearRegression:
     def __init__(self, x: list[float], y: list[float]):
        # error checking  
        assert len(x) == len(y), "x and y lists must have the same length"
        assert len(x) > 2, "number of data points must be greater than 2"
        
        # use decimal to help avoid floating-point error
        # set to track 100 decimal places 
        decimal.getcontext().prec = 100
        
        # convert lists to decimal type
        self.x = [decimal.Decimal(str(xi)) for xi in x]
        self.y = [decimal.Decimal(str(yi)) for yi in y]
        # get n number of data points
        self.n = len(x)
        
        # sum of x's
        self.xSum = sum(self.x)
        # sum of y's
        self.ySum = sum(self.y)
        # sum of the xy's multiplied
        self.xySum = sum(xi * yi for xi, yi in zip(self.x, self.y))
        # sum of x^2's
        self.xxSum = sum(xi ** 2 for xi in self.x)
        # sum of the y^2's
        self.yySum = sum(yi ** 2 for yi in self.y)
        
        # mean x
        self.xBar = self.xSum / self.n
        # mean y
        self.yBar = self.ySum / self.n
        
        # covarience of x and y
        self.S_xy = self.xySum - ((self.xSum * self.ySum) / self.n)
        # sum of squares for x^2
        self.S_xx = self.xxSum - ((self.xSum ** 2) / self.n)
        # sum of squares total - equivilant to sum of squares for y^2
        self.SST = self.yySum - ((self.ySum ** 2) / self.n)
        
        # beta_1 hat or model slope
        self.beta_1 = self.S_xy / self.S_xx
        # beta_2 hat or model y-intercept
        self.beta_0 = self.yBar - (self.beta_1 * self.xBar)
        
        # sum of squares error/residual
        self.SSE = self.yySum - (self.beta_0 * self.ySum) - (self.beta_1 * self.xySum)
        
        # sample correlation or r
        self.r = self.S_xy / (self.S_xx.sqrt() * self.SST.sqrt())
        # coefficient of determination or R^2 - equivilent to r^2
        self.RSquared = (self.SST - self.SSE) / self.SST
        # sigma^2 estimate
        self.varianceEstimate = self.SSE / (self.n - 2)
    
     # getters
     def GetN(self): return self.n
     def GetXSum(self): return self.xSum
     def GetYSum(self): return self.ySum
     def GetXYSum(self): return self.xySum
     def GetXXSum(self): return self.xxSum
     def GetYYSum(self): return self.yySum
     def GetXBar(self): return self.xBar
     def GetYBar(self): return self.yBar
     def GetS_xy(self): return self.S_xy
     def GetS_xx(self): return self.S_xx
     def GetSST(self): return self.SST
     def GetSSE(self): return self.SSE
     def GetBeta_0(self): return self.beta_0
     def GetBeta_1(self): return self.beta_1
     def Getr(self): return self.r
     def GetRSquared(self): return self.RSquared
     def GetVarianceEstimate(self): return self.varianceEstimate


