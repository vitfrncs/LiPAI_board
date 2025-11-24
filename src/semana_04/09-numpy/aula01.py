import numpy as np

# array

arr = np.array([10, 20, 30, 40, 50, 60])                 # cria array 1D com múltiplos de 10
np.zeros((3, 2))                                         # matriz 3x2 preenchida com zeros
np.ones((2, 4))                                          # matriz 2x4 preenchida com uns
np.full((3, 3), 7)                                       # matriz 3x3 preenchida com o número 7
np.eye(4)                                                # matriz identidade 4x4
np.arange(5, 25, 5)                                      # array de 5 a 20 com passo 5 → [5,10,15,20]
np.linspace(2, 8, 4)                                     # 4 valores entre 2 e 8 igualmente espaçados

arr.shape                                                # retorna (6,) → vetor com 6 elementos
arr.reshape((3, 2))                                      # muda o formato para 3 linhas e 2 colunas
arr.flatten()                                            # transforma qualquer array em vetor 1D
arr.T                                                    # transposta (não muda vetor 1D)
np.expand_dims(arr, axis=1)                              # adiciona uma dimensão (vira matriz 6x1)

np.sum(arr)                                              # soma todos os valores do array
np.mean(arr)                                             # calcula a média dos elementos
np.std(arr)                                              # desvio padrão dos elementos
np.min(arr), np.max(arr)                                # menor e maior valor do array
np.argmin(arr), np.argmax(arr)                          # índice do menor e do maior valor
np.prod(arr)                                             # produto de todos os elementos

arr > 35                                                 # retorna array de booleanos onde valor > 35
np.where(arr < 40, -1, 1)                                # -1 se valor < 40, senão 1
np.any(arr == 30)                                        # retorna True se algum valor for 30
np.all(arr % 10 == 0)                                    # verifica se todos são múltiplos de 10
arr[arr <= 30]                                           # filtra elementos menores ou iguais a 30

np.unique([1, 2, 2, 3, 3, 3])                            # retorna os valores únicos → [1, 2, 3]
np.sort(np.array([30, 10, 20]))                          # ordena os valores → [10, 20, 30]
np.argsort(np.array([30, 10, 20]))                       # índices da ordenação → [1, 2, 0]
np.clip(np.array([0, 5, 10]), 3, 8)                      # valores limitados entre 3 e 8 → [3, 5, 8]

#random

np.random.seed(123)                                      # fixa a aleatoriedade para reprodutibilidade

np.random.randint(1, 100, (3, 2))                         # matriz 3x2 com inteiros entre 1 e 99
np.random.rand(3, 3)                                      # matriz 3x3 com floats uniformes entre 0 e 1
np.random.randn(5)                                       # vetor com 5 valores da distribuição normal
np.random.uniform(0.5, 1.5, size=(2, 2))                  # floats entre 0.5 e 1.5
np.random.choice([100, 200, 300], size=2, p=[0.2, 0.5, 0.3])  # escolhe 2 valores com probabilidades dadas
