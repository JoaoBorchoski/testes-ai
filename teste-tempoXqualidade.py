def avaliar_trabalho(tempo_em_dias, qualidade):
    # Defina os pesos para tempo e qualidade
    peso_tempo = 0.4
    peso_qualidade = 0.6

    # Converta os dias em uma escala de 0 a 1, onde 0 é o melhor (menos dias) e 1 é o pior (mais dias)
    escala_tempo = tempo_em_dias / 365  # Assumindo um ano como referência

    # Calcule a pontuação total com base nos pesos
    pontuacao_total = escala_tempo * peso_tempo + qualidade * peso_qualidade

    # Defina um limiar para considerar se o trabalho foi bom ou não
    limiar_bom = 0.8

    # Verifique se a pontuação total atinge o limiar para considerar o trabalho bom
    if pontuacao_total >= limiar_bom:
        return "Trabalho bom!"
    else:
        return "Trabalho a ser melhorado."


# Exemplo de uso
tempo_exemplo_dias = 150  # Mais dias é pior
qualidade_exemplo = 5  # Em uma escala de 1 a 5

resultado = avaliar_trabalho(tempo_exemplo_dias, qualidade_exemplo)
print(resultado)
