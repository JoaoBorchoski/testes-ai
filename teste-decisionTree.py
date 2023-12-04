# from sklearn import tree

# x = [[140, 1], [130, 1], [150, 0], [170, 0]]
# y = [5, 5, 10, 10]

# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(x, y)

# print(clf.predict([[100, 1]]))

# Importando as bibliotecas necessárias
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Gerando dados de exemplo
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Dividindo os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Criando e treinando o modelo de Regressão Linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazendo previsões no conjunto de teste
y_pred = model.predict(X_test)

# Avaliando o desempenho do modelo
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Visualizando os resultados
import matplotlib.pyplot as plt

plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, y_pred, color="blue", linewidth=3)
plt.title("Regressão Linear - Exemplo Simples")
plt.xlabel("Variável Independente")
plt.ylabel("Variável Dependente")
plt.savefig("regressao_linear_plot.png")
