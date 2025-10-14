import csv

IN_FILE = "countries.csv"


def main():
    country_data = get_country_data()
    display_countries(country_data)


def get_country_data():
    country_to_data = {}
    with open(IN_FILE) as in_file:
        reader = csv.reader(in_file)
        header = next(reader)
        for row in reader:
            row[2] = int(row[2].replace(',', ''))
            row[3] = float(row[3].replace('%', ''))
            country_to_data[row[0]] = row[1:-1]
    return country_to_data


def display_countries(country_to_info):
    for country in country_to_info:
        print(f"{country} has {country_to_info.get(country)[0]}")


main()

# {Country: [Capital, Population, %], Country2: [data, data2, data3]}
