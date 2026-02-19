import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# -----------------------------
# Load dataset
# -----------------------------
data = pd.read_csv("../data/simulated_radiotherapy_dataset.csv")

X = data[[
    "MLC_speed",
    "Monitor_Units",
    "Field_Size",
    "Complexity_Index"
]]

y = data["Gamma_Passing_Rate"]

# -----------------------------
# Train model
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# Save model
# -----------------------------
joblib.dump(model, "../results/gamma_prediction_model.pkl")

print("Model saved successfully")
