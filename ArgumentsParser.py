import argparse

def enter_argument_parser():
    argument = argparse.ArgumentParser(description='hackwareCrypter')
    argument.add_argument('-d', '--decrypt', help='Decrypt archives [Default: no]', action='store_true')
    var_argument = vars(argument.parse_args())    
    return var_argument
