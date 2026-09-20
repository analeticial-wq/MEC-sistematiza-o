**Dataset usado:** https://www.kaggle.com/datasets/serkantysz/annas-archive-top-10k-spotify-songs-metadata-2025

Eu escolhi esse dataset por cumprir com o tamanho exigido pelo professor e por conter dados sobre assuntos do meu interesse, o que deixaria a tarefa mais atrativa de fazer e também mais fácil, por conter dados que eu consigo compreender bem.

Eu decidi fazer as estatísticas em uma classe, pois sou mais acostumada com Java e, no momento de imaginar o trabalho, fiz o rascunho conforme eu faria em Java. Então, é uma classe com os métodos para calcular média, moda e mediana, para que eu consiga chamá-los em outras classes, como a classe `main`, onde está o menu.

As fórmulas usadas foram:

**Média**

Usei a média para calcular a duração média das músicas, em segundos.

x̄ = (x₁ + x₂ + ... + xₙ) / n

**Mediana**

Usei a mediana para encontrar o valor central da duração das músicas, sem sofrer influência de durações muito longas ou muito curtas.

Se n for ímpar:

Md = x₍ₙ₊₁₎/₂

Se n for par:

Md = (xₙ/₂ + xₙ/₂₊₁) / 2

**Moda**

Usei a moda para encontrar a duração de música que mais se repete no dataset.

Mo = valor x com a maior frequência f(x) entre todos os valores.

**Porcentagem**

Usei a porcentagem para calcular, por exemplo, quantas músicas se enquadram em cada faixa de duração.

P = (parte / total) × 100



## Descobertas

###  Música
musicas entre 3 e quatro munitos são as com maior número de produções de acordo com esse dataset

<img width="621" height="554" alt="image" src="https://github.com/user-attachments/assets/8a646fcc-6939-4f2c-b824-3278df73bd6e" />



###  Artista
Drake é o artista com mais músicas presentes no top 10k do dataset, com 121 faixas diferentes 

<img width="631" height="541" alt="image" src="https://github.com/user-attachments/assets/92d5186f-2ca3-4230-a33d-b859921831e3" />


### 📊 Geral
Ao sortear 1000 músicas aleatórias do dataset, cerca de 71% delas têm mais de 3 minutos de duração, um número muito próximo da proporção real do dataset inteiro
<img width="568" height="184" alt="image" src="https://github.com/user-attachments/assets/859e84a2-21a8-4d75-a174-d0c16da99e38" />
