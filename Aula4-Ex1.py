def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

def verificar_situacao(media):
    if media < 7:
        situacao = "Reprovado"
    elif media == 10:
        situacao = "Parabéns, sua média é 10"
    else:
        situacao = "Aprovado"
    return situacao

def main():
    notas = []
    while True:
        nota = input("Digite uma nota (ou digite 'fim' para encerrar): ")
        if nota.lower() == 'fim':
            break
        try:
            nota = float(nota)
            if nota < 0 or nota > 10:
                print("Nota inválida. As notas devem estar entre 0 e 10.")
            else:
                notas.append(nota)
        except ValueError:
            print("Por favor, digite um número válido.")

    if notas:
        media = calcular_media(notas)
        situacao = verificar_situacao(media)
        print("Média:", media)
        print("Situação:", situacao)
    else:
        print("Nenhuma nota foi digitada.")

if __name__ == "__main__":
    main()