import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    recall_score,
    f1_score
)

import joblib
import matplotlib.pyplot as plt


# ==========================================
# SUPPLY CHAIN MACHINE LEARNING
# DELIVERY DELAY PREDICTION
# ==========================================

print("==========================================")
print("SUPPLY CHAIN MACHINE LEARNING")
print("==========================================")


# ==========================================
# 1. LOAD DATASET
# ==========================================

file_path = "../data/supply_chain_dataset_2000.xlsx"

df = pd.read_excel(file_path)

print("Dataset loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# ==========================================
# 2. CREATE TARGET VARIABLE
# ==========================================

# 0 = On Time
# 1 = Delayed

df["Delayed"] = (
    df["Delivery_Status"] == "Delayed"
).astype(int)

print("\nTarget Distribution:")
print(df["Delayed"].value_counts())

print(
    df["Delayed"].value_counts(normalize=True) * 100
)


# ==========================================
# 3. SELECT FEATURES
# ==========================================

# Supplier_Performance_Pct is excluded because
# it creates an unrealistically strong relationship
# with the target variable.

features = [
    "Quantity",
    "Unit_Cost",
    "Transportation_Cost",
    "Lead_Time_Days",
    "Inventory_Level",
    "Reorder_Level",
    "Monthly_Demand_Estimate"
]

X = df[features]
y = df["Delayed"]

print("\nFeatures used:")
print(features)

print("\nFeature shape:", X.shape)
print("Target shape:", y.shape)


# ==========================================
# 4. TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\n==========================================")
print("TRAIN / TEST SPLIT")
print("==========================================")

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# ==========================================
# 5. RANDOM FOREST
# ==========================================

random_forest = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

random_forest.fit(X_train, y_train)

print("\nRandom Forest model trained successfully!")


# Predictions

rf_pred = random_forest.predict(X_test)


# ==========================================
# 6. RANDOM FOREST EVALUATION
# ==========================================

rf_accuracy = accuracy_score(
    y_test,
    rf_pred
)

rf_delayed_recall = recall_score(
    y_test,
    rf_pred,
    pos_label=1
)

rf_delayed_f1 = f1_score(
    y_test,
    rf_pred,
    pos_label=1
)

print("\n==========================================")
print("RANDOM FOREST PERFORMANCE")
print("==========================================")

print(
    "Accuracy:",
    round(rf_accuracy * 100, 2),
    "%"
)

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        rf_pred,
        target_names=["On Time", "Delayed"]
    )
)

print("Confusion Matrix:")

print(
    confusion_matrix(
        y_test,
        rf_pred
    )
)


# ==========================================
# 7. LOGISTIC REGRESSION
# ==========================================

print("\n==========================================")
print("LOGISTIC REGRESSION")
print("==========================================")

# Standardize features

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)

X_test_scaled = scaler.transform(
    X_test
)


logistic_model = LogisticRegression(
    random_state=42,
    class_weight="balanced",
    max_iter=1000
)

logistic_model.fit(
    X_train_scaled,
    y_train
)

print(
    "Logistic Regression model trained successfully!"
)


# Predictions

lr_pred = logistic_model.predict(
    X_test_scaled
)


# ==========================================
# 8. LOGISTIC REGRESSION EVALUATION
# ==========================================

lr_accuracy = accuracy_score(
    y_test,
    lr_pred
)

lr_delayed_recall = recall_score(
    y_test,
    lr_pred,
    pos_label=1
)

lr_delayed_f1 = f1_score(
    y_test,
    lr_pred,
    pos_label=1
)

print(
    "\nLogistic Regression Accuracy:",
    round(lr_accuracy * 100, 2),
    "%"
)

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        lr_pred,
        target_names=["On Time", "Delayed"]
    )
)

print("Confusion Matrix:")

print(
    confusion_matrix(
        y_test,
        lr_pred
    )
)


# ==========================================
# 9. MODEL COMPARISON
# ==========================================

comparison = pd.DataFrame({

    "Model": [
        "Random Forest",
        "Logistic Regression"
    ],

    "Accuracy": [
        rf_accuracy * 100,
        lr_accuracy * 100
    ],

    "Delayed Recall": [
        rf_delayed_recall * 100,
        lr_delayed_recall * 100
    ],

    "Delayed F1": [
        rf_delayed_f1 * 100,
        lr_delayed_f1 * 100
    ]
})


print("\n==========================================")
print("MODEL COMPARISON")
print("==========================================")

print(
    comparison.round(2)
)


# ==========================================
# 10. RANDOM FOREST FEATURE IMPORTANCE
# ==========================================

feature_importance = pd.DataFrame({

    "Feature": features,

    "Importance":
        random_forest.feature_importances_

}).sort_values(
    by="Importance",
    ascending=False
)


print("\n==========================================")
print("FEATURE IMPORTANCE")
print("==========================================")

print(
    feature_importance
)


# ==========================================
# 11. SAVE FEATURE IMPORTANCE CHART
# ==========================================

plt.figure(figsize=(10, 6))

plt.barh(
    feature_importance["Feature"],
    feature_importance["Importance"]
)

plt.title(
    "Random Forest Feature Importance"
)

plt.xlabel("Importance")

plt.ylabel("Feature")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig(
    "model_results/feature_importance.png",
    dpi=300
)

plt.close()

print(
    "\nFeature importance chart saved successfully!"
)


# ==========================================
# 12. SAVE MODELS
# ==========================================

joblib.dump(
    random_forest,
    "model_results/delivery_delay_model.pkl"
)

joblib.dump(
    logistic_model,
    "model_results/logistic_regression_model.pkl"
)

joblib.dump(
    scaler,
    "model_results/scaler.pkl"
)

print("\nModels saved successfully!")


# ==========================================
# 13. SAVE MODEL COMPARISON
# ==========================================

comparison.to_csv(
    "model_results/model_comparison.csv",
    index=False
)

# ==========================================
# 15. MODEL ACCURACY COMPARISON CHART
# ==========================================

plt.figure(figsize=(8, 5))

plt.bar(
    comparison["Model"],
    comparison["Accuracy"]
)

plt.title("Model Accuracy Comparison")
plt.xlabel("Machine Learning Model")
plt.ylabel("Accuracy (%)")

plt.ylim(0, 100)

plt.tight_layout()

plt.savefig(
    "model_results/model_accuracy_comparison.png",
    dpi=300
)

plt.close()

print(
    "Model accuracy comparison chart saved successfully!"
)


# ==========================================
# 16. DELAYED RECALL COMPARISON CHART
# ==========================================

plt.figure(figsize=(8, 5))

plt.bar(
    comparison["Model"],
    comparison["Delayed Recall"]
)

plt.title("Delayed Order Recall Comparison")
plt.xlabel("Machine Learning Model")
plt.ylabel("Delayed Recall (%)")

plt.ylim(0, 100)

plt.tight_layout()

plt.savefig(
    "model_results/delayed_recall_comparison.png",
    dpi=300
)

plt.close()

print(
    "Delayed recall comparison chart saved successfully!"
)

feature_importance.to_csv(
    "model_results/feature_importance.csv",
    index=False
)

print(
    "Model comparison saved successfully!"
)

print(
    "Feature importance data saved successfully!"
)


# ==========================================
# 14. FINAL MESSAGE
# ==========================================

print("\n==========================================")
print("MACHINE LEARNING ANALYSIS COMPLETED")
print("==========================================")