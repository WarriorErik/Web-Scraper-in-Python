import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Part 1: Scrape award per year data
url = "https://en.wikipedia.org/wiki/Turing_Award"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})
rows = table.find_all('tr')
data = []

for row in rows[1:]:
    cols = row.find_all('td')
    year = cols[0].text.strip()
    laureates = cols[1].text.strip()
    data.append((year, laureates))

df = pd.DataFrame(data, columns=['Year', 'Laureates'])

# Part 2: Store data to a well formatted dataframe, save to file
df.to_csv('turing_award.csv', index=False)

# Part 3: Create at least two (very different) visualizations
# Visualization 1: Count of laureates per year
df['Laureate Count'] = df['Laureates'].str.split(',').str.len()
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

plt.figure(figsize=(10,6))
sns.lineplot(data=df, x='Year', y='Laureate Count')
plt.title('Number of Turing Award Laureates Over Time')
plt.show()

# Visualization 2: Cumulative laureates over time
df['Cumulative Count'] = df['Laureate Count'].cumsum()

plt.figure(figsize=(10,6))
sns.lineplot(data=df, x='Year', y='Cumulative Count')
plt.title('Cumulative Number of Turing Award Laureates Over Time')
plt.show()
