import utils
import charts
import pandas as pd

def run():
    # Leer el archivo CSV usando pandas
    data = pd.read_csv('data.csv')
    
    # Convertir DataFrame a una lista de diccionarios
    data = data.to_dict(orient='records')
    
    # Filtrar los datos por continente
    data = list(filter(lambda item: item['Continent'] == 'South America', data))
    
    # Extraer los nombres de los países y los porcentajes de población mundial
    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    
    # Generar un gráfico de torta (pie chart)
    charts.generate_pie_chart(countries, percentages)
    
    # Pedir al usuario que ingrese un país
    country = input('Type Country => ')
    print(country)
    
    # Buscar la población del país
    result = utils.population_by_country(data, country)
    
    if len(result) > 0:
        country = result[0]
        print(country)
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country'], labels, values)

if __name__ == '__main__':
    run()


