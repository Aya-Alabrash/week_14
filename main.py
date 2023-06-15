form get_covid_cases import *
from get_weather import *

def main():
  country = "canada"
  print(get_covid_cases(country))
  print(get_weather(country))

if __name__ == '__main__':
  main()