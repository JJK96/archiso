import csv


def process_csv(input_file, output_file, process_function, delimiter=','):
    with open(input_file) as input, open(output_file, 'w') as output:
        reader = csv.DictReader(input, delimiter=delimiter)
        writer = csv.DictWriter(output, fieldnames=reader.fieldnames, delimiter=delimiter)
        writer.writeheader()
        for line in reader:
            if process_function(line):
                writer.writerow(line)


def csv_lines(input_file, delimiter=','):
    with open(input_file) as input:
        reader = csv.DictReader(input, delimiter=delimiter)
        yield from reader
