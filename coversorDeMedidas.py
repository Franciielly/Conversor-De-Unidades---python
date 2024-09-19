from funcoes import*
import time

 
while True: 
    print("----------------Conversor de Unidade-----------------\n")
    escolha = opcoes()
    
    time.sleep(1)  # Espera 2 segundos para limpar tela após escolha
    limpar_tela()  # Limpa a tela

    if escolha == "1":
        while True:         
            escolha2 = opcoesC()
            if escolha2 == "1":
                metrosParaCentimetros()
            elif escolha2 == "2":
                kmParaMetros()
            elif escolha2 == "3":
                milhasParaKm()
            elif escolha2 == "4":
                pesParaMetros()
            elif escolha2 == "5": 
                polegadasParaCentimetros()
            elif escolha2 == "6":
                voltar()
                break
            else: 
                print("\nPor favor, insira apenas números válidos.")
        
    elif escolha == "2":
        while True: 
            escolha2 = opcoesT()
            if escolha2 == "1":
                celsiusParaFahrenheit()
            elif escolha2 == "2":
                fahrenheitParaCelsius()
            elif escolha2 == "3":
                celsiusParaKelvin()
            elif escolha2 == "4":
                kelvinParaCelsius()
            elif escolha2 == "5":
                voltar()
                break
            else:
                print("\nPor favor, insira apenas números válidos.")
    
    elif escolha == "3":
        while True:
            escolha2 = opcoesP()
            if escolha2 == "1":
                quilogramaParaGramas()
            elif escolha2 == "2":
                librasParaQuilogramas()
            elif escolha2 == "3":
                toneladasParaQuilogramas()
            elif escolha2 == "4":
                oncasParaGramas()
            elif escolha2 == "5":
                voltar()
                break
            else:
                print("\nPor favor, insira apenas números válidos.")
    
    elif escolha == "4":
        while True:
            escolha2 = opcoesTempo()
            if escolha2 == "1":
                horasParaMinutos()
            elif escolha2 == "2":
                minutosParaSegundos()
            elif escolha2 == "3":
                diasParaHoras()
            elif escolha2 == "4":
                semanasParaDias()
            elif escolha2 == "5":
                voltar()
                break
            else:
                print("\nPor favor, insira apenas números válidos."")
    
    elif escolha == "5":
        while True:
            escolha2 = opcoesV()
            if escolha2 == "1":
                quilometroParaMetros()
            elif escolha2 == "2":
                milhasParaQuilometros()
            elif escolha2 == "3":
                voltar()
                break
            else: 
                print("\nPor favor, insira apenas números válidos.")
    
    elif escolha == "6":
        while True:
            escolha2 = opcoesA()
            if escolha2 == "1":
                metrosParaCentimetrosQ()
            elif escolha2 == "2":
                quilometrosParaMetrosQ()
            elif escolha2 == "3":
                acresParaMetros()
            elif escolha2 == "4":
                voltar()
                break
            else:
                print("\nPor favor, insira apenas números válidos.")
    
    elif escolha == "7":
        print("Programa encerrado......")
        time.sleep(1)
        limpar_tela()
        break

    else: 
        print("\nPor favor, insira apenas números válidos.")
        time.sleep(2)
        limpar_tela()