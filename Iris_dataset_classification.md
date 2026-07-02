
# Iris Flower Classification using KNN
 
DecodeLabs Industrial Training — Project 2: Data Classification Using AI
 
## What This Project Does
 
This project builds a supervised learning model that classifies iris flowers into one of three species — **Setosa**, **Versicolor**, or **Virginica** — based on four physical measurements: sepal length, sepal width, petal length, and petal width.
 
The model uses the **K-Nearest Neighbors (KNN)** algorithm and the classic **Iris dataset** (150 samples, 3 balanced classes, 4 features).
 
## Pipeline Overview
 
The script follows the IPO (Input → Process → Output) framework:
 
1. **Load Data** — Load the built-in Iris dataset from scikit-learn
2. **Train-Test Split** — Split data 80/20 with shuffling and stratification (keeps class balance equal in both sets)
3. **Feature Scaling** — Apply `StandardScaler` so all features contribute equally to distance calculations (fit only on training data to avoid data leakage)
4. **Hyperparameter Tuning** — Loop through K values (1–20) to find the K with the lowest error rate (the "elbow method")
5. **Train Model** — Fit a `KNeighborsClassifier` using the optimal K
6. **Evaluate** — Generate a confusion matrix, F1 score, precision, and recall — not just raw accuracy
7. **Predict on New Data** — Test the trained model on a completely new, unseen sample
## Requirements
 
```bash
pip install scikit-learn pandas numpy matplotlib seaborn
```
 
## How to Run
 
```bash
python iris_classification.py
```
 
## Output
 
Running the script prints:
- Dataset overview and class distribution
- Train/test split sizes
- Scaling verification (mean ≈ 0, std ≈ 1)
- The best K value found
- Accuracy, F1 score, confusion matrix, and full classification report
- A prediction on a new sample
It also saves two plots in the same folder as the script:
- `k_tuning_plot.png` — Error rate vs K value (shows the "elbow")
- `confusion_matrix.png` — Heatmap of predicted vs actual classes
## Key Concepts Used
 
| Concept | Why It Matters |
|---|---|
| Feature Scaling | KNN relies on distance — unscaled features bias results |
| Stratified Split | Keeps class proportions equal in train/test sets |
| Elbow Method | Prevents underfitting (K too high) or overfitting (K too low) |
| Confusion Matrix | Shows exactly where the model gets confused between classes |
| F1 Score | More reliable than accuracy alone, especially if classes were imbalanced |
 
## Results
 
With the tuned K value, the model achieves **~96–97% accuracy** on the test set.
 







