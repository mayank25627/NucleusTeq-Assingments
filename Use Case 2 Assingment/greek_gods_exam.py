import pandas as pd
print("********************************************************************************************************************************")


# 1.Merge the data from greek_gods.csv and greek_goddesses.csv based on a common field and create a new table that includes information about both gods and goddesses.


greek_gods_dataframe = pd.read_csv('greek_gods.csv')
greek_goddesses_dataframe = pd.read_csv('greek_goddesses.csv')

merged_df = pd.concat([greek_gods_dataframe, greek_goddesses_dataframe])

new_column_order = ['God', 'Goddess', 'Domain', 'Symbol', 'Age']


merged_df = merged_df.reindex(columns=new_column_order)
print(merged_df)


print("********************************************************************************************************************************")

# 2.Filter the merged table to only include gods and goddesses who are older than 8000 years, then sort them based on their ages in descending order.

filter_dc = merged_df[merged_df['Age'] > 8000]

filter_dc_sort = filter_dc.sort_values(by='Age', ascending=False)

print(filter_dc_sort)

print("********************************************************************************************************************************")

# 3.Join the two tables based on the "Domain" field and calculate the average age of gods and goddesses in each domain.

avg_age_by_domain = merged_df.groupby('Domain')['Age']
avg_age_by_domain = avg_age_by_domain.mean()

print(avg_age_by_domain)

print("********************************************************************************************************************************")

# 4.Determine which god/goddess has the highest age, and then find out if they are a god or a goddess.


god = pd.read_csv('greek_gods.csv')
god.rename(columns={'Age': 'God_Age'}, inplace=True)

goddess = pd.read_csv('greek_goddesses.csv')
goddess.rename(columns={'Age': 'Goddess_Age'}, inplace=True)


merged_god_godess = pd.concat([god, goddess])

max_age_god = merged_god_godess['God_Age'].max()
max_age_goddess = merged_god_godess['Goddess_Age'].max()


if max_age_god > max_age_goddess:
    oldest_entity = merged_god_godess[merged_god_godess['God_Age']
                                      == max_age_god].iloc[0]
    print(
        f"The oldest is {oldest_entity['God']} (God) with an age of {max_age_god} years.")
elif max_age_goddess > max_age_god:
    oldest_entity = merged_god_godess[merged_god_godess['Goddess_Age']
                                      == max_age_goddess].iloc[0]
    print(
        f"The oldest is {oldest_entity['Goddess']} (Goddess) with an age of {max_age_goddess} years.")
else:
    print("There is no god/goddess with the highest age.")

print("********************************************************************************************************************************")

# 5.Create a new column in each table called "Age_Group" and categorize the gods/goddesses into groups such as "Young" (age < 5000), "Middle-aged" (age between 5000 and 8000), and "Old" (age > 8000).


def categorize_age(age):
    if age < 5000:
        return 'Young'
    elif 5000 <= age <= 8000:
        return 'Middle-aged'
    else:
        return 'Old'


god = pd.read_csv('greek_gods.csv')
goddess = pd.read_csv('greek_goddesses.csv')


god['Age_Group'] = god['Age'].apply(categorize_age)
goddess['Age_Group'] = goddess['Age'].apply(categorize_age)

print(god)
print()
print(goddess)


print("********************************************************************************************************************************")


# 6.Compare the average ages of gods and goddesses. Is there a significant age difference between them? If yes, which group tends to be older?

avg_age_gods = god['Age'].mean()
avg_age_goddesses = goddess['Age'].mean()
age_difference = avg_age_gods - avg_age_goddesses
if age_difference > 0:
    print("Yes there is a significant age difference and Gods tend to be older than goddesses.")
elif age_difference < 0:
    print("Yes there is a significant age difference and Goddesses tend to be older than gods.")
else:
    print("The average ages of gods and goddesses are the same.")


print("********************************************************************************************************************************")


# 7.Write a Python program using for loop to iterate over the "Age" column of the merged table (after merging the gods and goddesses tables) and print out the names of gods/goddesses who are older than 8000 years.


for index, row in merged_df.iterrows():
    if row['Age'] > 8000:
        if pd.notna(row['God']):  # Check if 'God' column is not NaN
            print(row['God'])
        else:
            print(row['Goddess'])


print("********************************************************************************************************************************")

# 8.Write a Python program to find the oldest god/goddess from the merged table (after merging the gods and goddesses tables) by iterating through the "Age" column using a while loop. Print out the name of the oldest god/goddess and their age.

merged_god_godess['Age'] = merged_god_godess[[
    'God_Age', 'Goddess_Age']].max(axis=1)
oldest_name = None
oldest_age = None
i = 0
while i < len(merged_god_godess):
    row = merged_god_godess.iloc[i]
    if oldest_age is None or row['Age'] > oldest_age:
        oldest_age = row['Age']
        oldest_name = row['God'] if pd.notna(row['God']) else row['Goddess']
    i += 1

print(
    f"The oldest god/goddess is {oldest_name} with an age of {oldest_age} years.")
