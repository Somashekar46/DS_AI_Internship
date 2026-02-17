import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# ----------------------------------
# Step 1: Create Non-Linear Dataset
# ----------------------------------
np.random.seed(42)

X = np.linspace(1, 10, 50)
y = 4*(X**2) + 3*X + 5 + np.random.randn(50)*20   # Quadratic relationship

X = X.reshape(-1, 1)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------------
# Step 2: Linear Regression (Original Feature)
# ----------------------------------
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

y_pred_linear = linear_model.predict(X_test)
r2_linear = r2_score(y_test, y_pred_linear)

# ----------------------------------
# Step 3: Generate 2nd-Degree Features
# ----------------------------------
poly = PolynomialFeatures(degree=2, include_bias=False)

X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# ----------------------------------
# Step 4: Train Linear Regression on Polynomial Features
# ----------------------------------
poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

y_pred_poly = poly_model.predict(X_test_poly)
r2_poly = r2_score(y_test, y_pred_poly)

# ----------------------------------
# Step 5: Compare Results
# ----------------------------------
print("Model Performance Comparison")
print("----------------------------------")
print(f"R² Score (Linear Model): {r2_linear:.4f}")
print(f"R² Score (Polynomial Degree 2): {r2_poly:.4f}")
