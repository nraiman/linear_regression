from train import predictprice

def main():
    with open ('theta.csv', 'r') as fin:
        filecontent = fin.read()
        theta0, theta1 = filecontent.split('\n')

        theta0 = float(theta0)
        theta1 = float(theta1)
    km = input("quel est le kilometrage de votre voiture?")
    km = float(km)
    print (predictprice(theta0,theta1,km))

        


if __name__ == "__main__":
    main()

