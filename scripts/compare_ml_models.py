import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

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
# Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Models to compare
# -----------------------------
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=200, random_state=42),
    "Support Vector Regression": SVR()
}

# -----------------------------
# Train and evaluate
# -----------------------------
print("Model Comparison Results:\n")

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    error = mean_absolute_error(y_test, predictions)

    print(name)
    print("Mean Absolute Error:", round(error, 3))
    print("-" * 30)
