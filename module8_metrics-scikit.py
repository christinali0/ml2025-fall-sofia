import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    N = int(input("Enter the number of points N (positive integer): "))
    if N <= 0:
        print("Error: N must be a positive integer.")
        return

    true_labels = []
    pred_labels = []

    # Read N (x, y) pairs
    for i in range(N):
        x_val = int(input(f"Enter TRUE class (0 or 1) for point {i+1}: "))
        y_val = int(input(f"Enter PREDICTED class (0 or 1) for point {i+1}: "))

        # Validate values
        if x_val not in [0, 1] or y_val not in [0, 1]:
            print("Error: Both X and Y must be 0 or 1.")
            return

        true_labels.append(x_val)
        pred_labels.append(y_val)

    # Convert to NumPy arrays
    y_true = np.array(true_labels)
    y_pred = np.array(pred_labels)

    # Compute Precision and Recall using sklearn
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)

    print("\n=== Results ===")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")

if __name__ == "__main__":
    main()
