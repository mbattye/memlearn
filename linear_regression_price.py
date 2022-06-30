import statsmodel.api as sm
import pandas as pd

df = pd.read_csv("/Users/michaelbattye/Downloads/bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv")

df.dropna()
print(df.head())

# model = sm.OLS()