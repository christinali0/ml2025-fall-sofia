import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    N = int(input("Enter the number of points N (positive integer): "))
    if N <= 0:
        print("Error: N must be a positive integer.")
        return

    k = int(input("Enter the number of neighbors k (positive integer): "))
    if k <= 0:
        print("Error: k must be a positive integer.")
        return
    if k > N:
        print("Error: k cannot be greater than N.")
        return

    X_list = []
    y_list = []

    for i in range(N):
        x_val = float(input(f"Enter x value for point {i+1}: "))
        y_val = float(input(f"Enter y value for point {i+1}: "))
        X_list.append([x_val])
        y_list.append(y_val)

    X = np.array(X_list)
    y = np.array(y_list)

    variance_y = np.var(y)
    print(f"\nVariance of labels in training dataset: {variance_y:.4f}")

    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X, y)

    X_input = float(input("\nEnter the X value for prediction: "))
    Y_pred = knn.predict(np.array([[X_input]]))
    print(f"Predicted Y value for X={X_input}: {Y_pred[0]:.4f}")

if __name__ == "__main__":
    main()
