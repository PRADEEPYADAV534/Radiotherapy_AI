import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# -----------------------------
# Load dataset
# -----------------------------
data = pd.read_csv("../data/clinical_plan_dataset.csv")

print("Clinical dataset loaded:")
print(data)

# -----------------------------
# Features and target
# -----------------------------
X = data[[
    "MLC_speed",
    "Monitor_Units",
    "Field_Size",
    "Complexity_Index"
]]

y = data["Gamma_Passing_Rate"]

# -----------------------------
# Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# -----------------------------
# Train model (Random Forest)
# -----------------------------
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# Evaluate
# -----------------------------
predictions = model.predict(X_test)
error = mean_absolute_error(y_test, predictions)

print("\nClinical model trained")
print("Mean Absolute Error:", round(error, 2))

# -----------------------------
# Predict new plan
# -----------------------------
new_plan = pd.DataFrame(
    [[1.3, 370, 13, 0.67]],
    columns=["MLC_speed", "Monitor_Units", "Field_Size", "Complexity_Index"]
)

predicted = model.predict(new_plan)
print("\nPredicted gamma passing rate:", round(predicted[0], 2))
