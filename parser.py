import csv

years = ['2015', '2016', '2017', '2018', '2019']
mouths = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# for year in years:
#
#     for mouth in mouths:
#
#         with open('dataset/dataset_initial/' + year + '/' + mouth + '.csv', 'r') as csv_file:
#
#             csv_reader = csv.DictReader(csv_file)
#
#             with open('dataset/dataset_final/' + year + '/' + mouth + '.csv', 'w') as new_file:
#
#                 fieldnames = ['datahora', 'estado', 'riscofogo', 'riscoAbsoluto']
#                 csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
#                 csv_writer.writeheader()
#
#                 for line in csv_reader:
#
#                     del line['satelite']
#                     del line['pais']
#                     del line['municipio']
#                     del line['precipitacao']
#                     del line['frp']
#                     del line['latitude']
#                     del line['longitude']
#                     del line['bioma']
#                     del line['diasemchuva']
#
#                     if line['riscofogo'] >= '0.7':
#                         line['riscoAbsoluto'] = '1'
#                     else:
#                         line['riscoAbsoluto'] = '0'
#
#                     csv_writer.writerow(line)

"""
Antes de Mandar Rodar o parser completo, lembre-se de excluir os dados da pasta queimadas_initial
"""

for year in years:

    for mouth in mouths:

        with open('dataset/dataset_final/' + year + '/' + mouth + '.csv', 'r') as csv_file:

            csv_reader = csv.DictReader(csv_file)

            with open('queimadas/queimadas_initial/queimadas-Brasil-' + year + '.csv', 'a') as new_file:

                fieldnames = ['ano','mes','datahora', 'estado', 'riscofogo', 'riscoAbsoluto']
                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                csv_writer.writeheader()

                for line in csv_reader:

                    line['ano'] = year
                    line['mes'] = mouth

                    csv_writer.writerow(line)

"""
Antes de Mandar Rodar o parser completo, lembre-se de excluir os dados da pasta queimadas_final
"""

for year in years:

    for mouth in mouths:

        with open('dataset/dataset_final/' + year + '/' + mouth + '.csv', 'r') as csv_file:

            csv_reader = csv.DictReader(csv_file)

            with open('queimadas/queimadas_final/queimadas-Brasil-' + year + '.csv', 'a') as new_file:

                fieldnames = ['id', 'ano', 'mes', 'datahora', 'estado', 'riscofogo', 'riscoAbsoluto']
                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                csv_writer.writeheader()

                for aux, row in enumerate(csv_reader):

                    row['id'] = aux
                    row['ano'] = year
                    row['mes'] = mouth

                    csv_writer.writerow(row)