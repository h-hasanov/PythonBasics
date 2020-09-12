def functionWithMultipleResults(x):
    return 2*x, 3*x, 1+x

for i in range(0,5):
    double, tripple, _ = functionWithMultipleResults(i)
    print(double, tripple)