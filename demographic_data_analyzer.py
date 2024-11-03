import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    df.index= df['race']
    race_count = df.index.value_counts()

    # What is the average age of men?
    men_mask = df['sex'] == 'Male'
    average_age_men = round(df[men_mask].age.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_mask = df['education'] == 'Bachelors'
    bachelors_mask.value_counts()
    percentage_bachelors = round((bachelors_mask.value_counts()[True]/df.shape[0])*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    edu_df = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = round((edu_df.value_counts()[True]/df.shape[0])*100, 1)
    lower_education = round((edu_df.value_counts()[False]/df.shape[0])*100, 1)

    # percentage with salary >50K
    high_edu_mask = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    high_edu_rich_df = high_edu_mask['salary'] == '>50K'
    higher_education_rich = round((high_edu_rich_df.value_counts()[True]/high_edu_mask.shape[0])*100, 1)

    low_edu_mask = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    low_edu_rich_df = low_edu_mask['salary'] == '>50K'
    lower_education_rich = round((low_edu_rich_df.value_counts()[True]/low_edu_mask.shape[0])*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work_mask = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = min_work_mask.shape[0]

    rich_min_work_df = min_work_mask['salary'] == '>50K'
    rich_percentage = round((rich_min_work_df.value_counts()[True]/rich_min_work_df.shape[0])*100, 1)

    # What country has the highest percentage of people that earn >50K?
    high_earners_mask = df[df['salary'] == '>50K']
    country_counts = df['native-country'].value_counts()
    high_earner_counts = high_earners_mask['native-country'].value_counts()
    earning_percentages = high_earner_counts/country_counts * 100
    highest_earning_country = earning_percentages.idxmax()
    highest_earning_country_percentage = round(earning_percentages.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    IN_mask = df[df['native-country'] == 'India']
    IN_occupation_counts = IN_mask['occupation'].value_counts()
    top_IN_occupation = IN_occupation_counts.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
