import numpy as np

class KNNRegression:
    def __init__(self, k):
        self.k = k
        self.X = None  # Will hold input features
        self.Y = None  # Will hold labels

    def fit(self, X, Y):
        self.X = np.array(X, dtype=float)
        self.Y = np.array(Y, dtype=float)

    def predict(self, x_test):
        if self.k > len(self.X):
            raise ValueError("k cannot be greater than the number of training points.")

        # Compute L2 distances from x_test to all points in training set
        distances = np.abs(self.X - x_test)

        # Get indices of k nearest neighbors
        nearest_indices = np.argsort(distances)[:self.k]

        # Return the average of Y values of k nearest neighbors
        return np.mean(self.Y[nearest_indices])

def main():
    # Read number of data points
    N = int(input("Enter the number of data points N (positive integer): "))

    if N <= 0:
        print("N must be a positive integer.")
        return

    # Read k
    k = int(input("Enter k (positive integer): "))

    if k <= 0:
        print("k must be a positive integer.")
        return

    # Read N (x, y) points
    X = []
    Y = []
    for i in range(N):
        x_val = float(input(f"Enter x value for point {i+1}: "))
        y_val = float(input(f"Enter y value for point {i+1}: "))
        X.append(x_val)
        Y.append(y_val)

    # Initialize k-NN model
    knn = KNNRegression(k)
    knn.fit(X, Y)

    # Read the test point
    x_test = float(input("Enter X value to predict Y: "))

    try:
        y_pred = knn.predict(x_test)
        print(f"Predicted Y value: {y_pred}")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
