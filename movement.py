from scipy.io import loadmat
import numpy as np

files = [
    "data/s1/S1_E1_A1.mat",
    "data/s1/S1_E2_A1.mat",
    "data/s1/S1_E3_A1.mat",
]

for file in files:
    data = loadmat(file)

    exercise = int(data["exercise"].flatten()[0])
    labels = data["restimulus"].flatten()

    print("\n==============================")
    print("File:", file)
    print("Exercise:", exercise)
    print("Labels:", np.unique(labels))

    print("\nNumber of samples per label:")

    for label, count in zip(*np.unique(labels, return_counts=True)):
        print(f"Label {label}: {count}")