def sequential_search(deret, karakter):
  """Melakukan pencarian sequential pada deret untuk menemukan karakter

  Args:
    deret: Deret karakter yang akan dicari
    karakter: Karakter yang ingin dicari

  Returns:
    Indeks dari karakter jika ditemukan, -1 jika tidak ditemukan
  """

  for i in range(len(deret)):
    if deret[i] == karakter:
      return i
  return -1

# Contoh penggunaan
deret = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
karakter_yang_dicari = 'g'

hasil = sequential_search(deret, karakter_yang_dicari)

if hasil != -1:
  print(f"Karakter '{karakter_yang_dicari}' ditemukan pada indeks {hasil}")
else:
  print(f"Karakter '{karakter_yang_dicari}' tidak ditemukan")