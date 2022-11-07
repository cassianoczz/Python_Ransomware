# Python_Ransomware
Exemplo didatico criação de Ransomware construido em Python com o proposito academico.

# Instalação

Instale o pipenv:

```
pip install pipenv
```

Faça o fork ou clone o projeto:
```
git clone git@github.com:<seu_usuario>/Python_Ransomware.git
```

Navegue até a pasta do projeto:
```
cd ../Python_Ransomware
```

Para instalar dependencias com pipenv:
```
pipenv install
```

Executar terminal:
```
python main.py
```
Após a execução, os arquivos da pasta ../Archives foram criptografados.
Altrando a variavel "start_path" incluido o caminho absoluto de outra pasta, 
os arquivos encontrados dentro serão criptografados

Para Decriptar os arquivos é necessario executar o arquivo "main.py" da seguinte forma:
```
python main.py -d || --decrypt
```