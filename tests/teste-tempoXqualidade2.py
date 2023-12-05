from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import numpy as np


# Função para treinar o modelo
def treinar_modelo(X, y):
    # Crie um modelo de regressão logística
    modelo = make_pipeline(StandardScaler(), LogisticRegression())

    # Treine o modelo
    modelo.fit(X, y)

    return modelo


# Função para avaliar o trabalho com o modelo treinado
def avaliar_trabalho_com_modelo(modelo, tempo_em_dias, qualidade, limiar=0.5):
    # Transforme os dados de entrada
    dados = np.array([[tempo_em_dias, qualidade]])
    dados_transformados = modelo.named_steps["standardscaler"].transform(dados)

    # Faça a previsão de probabilidade com o modelo treinado
    probabilidade = modelo.predict_proba(dados_transformados)[:, 1]

    # Compare a probabilidade com o limiar para decidir se o trabalho é bom ou precisa ser melhorado
    if probabilidade >= limiar:
        return "Trabalho bom!"
    else:
        return "Trabalho a ser melhorado."


# Exemplo de uso
# Vamos criar um conjunto de dados fictício para treinar o modelo
X_treino = np.array([[10, 5], [30, 3], [15, 4], [50, 2]])
y_treino = np.array([1, 0, 1, 0])

# Treine o modelo com os dados fictícios
modelo_treinado = treinar_modelo(X_treino, y_treino)

# Avalie o trabalho com base no modelo treinado
tempo_exemplo_dias = 25
qualidade_exemplo = 2
resultado = avaliar_trabalho_com_modelo(
    modelo_treinado, tempo_exemplo_dias, qualidade_exemplo, limiar=0.3
)

print(resultado)
