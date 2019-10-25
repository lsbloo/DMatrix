"""
 exporta os dados encontrados e armazenados no banco para arquivos csv;
"""
from core.auth import PATH_SAVE_CSV
import os
import sys
import csv

def get_list_address_valid(tuple_address):
    result=[tuple_address[0],tuple_address[1],tuple_address[2],tuple_address[3],tuple_address[4],tuple_address[5]]
    return result

def generate_csv_address(list_address):
    path = PATH_SAVE_CSV+"/"+"address.csv"
    locates = open(path,"w")
    spamwriter = csv.writer(locates, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['id','street','number','neighborhood','city','state'])
    list_valid=[]
    for i in range(len(list_address)):
        list_valid.append(get_list_address_valid(list_address[i]))
    for i in list_valid:
        spamwriter.writerow(i)

def transform_csv_address(row):
    exita = row[0].split(";")
    return exita

def reader_csv_address():
    path = PATH_SAVE_CSV+"/"+"address.csv"
    archive = open(path,'r')
    reader = csv.reader(archive)
    cabecalho =True
    list_resolve=[]
    for row in reader:
        if cabecalho:
            #print(f'Nome Colunas: {", ".join(row)}')
            cabecalho=False
        else:
            #print(f'{", ".join(row)}')
            list_resolve.append(transform_csv_address(row))
    return list_resolve
        


