import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile

# Fetch data from the World Bank API
url = "http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv"
response = requests.get(url)

# Save the zip file
with open('world_bank_data.zip', 'wb') as file:
    file.write(response.content)

# Extract the contents of the zip file
with zipfile.ZipFile('world_bank_data.zip', 'r') as zip_ref:
    zip_ref.extractall('world_bank_data')

# Load the data into a DataFrame
data_path = 'world_bank_data/API_SP.POP.TOTL_DS2_en_csv_v2_5668821.csv'
df = pd.read_csv(data_path, skiprows=4)

# Select relevant columns (Country Name and latest year of population data)
df_latest = df[['Country Name', '2022']]  # Change '2022' to the latest available year in your data
df_latest.columns = ['Country', 'Population']
df_latest = df_latest.dropna().reset_index(drop=True)

# Bar Chart: Top 10 Most Populous Countries
top_10 = df_latest.nlargest(10, 'Population')
plt.figure(figsize=(12, 6))
sns.barplot(x=top_10['Country'], y=top_10['Population'])
plt.xlabel('Country')
plt.ylabel('Population')
plt.title('Top 10 Most Populous Countries in 2022')
plt.xticks(rotation=45)
plt.show()

# Histogram: Distribution of Populations
plt.figure(figsize=(12, 6))
sns.histplot(df_latest['Population'], bins=30, kde=False)
plt.xlabel('Population')
plt.ylabel('Count')
plt.title('Distribution of Populations of Countries in 2022')
plt.show()
