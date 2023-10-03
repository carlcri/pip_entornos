import utils
import read_csv
import charts
import pandas as pd

def run():

  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'South America']

  countries = df['Country'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  country = input('Type Country => ').capitalize()
  print(country)

  data = read_csv.read_csv('data.csv')
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)

if __name__ == '__main__':
  run()