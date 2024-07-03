import pandas as pd

def calculate_demographic_data(print_data=True):
    # Cargar el conjunto de datos
    df = pd.read_csv('data.csv')

    # Cuántas personas de cada raza están representadas en este conjunto de datos
    race_count = df['race'].value_counts()

    # Edad promedio de los hombres
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Porcentaje de personas que tienen un título de Bachelors
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Porcentaje de personas con educación avanzada que ganan más de 50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((higher_education & (df['salary'] == '>50K')).mean() * 100, 1)

    # Porcentaje de personas sin educación avanzada que ganan más de 50K
    lower_education = ~higher_education
    lower_education_rich = round((lower_education & (df['salary'] == '>50K')).mean() * 100, 1)

    # Número mínimo de horas que trabaja una persona por semana
    min_work_hours = df['hours-per-week'].min()

    # Porcentaje de las personas que trabajan el número mínimo de horas por semana y tienen un salario de más de 50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # País con el porcentaje más alto de personas que ganan >50K
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_population = df['native-country'].value_counts()
    highest_earning_country = (country_salary / country_population * 100).idxmax()
    highest_earning_country_percentage = round((country_salary / country_population * 100).max(), 1)

    # Ocupación más popular para aquellos que ganan >50K en India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # Imprimir los resultados si print_data es True
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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
