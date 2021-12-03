# LOCAL RAW TO CURATED - LINUX SPARK JOB

Neste repositório você vai encontrar a etapa de movimentação de um determinado arquivo .PARQUET da Zona Raw para a Zona Curated, sendo executado **LOCALMENTE** através do Linux.
Foi desenvolvido em ambiente VENV com PIPENV, conforme descrição abaixo.

1. Leitura dos dados de origem na Zona Raw;
2. Escrita dos dados no destino na Zona Curated.

# Execução

O arquivo [run_job.sh](scripts/run_job.sh) contém os comandos necessários para a criação da build, onde deverá conter:
- `packages`: com a pasta e arquivos (src/read_write.py && config.py) zipados
e a execução do código.

# Fontes

- Leitura (origem): ["./datalake_env/raw"]
- Escrita (destino): ["./datalake_env/curated"]

---------------------------------------------------------------------------------------------------------------------------------------------------------

# Para criar o amviente VENV dentro do Vscode com PIPENV

Primeiramente entramos no diretório do projeto e seguimos os seguintes passos:

1. pip3 install pipenv **caso não tenha instalado o pipenv**
2. set PIPENV_VENV_IN_PROJECT
3. PIPENV_VENV_IN_PROJECT=1 pipenv shell
4. pipenv install pyspark **instalar todas as lib necessárias para o projeto**
5. Criar a pasta Makefile na raiz do projeto com o seguinte script:
build:
	mkdir ./packages
	cd ./src && zip -r ../packages/src.zip .

---------------------------------------------------------------------------------------------------------------------------------------------------------

# Para fazer a chamada do script e rodar o projeto

1. Entrar no diretório scripts
2. No terminal digitar: sudo ./run_job.sh