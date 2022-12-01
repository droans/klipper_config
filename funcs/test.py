FUNCTIONS = [
    {
        'name': 'tester_func',
        'function': 'function_test',
    },
    {
        'name': 'repeater',
        'function': 'repeat_back',
    }
]

def function_test():
    return 'hello'

def repeat_back(rept):
    return rept + ' ' + rept