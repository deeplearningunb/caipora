import csv

years = ['2015', '2016', '2017', '2018', '2019']
mouths = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Novembro', 'Dezembro']

for year in years:

    for mouth in mouths:

        with open('dataset_initial/' + year + '/' + mouth + '.csv', 'r') as csv_file:

            csv_reader = csv.DictReader(csv_file)

            with open('dataset_final/' + year + '/' + mouth + '/' + mouth + '.csv', 'w') as new_file:

                fieldnames = ['datahora', 'estado', 'riscofogo','porcentagem']
                csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
                csv_writer.writeheader()

                for line in csv_reader:

                    del line['satelite']
                    del line['pais']
                    del line['municipio']
                    del line['precipitacao']
                    del line['frp']
                    del line['latitude']
                    del line['longitude']
                    del line['bioma']
                    del line['diasemchuva']

                    if line['riscofogo'] >= '0.7':
                        line['porcentagem'] = '1'
                    else:
                        line['porcentagem'] = '0'

                    csv_writer.writerow(line)