import typer


def ordenar_maxmin_select(numbers: list[int]) -> tuple[int, int]:
  num_items = len(numbers)

  if num_items == 1:
    return (numbers[0], numbers[0])

  if num_items == 2:
    if numbers[0] > numbers[1]:
      return (numbers[1], numbers[0])
    else:
      return (numbers[0], numbers[1])

  metade = num_items // 2
  array_1 = numbers[:metade]
  array_2 = numbers[metade:]

  array_1_min, array_1_max = ordenar_maxmin_select(array_1)
  array_2_min, array_2_max = ordenar_maxmin_select(array_2)

  menor = array_1_min if array_1_min < array_2_min else array_2_min
  maior =  array_1_max if array_1_max > array_2_max else array_2_max

  return (menor, maior)


def main(numbers: list[int]):
  menor, maior = ordenar_maxmin_select(numbers)
  print(f"Menor: {menor}, Maior: {maior}")


if __name__ == "__main__":
  typer.run(main)
