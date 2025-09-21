# FPAA-TI2

> **Fundamentos de Programação e Algoritmos Avançados**
> 
> Trabalho Individual 2 - Implementação do Algoritmo de Seleção
Simultânea do Maior e do Menor Elementos (MaxMin Select) em Python


## Descrição do projeto


### Explicação do código

No código, o algoritmo está implementado na função `def ordenar_maxmin_select(numbers: list[int]) -> tuple[int, int]`.
Essa função recebe uma lista de números inteiros e retorna uma
tupla contendo o menor e maior elemento utilizando o algoritmo MaxMin Select.

Como trata-se de um código pequeno, foi escolhido deixar todo o
conteúdo somente no arquivo main.py. Dessa forma, fica mais fácil
de entender e manter o código.

Abaixo, explico cada passo do código:

`Linha 8`: Casos base

Tratam-se dos casos base do algoritmo. Como trata-se de um algoritmo
recursivo, é necessário existir casos base para finalizar a recursão.

No primeiro caso base, se há apenas 1 elemento na lista, esse elemento
é tanto o menor quanto o maior, então retorna uma tupla com o mesmo valor.

No segundo caso base, se há 2 elementos, compara ambos e retorna
ordenados como (menor, maior).

`Linha 5`: Passo 1

O número de elementos da lista é obtido para determinar como proceder
com o algoritmo. Essa informação é utilizada para identificar os casos
base e para dividir a lista posteriormente.

`Linha 19`: Passo 2

A lista é dividida em duas metades utilizando a estratégia de dividir e
conquistar. A primeira metade contém os elementos do início até a metade,
e a segunda metade contém os elementos restantes.

`Linha 24`: Passo 3

Os menores e maiores elementos são encontrados recursivamente para cada
metade da lista. Isso permite que o algoritmo processe sublistas menores
até chegar aos casos base.

`Linha 28`: Passo 4

Os resultados das duas metades são combinados comparando os valores mínimos
e máximos encontrados em cada metade. O menor entre os dois mínimos e o
maior entre os dois máximos são selecionados.

`Linha 32`: Retorno do resultado

O resultado final é retornado como uma tupla contendo o menor e maior
elemento de toda a lista original.



## Como executar o projeto

Este projeto utiliza Python. Para rodar o projeto, você precisa ter
o Python instalado na sua máquina. Foi utilizado, durante o
desenvolvimento, o Python 3.13. Recomendo a utilização do
[PyEnv](https://github.com/pyenv/pyenv) para instalar e gerenciar as
versões do Python.

### Configurar ambiente virtual

Para configurar um ambiente virtual, você pode usar o `venv`.
Execute os seguintes criar e rodar um novo `venv`:

```
# Criar novo venv
python -m venv venv

# Executar o venv
source venv/bin/activate  # No Linux ou macOS
venv\Scripts\activate  # No Windows
```

### Instalar Dependências

Para instalar as dependências do projeto, execute o seguinte
comando na raiz do projeto:

```
pip install -r requirements.txt
```

### Sobre as dependências

Para este projeto, foram utilizadas algumas dependências para
auxiliar no desenvolvimento. Dentre elas:

[`typer`](https://typer.tiangolo.com/): Biblioteca para a criação
de CLI (Interfaces de Linha de Comando). Utilizada para facilitar
a inserção dos números a serem multiplicados.


### Rodar o projeto

Para rodar o projeto, você pode utilizar o seguinte comando:

```
# Comando
python main.py <NÚMERO_1> <NÚMERO_2> <NÚMERO_3> ... <NÚMERO_N>

# Exemplo
python main.py 1 9 3 7 50 25 100
```



## Relatório Técnico

