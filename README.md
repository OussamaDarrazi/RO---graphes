# RO-graphes
![image](https://github.com/OussamaDarrazi/RO-graphes/assets/34890717/5a3c8204-e609-485e-8cc5-2d492b3776d5)

### La matrice ci-dessus representée par notre class
```python
graphe = Graphe(("a", "b", "c", "d", "e", "f", "g", "h"),
                [[0, 10, 11, 2, 0, 0, 0, 0],
                 [0, 0, 0, 0, 7, 0, 0, 0],
                 [0, 1, 0, 0, 4, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 3, 0],
                 [0, 0, 0, 0, 0, 1, 0, 6],
                 [0, 0, 2, 0, 3, 0, 0, 8],
                 [0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 5]])
```

#### Pour trouver les plus cours chemins du sommets "a" vers les autres sommets:
```python
print(graphe.dijkstra("a"))
```

### Output:
```python
{'PCC': [0, 7, 6, 2, 3, 4, 5, 9], 'Predecesseurs': ['a', 'c', 'f', 'a', 'd', 'e', 'd', 'e']}
```
