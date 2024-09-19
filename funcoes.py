import os
import time

#Função para limpar tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def voltar(): #Função que limpa após 2 segundos
    print("\nVoltando para categorias........")
    time.sleep(2)
    limpar_tela()

#Função que mostra as categorias 
def opcoes():
    menu = """
1 - Comprimento.
2 - Temperatura.
3 - Peso/Massa.
4 - Tempo. 
5 - Velocidade. 
6 - Área. 
7 - Sair.
"""
    escolha = input(menu + "Escolha uma categoria: ")

    return escolha

#funções comprimento

def opcoesC (): #Função com opções de comprimento
    menuC = """
1 - Metros para Centímetros.
2 - Quilômetros para Metros.
3 - Milhas para Quilômetros.
4 - Pés para Metros. 
5 - Polegadas para Centímetros.
6 - voltar.
"""
    escolha2 = input(menuC + "Escolha a Unidade De Medida para conversão: ")

    return escolha2

def metrosParaCentimetros(): #função que converte metros para centímetros
    metros = input("Insira a medida em Metros: ")
    if metros.replace('.', '', 1).isdigit():
        metros = float(metros)
        cent = metros * 100
        print(f"\n{metros} Metros equivalem a {cent} Centímetros.")
    else:
        print("\nPor favor, insira apenas números válidos.")

def kmParaMetros(): #Função que converte km para metros
    km = input("Insira a medida em Quilômetros: ")
    if km.replace('.', '', 1).isdigit():
        km = float(km)
        metros = km * 1000
        print(f"\n{km} Quilômetros equivalem a {metros} Metros.")
    else:
        print("\nPor favor, insira apenas números válidos.")
    

def milhasParaKm(): #Função que converte milhas para km
    milhas = input("Insira a medida em Milhas: ")
    if milhas.replace('.', '', 1).isdigit():
        milhas = float(milhas)
        km = milhas * 1.60934
        print(f"\n{milhas} Milhas equivalem a {km} Quilômetros.")
    else:
        print("\nPor favor, insira apenas números válidos.")

def pesParaMetros(): #Função que converte pés para metros
    pes = input("Insira a medida em Pés: ")
    if pes.replace('.', '', 1).isdigit():
        pes = float(pes)
        metros = pes * 0.3048
        print(f"\n{pes} Pés equivalem a {metros} Metros.")
    else:
        print("\nPor favor, insira apenas números válidos.")

def polegadasParaCentimetros(): #função que converte polegadas para centímetros
    polegadas = input("Insira a medida em Polegadas: ")
    if polegadas.replace('.', '', 1).isdigit():
        polegadas = float(polegadas)
        cent = polegadas * 2.54
        print(f"\n{polegadas} Polegadas equivalem a {cent} Centímetros.")
    else:
        print("\nPor favor, insira apenas números válidos.")

#Funções temperatura

def opcoesT(): #Fução com opções de temperatura
    menuT = """
1 - Celsius para Fahrenheit.
2 - Fahrenheit para Celsius.
3 - Celsius para Kelvin.
4 - Kelvin para Celsius. 
5 - Voltar.
"""
    escolha2 = input(menuT + "Escolha a Unidade De Medida para conversão: ")

    return escolha2

def celsiusParaFahrenheit(): #Função que converte celsius para fahrenheit
    celsius = input("Insira a temperatura em Celsius: ")
    if celsius.replace('.', '', 1).replace('-', '', 1).isdigit() and celsius.count('-') <= 1 and celsius[0] == '-' or celsius[0].isdigit():
        celsius = float(celsius)
        fah = celsius * 9/5 + 32
        print(f"\n{celsius} ºC equivalem a {fah} ºF.")
    else:
        print("\nPor favor, insira apenas números válidos.")

def fahrenheitParaCelsius(): #Função que converte fahrenheit para celsius
    fah = input("Insira a temperatura em Fahrenheit: ")
    if fah.replace('.', '', 1).replace('-', '', 1).isdigit() and fah.count('-') <= 1 and fah[0] == '-' or fah[0].isdigit():
        fah = float(fah)
        celsius = (fah - 32) * 5/9
        print(f"\n{fah} ºF equivalem a {celsius} ºC.")
    else:
        print("\nPor favor, insira apenas números válidos.")

def celsiusParaKelvin(): #Função que converte celsius para kelvin
    celsius = input("Insira a temperatura em Celsius: ")
    if celsius.replace('.', '', 1).replace('-', '', 1).isdigit() and celsius.count('-') <= 1 and celsius[0] == '-' or celsius[0].isdigit():
        celsius = float(celsius)
        kelvin = celsius + 273.15
        print(f"\n{celsius} ºC equivalem a {kelvin}ºK")
    else:
        print("\nPor favor, insira apenas números válidos.")

def kelvinParaCelsius(): #Função que converte kelvin para celsius
    kelvin = input("Insira a temperatura em Kelvin: ")
    if kelvin.replace('.', '', 1).replace('-', '', 1).isdigit() and kelvin.count('-') <= 1 and kelvin[0] == '-' or kelvin[0].isdigit():
        kelvin = float(kelvin)
        celsius = kelvin - 273.15
        print(f"\n{kelvin}ºK equivalem a {celsius}ºC")
    else: 
        print("\nPor favor, insira apenas números válidos.")

#Funções peso/massa

def opcoesP(): #Fução com opções de pesso/massa
    menuP = """
1 - Quilogramas para Gramas.
2 - Libras para Quilogramas.
3 - Toneladas para Quilogramas.
4 - Onças para Gramas. 
5 - Voltar.
"""
    escolha2 = input(menuP + "Escolha uma Unidade De Medida para conversão: ")

    return escolha2

def quilogramaParaGramas(): #Função que converte quilogramas para gramas
    kg = input("Insira o peso/massa em Quilogramas: ")
    if kg.replace('.',  '', 1).isdigit():
        kg = float(kg)
        gramas = kg * 1000
        print(f"\n{kg} Quilogramas equivalem a {gramas} gramas.")
    else:
        print("\nPor favor, insira apenas números válidos.")

def librasParaQuilogramas(): #Função que converte libras para quilogramas
    libras = input("Insira o peso/massa em Libras: ")
    if libras.replace('.', '', 1).isdigit():
        libras = float(libras)
        kg = libras * 0.453592
        print(f"\n{libras} Libras equivalem a {kg} Quilogramas.")
    else:
        print("\nPor favor, insira apenas números válidos.")

def toneladasParaQuilogramas(): #Função que converte toneladas para quilogramas
    toneladas = input("Insira o peso/massa em Toneladas: ")
    if toneladas.replace('.', '', 1).isdigit():
        toneladas = float(toneladas)
        kg = toneladas * 1000
        print(f"\n{toneladas} Toneladas equivalem a {kg} Quilogramas.")
    else:
        print("\nPor favor, insira apenas números válidos.")
    
def oncasParaGramas(): #Função que converte onças para gramas
    oncas = input("Insira o peso/massa em Onças: ")
    if oncas.replace('.', '', 1).isdigit():
        oncas = float(oncas)
        gramas = oncas * 28.3495
        print(f"\n {oncas} Onças equivalem a {gramas} Gramas.")

#Funções tempo 

def opcoesTempo(): #Função com opções de tempo 
    menuT = """
1 - Horas para Minutos. 
2 - Minutos para Segundos. 
3 - Dias para Horas. 
4 - Semanas para Dias. 
5 - Voltar.
"""
    escolha2 = input(menuT + "Escolha uma Unidade De Medida para conversão: ")

    return escolha2

def horasParaMinutos(): #Função que converte horas para minutos
    horas = input('Insira o tempo em horas (Utilize "." ex: 1.4): ')
    if horas.replace('.', '', 1).isdigit():
        horas = float(horas)
        minutos = horas * 60
        print(f"\n{horas} Horas equivalem a {minutos} Minutos.")
    else: 
        print("\nPor favor, insira apenas números válidos ou da forma pedida.")
    
def minutosParaSegundos(): #Função que converte minutos para segundos
    minutos = input("Insira o tempo em minutos: ")
    if minutos.replace('.', '', 1).isdigit():
        minutos = float(minutos)
        segundos = minutos * 60
        print(f"\n{minutos} Minutos equivalem a {segundos} Segundos.")
    else:
        print("\nPor favor, insira apenas números válidos.")

def diasParaHoras(): #Função que converte dias para horas
    dias = input("Insira o tempo em Dias: ")
    if dias.replace('.', '', 1).isdigit():
        dias = float(dias)
        horas = dias * 24
        print(f"\n{dias} Dias equivalem a {horas} Horas.")
    else:
        print("\nPor favor, insira apenas números válidos.")

def semanasParaDias(): #Função que converte semanas para dias
    semanas = input("Insira o tempo em Semanas: ")
    if semanas.replace('.', '', 1).isdigit():
        semanas = float(semanas)
        dias = semanas * 7
        print(f"\n{semanas} Semanas equivalem a {dias} Dias.")
    else:
        print("\nPor favor, insira apenas números válidos.")

#Funções para Velocidade
def opcoesV(): #Função com opções de velocidade
    menuV = """
1 - Quilômetros por Horas para Metros por Segundo.
2 - Milhas por Hora para Quilômetros por hora.
3 - Voltar.
"""
    escolha2 = input(menuV + "Escolha uma Unidade De Medida para conversão: ")

    return escolha2

def quilometroParaMetros(): #Função que converte quilômetros por hora para metros por segundo
    km = input("Insira a velocidade em Quilômetros por hora (km/h): ")
    if km.replace('.', '', 1).isdigit():
        km = float(km)
        ms = km * 0.277778
        print(f"\n{km} Quilometros por Hora equivalem a {ms} Metros por Segundo.")
    else:
        print("\nPor favor, insira apenas números válidos.")
    
def milhasParaQuilometros(): #Função que converte milhas por hora para quilometros por hora
    milhas = input("Insira a velocidade em Milhas: ")
    if milhas.replace('.', '', 1).isdigit():
        milhas = float(milhas)
        km = milhas * 1.60934
        print(f"\n{milhas} Milhas por Hora equivalem a {km} Quilômetros por hora.")
    else:
        print("\nPor favor, insira apenas números válidos.")

#Funções para área
def opcoesA(): #Função com opções área 
    menuA = """
1 - Metros Quadrados para Centímetros Quadrados.
2 - Quilômetros Quadrados para Metros Quadrados.
3 - Acres para Metros Quadrados.
4 - Voltar
"""
    escolha2 = input(menuA + "Escolha uma Unidade De Medida para conversão: ")

    return escolha2
 
def metrosParaCentimetrosQ(): #Função que converte metros quadrados para centímetros quadrados.
    metros = input("Insira a área em Metros Quadrados: ")
    if metros.replace('.', '', 1).isdigit():
        metros = float(metros)
        cent = metros * 10000
        print(f"\n{metros} Metros Quadrados equivalem a {cent} Centímetros Quadrados.")
    else:
        print("\nPor favor, insira apenas números válidos.")

def quilometrosParaMetrosQ(): #Função que converte quilômetros quadrados para metros quadrados
    km = input("Insira a área em Quilômetros Quadrados: ")
    if km.replace('.', '', 1).isdigit():
        km = float(km)
        metros = km * 1_000_000
        print(f"\n{km} Quilômetros Quadrados equivalem a {metros} Metros Quadrados.")
    else:
        print("\nPor favor, insira apenas números válidos.")

def acresParaMetros(): #Função que converte acres para metros quadrados
    acres = input("Insira a área em Acres: ")
    if acres.replace('.', '', 1).isdigit():
        acres = float(acres)
        metros = acres * 4046.86
        print(f"\n{acres} Acres equivalem a {metros} Metros Quadrados.")
    else:
        print("\nPor favor, insira apenas números válidos.")