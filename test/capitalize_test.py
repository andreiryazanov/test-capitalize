from capitalize import capitalize

if capitalize('') != '':
    raise Exception('function does not work properly')
if capitalize('hello') != 'Hello':
    raise Exception('functiom does not work properly')

print('Tests are done')
