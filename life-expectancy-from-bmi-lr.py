# Predecting life expectancy from BMI
# Data came from https://www.gapminder.org/

import pandas
from sklearn.linear_model import LinearRegression

# Assign the dataframe to this variable.
bmi_life_data = pandas.read_csv("bmi_and_life_expectancy.csv")

# Make and fit the linear regression model

bmi_life_model = LinearRegression()
bmi_life_model.fit(bmi_life_data[["BMI"]], bmi_life_data[["Life expectancy"]])

# Mak a prediction using the model

laos_life_exp = bmi_life_model.predict([[21.07931]])

print laos_life_exp
