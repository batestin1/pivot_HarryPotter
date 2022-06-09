
#!/usr/local/bin/python
# coding: latin-1
#extrac

##################################################################################################################################################################
# Created on 07 de Outubro de 2021
#
#     Projeto base: Harry Potter Kafka Eventos
#     Repositório: Postgree
#     Author: Maycon Cypriano Batestin
#
##################################################################################################################################################################
##################################################################################################################################################################
#imports


import time
import argparse
import pandas as pd
import numpy as np
from faker import Faker
from sqlalchemy import create_engine
from datetime import datetime
import random


username = ""
password = ""
host = "kafka-db.ctkgorl88sm6.us-east-2.rds.amazonaws.com"
port = 5432
database = ""
table = "master"

# função para parsear a saída do parâmetro SILENT
def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

# Instancia a classe Faker
faker = Faker()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Generate fake data...')

    parser.add_argument('--interval', type=int, default=0.005,
                        help='interval of generating fake data in seconds')
    parser.add_argument('-n', type=int, default=1,
                        help='sample size')
    parser.add_argument('--connection-string', '-cs', dest="connection_string", 
                        type=str, default=f'ql://{username}:{password}@{host}:{port}/{database}',
                        help='Connection string to the database')
    parser.add_argument('--silent', type=str2bool, nargs='?',
                        const=True, default=False,
                        help="print fake data")

    args = parser.parse_args()

    print(f"Args parsed:")
    print(f"Interval: {args.interval}")
    print(f"Sample size; {args.n}")
    
    #-----------------------------------------------------------------

    engine = create_engine(args.connection_string)

    print("Iniciando a simulacao...", end="\n\n")

    # Gera dados fake a faz ingestão harry potter
    while True:
        nome = [faker.name() for i in range(args.n)]
        sexo = [np.random.choice(["M", "F"], p=[0.5, 0.5]) for i in range(args.n)]
        endereco = [faker.address() for i in range(args.n)]
        casa = [random.choice(['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw']) for i in range(args.n)]
        varinha  = [random.choice(['Acacia', 'Elder', 'Chestnut', 'Spruce ']) for i in range(args.n)]
        patronus = [random.choice(['Otter', 'Dog', 'Fox', 'Dumb', 'Elephant', 'Deer','Mouse', 'Bird', 'Frog', 'Fish', 'Mosquito', 'Bunny'])]
        nascimento = [faker.date_of_birth() for i in range(args.n)]
        profissao = [faker.job() for i in range(args.n)]
        dt_update = [datetime.now() for i in range(args.n)]

        df = pd.DataFrame({
            "name": nome,
            "gender": sexo,
            "adress": endereco,
            "houses": casa,
            "wand": varinha,
            "patronus": patronus,
            "birth": nascimento,
            "occupation": profissao,
            "dt_update": dt_update
        })

        df.to_sql("harrypotter", con=engine, if_exists="append", index=False)

