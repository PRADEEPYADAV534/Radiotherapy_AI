import numpy as np
import pandas as pd

np.random.seed(42)

num_plans = 200

# -------------------------
# Simulate realistic ranges
# -------------------------
mlc_speed = np.random.uniform(0.5, 2.5, num_plans)
monitor_units = np.random.uniform(150, 700, num_plans)
field_size = np.random.uniform(5, 25, num_plans)
complexity = np.random.uniform(0.4, 0.9, num_plans)

# -------------------------
# Simulate gamma behaviour
# Higher complexity & MU → lower gamma
# -------------------------
gamma = (
    98
    - 0.9 * mlc_speed
    - 0.0025 * monitor_units
    + 0.08 * field_size
    - 1.2 * complexity
    + np.random.normal(0, 0.4, num_plans)
)

# -------------------------
# Create dataframe
# -------------------------
data = pd.DataFrame({
    "MLC_speed": mlc_speed,
    "Monitor_Units": monitor_units,
    "Field_Size": field_size,
    "Complexity_Index": complexity,
    "Gamma_Passing_Rate": gamma
})

# -------------------------
# Save dataset
# -------------------------
data.to_csv("../data/simulated_radiotherapy_dataset.csv", index=False)

print("Simulated dataset created with", num_plans, "plans")
print(data.head())
