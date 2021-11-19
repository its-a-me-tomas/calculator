import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
matrix=[[9,8],[6,4],[2,1]]
independet = [1,3,9]
if len(matrix[0]) == 3:
    fig = plt.figure()
    ax = fig.add_subplot(111,projection="3d")
    x, y = np.linspace(-8,8,500), np.linspace(-8,8,500)
    X, Y = np.meshgrid(x,y)
    for i in range(len(matrix)):
        z = (independet[i] - matrix[i][0]*X - matrix[i][1]*Y)/matrix[i][2]
        ax.plot_surface(X,Y,z, alpha=0.5, rstride=100, cstride=100)
    plt.show()
elif len(matrix[0]) == 2:
    x, y = np.linspace(-10,10,500), np.linspace(-10,10,500)
    for i in range(len(matrix)):
        y = (independet[i]-matrix[i][0]*x)/matrix[i][1]
        plt.plot(x,y)
    plt.show()    
    print("2d graphic")