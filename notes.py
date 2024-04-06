import pandas as pd

# Load the data into a DataFrame
data = pd.read_csv("StarWars.txt", encoding='ISO-8859-1', skiprows=[1])

# Convert 'Yes'/'No' answers to boolean values for easier analysis
seen_any_movie = data.iloc[:, 1].map({'Yes': True, 'No': False})

# Calculate the percentage of people who have seen at least one Star Wars film
percentage_seen_any = seen_any_movie.mean() * 100

print(f'Percentage of respondents who have seen at least one Star Wars film: {percentage_seen_any:.4f}%')


# Filter the data for male respondents
male_respondents = data[data['Gender'] == 'Male']

# Convert 'Yes'/'No' answers to boolean values for easier analysis among male respondents
seen_any_movie_male = male_respondents.iloc[:, 1].map({'Yes': True, 'No': False})

# Calculate the percentage of male respondents who have seen at least one Star Wars film
percentage_seen_any_male = seen_any_movie_male.mean() * 100

print(f'Percentage of male respondents who have seen at least one Star Wars film: {percentage_seen_any_male:.4f}%')