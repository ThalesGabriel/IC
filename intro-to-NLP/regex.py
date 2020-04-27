import re


sentence = "The PlayStation 5 (PS5) is an upcoming home video game console developed by Sony Interactive Entertainment. Announced as the successor to the PlayStation 4 in 2019, its launch is scheduled for late 2020."

patternMatch = "The"
patternSearch = "PlayStation"
patternFindAll = "PlayStation"


"""
  1. Se quisermos saber se uma palavra inicia a string podemos utilizar a função match, porém se tentarmos encontrar 
  algo que esteja além da primeira palavra a função match não irá performar

  2. Se quisermos encontrar a primeira ocorrência de uma palavra na sentença, devemos usar a função search

  3. Se quisermos encontrar todas as ocorrências de uma palavra na sentença, devemos utilizar o findAll e irá nos
  retornar uma lista

  4. Se quisermos encontrar o indice de todas as ocorrências de uma palavra em uma sentença devemos utilizar a função
  findIter, este nos retornar um objeto iterável com um for
    OBS. Utilize start para descobrir o index inicio das ocorrencias
    OBS. Utilize end para descobrir o index final das ocorrencias

  Obs. Para retornar o valor, devemos utilizar o group(0)

"""

matchFind = re.match(patternMatch, sentence)
matchSearch = re.search(patternSearch, sentence)
matchFindAll = re.findall(patternFindAll, sentence)
matchIter = re.finditer(patternFindAll, sentence)
print(matchFind.group(0), matchFind)
print()
print(matchSearch.group(0), matchSearch)
print()
print(matchFindAll)
print()
for match in matchIter:
  print(match.start(), match.end())


