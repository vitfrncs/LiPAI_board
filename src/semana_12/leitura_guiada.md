## *Introdução (Seção 1)* 

### Qual é a principal limitação das CNNs de classificação (como a VGG) quando aplicadas a tarefas de predição densa (pixel a pixel)?

A principal limitação é que as CNNs de classificação exigem entradas de tamanho fixo e suas camadas fully connected possuem dimensões fixas, o que resulta na perda de coordenadas espaciais e impede a predição densa em cada pixel.

### Qual é a "intuição chave" (key insight) que os autores propõem para superar essa limitação?

A intuição chave é construir redes totalmente convolucionais(FCNs) que aceitam entradas de tamanho arbitrário e produzem saídas de tamanho correspondente, o que permite inferência e aprendizado eficientes pixels a pixels.

### Como os autores propõem resolver a tensão entre a informação semântica (global) e a informação de aparência (local)?

Eles propõem uma nova arquitetura skip para combinar a informação semântica de uma camada profunda e grosseira com a informação de aparência de uma camada rasa e fina, visando produzir segmentações precisas e detalhadas.

## *Redes Totalmente Convolucionais (Seção 3)*

### Como exatamente os autores convertem uma camada fully connected (totalmente conectada) em uma camada convolucional? 


### Qual é o problema da saída de uma rede "convolucionalizada" (como descrito na Seção 3.1) e por que o upsampling é necessário? 

O problema é que a saída da rede é grosseira devido ao subsampling (pooling) da rede original, e o upsampling é necessário para conectar essas saídas de volta aos pixels originais da imagem para a predição densa.


### O que é a "convolução transposta" (ou deconvulução) e por que ela é preferível a uma interpolação simples (como a bilinear)? 



### Por que os autores argumentam que treinar com a imagem inteira é mais eficiente que o treinamento com patches? 



## *Arquitetura de Segmentação (Seção 4)* 

### Qual é a arquitetura da FCN-32s? Por que sua saída, mesmo após o upsampling, é considerada "insatisfatoriamente grosseira"?


### Como a FCN-16s melhora a FCN-32s? Qual informação da rede ela está "resgatando"?


### Explique a arquitetura da FCN-8s. Como ela combina informações de três escalas diferentes?



## *Resultados (Seção 5)*

### Quais foram os ganhos (em mIU) obtidos no PASCAL VOC 2012 em comparação com o método SDS?

### Qual foi o impacto das skip connections no desempenho (comparando FCN-32s, FCN-16s e FCN-8s na Tabela 2)?

### Além da precisão, qual outra grande vantagem a FCN demonstrou ter sobre os métodos concorrentes?

## *Após a leitura* 

### Qual você considera ser a principal contribuição deste artigo: a "convolucionalização" (Seção 3.1), o upsampling aprendível (Seção 3.3) ou as skip connections (Seção 4.2)?

### O que os autores querem dizer com "treinamento end-to-end, pixels-to-pixels"?  Por que isso foi um avanço tão significativo?
