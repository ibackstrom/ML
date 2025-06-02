x_values = [i for i in range(0,200)]
y_values = [i for i in range(0,400,2)]

def mean(values):
    return sum(values)/float(len(values))

mean_x = mean(x_values)
mean_y = mean(y_values)

def covariance(x, mean_x, y, mean_y):
    cov = 0
    for i in range(len(x)):
        cov += (x[i] - mean_x) * (y[i] - mean_y)
    return cov 

    
def variance(values, mean_value):
    return sum((x - mean_value) ** 2 for x in values)

def coeeficients(x, mean_x, y, mean_y):

    m = covariance(x, mean_x, y, mean_y) / variance(x, mean_x)
    b = mean_y - m * mean_x
    return m,b

slope, intersect = coeeficients(x_values,mean_x,y_values,mean_y)
def simple_linear_regression(x, slope, intersect):
    return slope*x+intersect
new_x = 6

prediction = simple_linear_regression(new_x,slope,intersect)

print(prediction)





