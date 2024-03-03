# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Start coding here!
nobel = pd.read_csv('data/nobel.csv')
print(nobel.columns)

#What is the most commonly awarded gender and birth country? Storing the string answers as top_gender and top_country.
top_gender = nobel['sex'].value_counts().index[0]
top_country = nobel['birth_country'].value_counts().index[0]
print('TOP GENDER: ' + top_gender)
print('\nTOP COUNTRY: ' + top_country)

#What decade had the highest proportion of US-born winners? Store this as an integer called max_decade_usa.
nobel['usa_born_winner'] = nobel['birth_country'] == 'United States of America'
nobel['decade'] = (np.floor(nobel['year'] / 10) * 10).astype(int)
prop_usa_winners = nobel.groupby('decade', as_index=False)['usa_born_winner'].mean()

max_decade_usa = prop_usa_winners[prop_usa_winners['usa_born_winner'] == prop_usa_winners['usa_born_winner'].max()]['decade'].values[0]
print('\nDecade with Highest proportion of US-born winners: ' + str(max_decade_usa))

#What decade and category pair had the highest proportion of female laureates? Store this as a dictionary called max_female_dict where the decade is the key and the category is the value.
nobel['female_winner'] = nobel['sex'] =='Female'
prop_female_winners = nobel.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()
max_female_decade_category = prop_female_winners[prop_female_winners['female_winner'] == prop_female_winners['female_winner'].max()][['decade', 'category']]
max_female_dict = {max_female_decade_category['decade'].values[0]: max_female_decade_category['category'].values[0]}
print("\nHighest Female Proportion (Decade and Category): " + str(max_female_dict))

#Who was the first woman to receive a Nobel Prize, and in what category? Save your string answers as first_woman_name and first_woman_category.
#first_woman_name = nobel.groupby(['full_name', 'female_winner','year']).isin()
first_woman_name = nobel[nobel['sex'] == 'Female']['full_name'].values[0]
print('\nFirst Woman Winner: ' + str(first_woman_name))

first_woman_category = nobel[nobel['sex'] == 'Female']['category'].values[0]
print('\nFirst Woman Winner(Category): ' + str(first_woman_category))

#Which individuals or organizations have won multiple Nobel Prizes throughout the years? Store the full names in a list named repeat_list.
counts = nobel['full_name'].value_counts()
repeat = counts[counts >= 2]
repeat_list = repeat.index
print('\nMultiple Wins:') 
print(repeat_list)
