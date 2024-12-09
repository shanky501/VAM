



#polynomial regresion- predictionn
import numpy as np
from sklearn.metrices 
import r2_score
age=[20,25,30,45,50]
salary=[40000,15000,20000,25000,2200]
futursalary=np.poly1d(np.polyfit (age,salary,3))
print(r2_score,salary,futuresalary(35))    




# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score
# import matplotlib.pyplot as plt

# # Load your dataset
# # Replace 'your_data.csv' with the path to your dataset
# data = pd.read_csv('your_data.csv')

# # Inspect data
# print(data.head())

# # Features (X) and target variable (y)
# # Replace 'Sales' and feature columns with appropriate column names
# X = data[['Economic_Indicator1', 'Economic_Indicator2', 'Past_Sales']]  # Add relevant feature columns
# y = data['Sales']  # Target variable

# # Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Initialize regression model
# model = LinearRegression()

# # Train the model
# model.fit(X_train, y_train)

# # Predict on the test set
# y_pred = model.predict(X_test)

# # Evaluate the model
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# print(f"Mean Squared Error: {mse}")
# print(f"R^2 Score: {r2}")

# # Plotting actual vs predicted values
# plt.scatter(y_test, y_pred)
# plt.xlabel('Actual Sales')
# plt.ylabel('Predicted Sales')
# plt.title('Actual vs Predicted Sales')
# plt.show()

# # Predict sales for next year
# # Replace 'next_year_data' with actual predictor values for the next year
# next_year_data = np.array([[economic_indicator1_value, economic_indicator2_value, past_sales_value]])
# predicted_sales = model.predict(next_year_data)

# print(f"Predicted Sales for Next Year: {predicted_sales[0]}")







