# Simple-Linear-Regression-Modeler
Takes raw data from an Excel file (.xlsx) and determines the best linear equation to fit that data. Outputs a scatterplot of data and line of best fit, equation for line, R^2, written interpretation, sample correlation, sigma^2 estimate, and sigma estimate.  

Excel sheet format: A1 must contain the title for the x-axis/independent variable. All data for this variable must be in A column.  
Likewise B1 must contain the title for the y-axis/dependent variable. All data for that variable must be in B column.  
EMPTY SPACES WILL BE IGNORED. Make sure the data is clean.  

Example:  
\_\_\_x\_\_\_\_|\_\_\_y\_\_\_\_  
\_\_\_\_\_\_\_\_|_\_\_\_\_\_\_\_  
\_\_12.1\_\_|\_\_1.23\_\_  
\_\_11.3\_\_|\_\_3.25\_\_  
\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_  
\_\_13.9\_\_|\_\_1.11\_\_  

Line of best fit is determined using the simple linear regression model. $\hat{y}\_i=\hat{\beta}\_0 + \hat{\beta}\_1x\_i$  
With least-squared estimates determined using $\hat{\beta}\_1=\frac{S\_{XY}}{S\_{XX}}$ and $\hat{\beta}\_0=\bar{y}-\hat{\beta}\_1\bar{x}$  
Where $S_{XY}=\sum_{i=1}^nx_iy_i-\frac{\sum_{i=1}^nx_i\sum_{i=1}^ny_i}{n}$ and $S_{XX}=\sum_{i=1}^nx_i^2-\frac{(\sum_{i=1}^nx_i)^2}{n}$  

Estimate of sigma^2 is found using $\hat{\sigma}^2=\frac{SSE}{n-2}$  
Where sum of squared errors (SSE) is found with $SSE=\sum_{i=1}^ny_i^2+\hat{\beta}\_0\sum\_{i=1}^ny\_i-\hat{\beta}\_1\sum\_{i=1}^ny\_ix_i$  

Sample correlation r is found with $r=\frac{S_{XY}}{\sqrt{S_{XX}}\sqrt{SST}}$  
Where total sum of squares (SST) is given by $SST=S_{YY}=\sum_{i=1}^ny_i^2-\frac{(\sum_{i=1}^ny_i)^2}{n}$

Coefficient of determination R^2 is found with $R^2=\frac{SST-SSE}{SST}$  
Where for a simple linear regression $R^2=r^2$
