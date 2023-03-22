import functions

print(functions.read_data('winequality.csv'))

print(functions.split(functions.read_data('winequality.csv'))[0])

print(functions.reduce(functions.split(functions.read_data('winequality.csv'))[1],"alcohol"))