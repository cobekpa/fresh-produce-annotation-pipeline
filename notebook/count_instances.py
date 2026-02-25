import os
from collections import Counter

LABEL_DIR = r"C:\Users\Cobekpa\Downloads\fresh-produce-cvat-yolo-batch1\obj_train_data"

counter = Counter()

for file in os.listdir(LABEL_DIR):
    if file.endswith(".txt"):
        with open(os.path.join(LABEL_DIR, file), "r") as f:
            for line in f:
                if line.strip():
                    class_id = line.split()[0]
                    counter[class_id] += 1

print("Instance count per class ID:")
for k, v in counter.items():
    print(f"Class {k}: {v} instances")

print("\nTotal instances:", sum(counter.values()))