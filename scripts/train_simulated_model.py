import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

data = pd.read_csv("../data/simulated_radiotherapy_dataset.csv")

X = data[[
    "MLC_speed",
    "Monitor_Units",
    "Field_Size",
    "Complexity_Index"
]]

y = data["Gamma_Passing_Rate"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
error = mean_absolute_error(y_test, predictions)

print("Model trained on simulated radiotherapy dataset")
print("Mean Absolute Error:", round(error, 2))
