import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    print(df.head())

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    raca_contar = df['race'].value_counts()

    # What is the average age of men?
    idade_media_homens = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bacharel = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    educacao_avancada = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    educacao_avancada_mais_50mil = df[educacao_avancada & (df['salary'] == '>50K')]

    porcentagem_educacao_avancada_mais_50mil = (educacao_avancada_mais_50mil.shape[0] / df[educacao_avancada].shape[0]) * 100

    # What percentage of people without advanced education make more than 50K?
    educacao_inferior = ~educacao_avancada
    educacao_inferior_mais_50mil = df[educacao_inferior & (df['salary'] == '>50K')]
    porcentagem_educacao_inferior_mais_50mil = (educacao_inferior_mais_50mil.shape[0] / df[educacao_inferior].shape[0]) * 100


    # with and without `Bachelors`, `Masters`, or `Doctorate`
    educacao_avancada = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    educacao_inferior = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    educacao_avancada_mais_50mil = round((educacao_avancada['salary'] == '>50K').mean() * 100, 1)
    educacao_inferior_mais_50mil = round((educacao_inferior['salary'] == '>50K').mean() * 100, 1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_trabalhadas_semana  = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_pessoas = df[df['hours-per-week'] == min_trabalhadas_semana]
    porcentagem_mais_50mil = round((num_min_pessoas['salary'] == '>50K').mean() * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    país_ganha_mais = df[df['salary'] == '>50K']['native-country'].value_counts()
    quantos_países = df['native-country'].value_counts()
    país_ganho_mais_50mil = (país_ganha_mais / quantos_países * 100).idxmax()
    porcentagem_país_ganho_mais_50mil = round((país_ganha_mais / quantos_países * 100).max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    ocupacao = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n",raca_contar ) 
        print("Average age of men:", idade_media_homen)
        print(f"Percentage with Bachelors degrees: {bacharel}%")
        print(f"Percentage with higher education that earn >50K: {educacao_avancada_mais_50mil}%")
        print(f"Percentage without higher education that earn >50K: {educacao_inferior_mais_50mil}%")
        print(f"Min work time: {min_trabalhadas_semana} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {porcentagem_mais_50mil}%")
        print("Country with highest percentage of rich:", país_ganha_mais_50mil)
        print(f"Highest percentage of rich people in country: {porcentagem_país_ganho_mais_50mil}%")
        print("Top occupations in India:", ocupacao)

    return {
        'race_count': raca_contar,
        'average_age_men': idade_media_homens,
        'percentage_bachelors': bacharel,
        'higher_education_rich': educacao_avancada_mais_50mil,
        'lower_education_rich': educacao_inferior_mais_50mil,
        'min_work_hours': min_trabalhadas_semana,
        'rich_percentage': porcentagem_mais_50mil,
        'highest_earning_country': país_ganho_mais_50mil,
        'highest_earning_country_percentage': porcentagem_país_ganho_mais_50mil,
        'top_IN_occupation': ocupacao
    }
    
