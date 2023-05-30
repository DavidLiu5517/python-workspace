zuobiao = input("Enter the points: ").split()

def getRectangle(points):
    x = []
    y = []
    for i in range(0, len(zuobiao), 2):
        x.append(zuobiao[i])
    for i in range(1, len(zuobiao), 2):
        y.append(zuobiao[i])
    x.sort
    y.sort
    
    width = float(x[-1]) - float(x[0])
    height = float(y[-1]) - float(y[0])

    x_ = float(x[0]) + (float(x[-1]) - float(x[0])) / 2
    y_ = float(y[0]) + (float(y[-1]) - float(y[0])) / 2

    print("The bounding rectangle is centered at (" + str(x_) + ", " + str(y_) + ") with width " + str(width) + " and height " + str(height))
    
getRectangle(zuobiao)