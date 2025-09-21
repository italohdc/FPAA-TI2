import typer


def ordenar_maxmin_select(numbers: list[int]) -> tuple[int, int]:
  # Passo 1: Obter o número de elementos na lista
  num_items = len(numbers)

  # Caso base 1: Se há apenas 1 elemento, ele é tanto o menor quanto o maior
  if num_items == 1:
    return (numbers[0], numbers[0])

  # Caso base 2: Se há 2 elementos, compara e retorna ordenados (menor, maior)
  if num_items == 2:
    if numbers[0] > numbers[1]:
      return (numbers[1], numbers[0])
    else:
      return (numbers[0], numbers[1])

  # Passo 2: Dividir a lista em duas metades (divide-and-conquer)
  metade = num_items // 2
  array_1 = numbers[:metade]
  array_2 = numbers[metade:]

  # Passo 3: Resolver recursivamente para cada metade
  array_1_min, array_1_max = ordenar_maxmin_select(array_1)
  array_2_min, array_2_max = ordenar_maxmin_select(array_2)

  # Passo 4: Combinar os resultados comparando os mínimos e máximos das duas metades
  menor = array_1_min if array_1_min < array_2_min else array_2_min
  maior =  array_1_max if array_1_max > array_2_max else array_2_max

  # Passo 5: Retornar o menor e maior elemento encontrados
  return (menor, maior)


def main(numbers: list[int]):
  menor, maior = ordenar_maxmin_select(numbers)
  print(f"Menor: {menor}, Maior: {maior}")


if __name__ == "__main__":
  typer.run(main)
