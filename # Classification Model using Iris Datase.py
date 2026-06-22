"""
DecodeLabs Industrial Training - Project 2
Data Classification Using AI (Iris Dataset + KNN)

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score,
    f1_score
)


data = load_iris()
X = data.data                  
y = data.target                

df = pd.DataFrame(X, columns=data.feature_names)
df["species"] = pd.Categorical.from_codes(y, data.target_names)

print("\nDATASET OVERVIEW\n")
print(f"Shape: {df.shape}")
print(f"Classes: {list(data.target_names)}")
print(f"Class distribution:\n{df['species'].value_counts()}\n")
print(df.head())


X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,       
    random_state=42,     
    shuffle=True,        
    stratify=y           
)

print("\n")
print("TRAIN-TEST SPLIT")
print("\n")
print(f"Training samples: {X_train.shape[0]}")
print(f"Testing samples:  {X_test.shape[0]}")



scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)   

print("\n")
print("FEATURE SCALING")
print("\n")
print("Mean after scaling (train):", np.round(X_train_scaled.mean(axis=0), 2))
print("Std after scaling (train): ", np.round(X_train_scaled.std(axis=0), 2))



k_range = range(1, 21)
error_rates = []

for k in k_range:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)
    preds = model.predict(X_test_scaled)
    error_rates.append(1 - accuracy_score(y_test, preds))

best_k = k_range[np.argmin(error_rates)]

print("\n")
print("CHOOSING OPTIMAL K")
print("\n")
print(f"Best K found: {best_k}")

plt.figure(figsize=(8, 5))
plt.plot(k_range, error_rates, marker='o', linestyle='--', color='steelblue')
plt.axvline(best_k, color='orange', linestyle=':', label=f'Best K = {best_k}')
plt.title("Error Rate vs K Value")
plt.xlabel("K Value")
plt.ylabel("Error Rate")
plt.legend()
plt.tight_layout()
plt.savefig("k_tuning_plot.png", dpi=120)
plt.close()



model = KNeighborsClassifier(n_neighbors=best_k)
model.fit(X_train_scaled, y_train)
predictions = model.predict(X_test_scaled)

print("\n")
print("MODEL TRAINING COMPLETE")
print("\n")
print(f"Model: KNeighborsClassifier(n_neighbors={best_k})")



acc = accuracy_score(y_test, predictions)
f1 = f1_score(y_test, predictions, average='macro')
cm = confusion_matrix(y_test, predictions)
report = classification_report(y_test, predictions, target_names=data.target_names)

print("\nMODEL EVALUATION\n")
print(f"Accuracy: {acc:.4f}")
print(f"F1 Score (macro): {f1:.4f}\n")
print("Confusion Matrix:")
print(cm)
print("\nFull Classification Report:")
print(report)

# Visualize confusion matrix
plt.figure(figsize=(6, 5))
sns.heatmap(
    cm, annot=True, fmt='d', cmap='Blues',
    xticklabels=data.target_names, yticklabels=data.target_names
)
plt.title("Confusion Matrix - Iris KNN Classifier")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=120)
plt.close()



new_sample = np.array([[5.1, 3.5, 1.4, 0.2]])  
new_sample_scaled = scaler.transform(new_sample)
new_prediction = model.predict(new_sample_scaled)

print("\nPREDICTION ON NEW DATA\n")
print(f"Input: {new_sample[0]}")
print(f"Predicted species: {data.target_names[new_prediction[0]]}")