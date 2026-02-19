import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# -----------------------------------
# Step 1: Load dataset from CSV
# -----------------------------------
data = pd.read_csv("../data/gamma_dataset.csv")

print("Dataset loaded:")
print(data)

# -----------------------------------
# Step 2: Features and target
# -----------------------------------
X = data[["MLC_speed", "Monitor_Units", "Field_Size"]]
y = data["Gamma_Passing_Rate"]

# -----------------------------------
# Step 3: Train-test split
# -----------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------------
# Step 4: Train model
# -----------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------------
# Step 5: Evaluate
# -----------------------------------
predictions = model.predict(X_test)
error = mean_absolute_error(y_test, predictions)

print("\nModel trained from CSV data")
print("Mean Absolute Error:", round(error, 2))

# -----------------------------------
# Step 6: Predict new plan
# -----------------------------------
new_plan = pd.DataFrame(
    [[1.2, 350, 12]],
    columns=["MLC_speed", "Monitor_Units", "Field_Size"]
)

predicted = model.predict(new_plan)
print("\nPredicted gamma:", round(predicted[0], 2))
