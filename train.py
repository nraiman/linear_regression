from csv import DictReader
import numpy as np

def loaddata():
    # open file in read mode
    with open('data.csv', 'r') as fin:
        # pass the file object to DictReader() to get the DictReader object
        dict_reader = DictReader(fin)
        # get a list of dictionaries from dct_reader
        list_of_dict = list(dict_reader)
        #print (list_of_dict)
        #for row in list_of_dict:
    x= np.array([float(row['km']) for row in list_of_dict])#km
    y= np.array([float(row['price']) for row in list_of_dict])#prix   
    return x, y

def normalize_data(data,datamin,datamax):
        return (data - datamin)/(datamax -datamin)
        
def normalize (x, y):
    xmin=x.min()
    ymin=y.min()
    xmax=x.max()
    ymax=y.max()
    #old_x = x
    #old_y = y
    x = normalize_data(x,xmin,xmax)
    y = normalize_data(y,ymin,ymax)
    return x, xmin, xmax, y, ymin, ymax

def predictprice(theta0, theta1, km):
    return theta0 + theta1 * km

def newtheta0(theta0, theta1, prix, km, alpha):
    return alpha * (predictprice(theta0, theta1, km) - prix).mean()


def newtheta1 (theta0, theta1,prix, km, alpha):
    return alpha * (
        (predictprice(theta0, theta1, km) - prix) * km
    ).mean()

def train(x, xmin, xmax, y, ymin, ymax):
    alpha = 1.0
    theta0 = 0.0
    theta1 = 0.0
    prev_error = ((y - predictprice(theta0, theta1, x))**2).mean()

    for i in range(1000):
        delta0 = newtheta0(theta0, theta1, prix=y, km=x, alpha=alpha)
        delta1 = newtheta1(theta0=theta0, theta1=theta1, prix=y, km=x, alpha=alpha)
        theta0 = theta0 - delta0
        theta1 = theta1 - delta1
        predictedy = predictprice(theta0, theta1, x)
        # plt.plot(x, y)
        # plt.plot(x, predictedy)
        error = ((y - predictedy) ** 2).mean()
        # if (error / max(prev_error, 1e-6)) > 0.99:
        #     alpha = max(alpha * 0.6, 0.0000000001)
        #     print("alpha", alpha)
        prev_error=error
    print(error, theta0, theta1)
    theta1 = (ymax -ymin)* theta1/ (xmax -xmin)
    theta0 = ymin+ (ymax-ymin)*(theta0- xmin/(xmax -xmin))
    return theta0, theta1

def save(theta0, theta1):
    with open('theta.csv', 'w') as fout:
        fout.write(str(theta0))
        fout.write('\n')
        fout.write(str(theta1))


def main():
    x, y = loaddata()
    x, xmin, xmax, y, ymin, ymax  = normalize(x, y)
    theta0, theta1 = train(x, xmin, xmax, y, ymin, ymax)
    print(theta0,theta1)
    save(theta0,theta1)


if __name__ == "__main__":
    main()