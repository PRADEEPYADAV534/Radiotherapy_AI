import joblib
import pandas as pd

# -----------------------------
# Load saved model
# -----------------------------
model = joblib.load("../results/gamma_prediction_model.pkl")

print("Model loaded successfully")

# -----------------------------
# Predict new plan
# -----------------------------
new_plan = pd.DataFrame(
    [[1.3, 380, 14, 0.7]],
    columns=["MLC_speed", "Monitor_Units", "Field_Size", "Complexity_Index"]
)

prediction = model.predict(new_plan)

print("Predicted gamma passing rate:", round(prediction[0], 2))
