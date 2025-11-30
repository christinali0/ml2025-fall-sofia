import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# ----------- READ TRAINING DATA -----------

N = int(input("Enter N (number of training points): "))
if N <= 0:
    print("N must be a positive integer.")
    exit()

X_train = []
y_train = []

print("\nEnter training (x, y) pairs one by one:")

for i in range(N):
    x = float(input(f"Enter x{i+1}: "))
    y = int(input(f"Enter y{i+1} (class label): "))
    X_train.append([x])
    y_train.append(y)

X_train = np.array(X_train)
y_train = np.array(y_train)


# ----------- READ TEST DATA -----------

M = int(input("\nEnter M (number of test points): "))
if M <= 0:
    print("M must be a positive integer.")
    exit()

X_test = []
y_test = []

print("\nEnter test (x, y) pairs one by one:")

for i in range(M):
    x = float(input(f"Enter x{i+1}: "))
    y = int(input(f"Enter y{i+1} (class label): "))
    X_test.append([x])
    y_test.append(y)

X_test = np.array(X_test)
y_test = np.array(y_test)


# ----------- FIND BEST k USING kNN -----------

best_k = 1
best_accuracy = 0

print("\nTesting k from 1 to 10...")

for k in range(1, 11):
    if k > N:
        continue

    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"k = {k} --> Accuracy = {accuracy:.4f}")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_k = k


# ----------- OUTPUT RESULTS -----------

print(f"Best k value: {best_k}")
print(f"Test set accuracy: {best_accuracy:.4f}")
