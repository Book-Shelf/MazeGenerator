# Maze generator

Cały program składa się z 3 plików:
+ main.py - miejsce gdzie odpalamy nasz program
+ maze_generator.py - moduł z implementacją algorytmu DFS i tworzeniem gifa za pomocą tworzenia obrazków png, a następnie ich sklejania
+ maze_generator_animation.py - moduł z implementacją algorytmu DFS i tworzeniem gifa za pomocą matplotlib.animation

Dodatkowo w folderze w którym odpalamy nasz program musi znaleźć się folder "maze" do którego będą zapisywane poszczególne klatki gifa.

![gif](maze.gif "50x50")
![gif](Maze_10x10.gif "10x10")

## Generowanie labiryntu

Poszczególne opcje wygenerowania labiryntu są oznaczone w pliku main.py tj.
+ Recursive option
+ Iterative option

Należy odkomentować poszczególną sekcje w celu jej uruchomienia.

***Grid(width, height, (x, y))***

Inicjalizacja tablicy o rozmiarach ```width``` x ```height```. 
(x, y) służy ku wskazaniu punktu startowego skąd generowanie labiryntu ma się rozpocząć. <br>
0 <= x < width <br>
0 <= y < height

***Grid.generate_maze_iter(saveSteps=False)***

Rozpoczęcie generowania labiryntu algorytmem DFS z punktu ```Grid.start```. <br>
> **saveSteps** <br>
> + **False** - kroki algorytmu nie zostaną zapisane co wiąże się z niemożliwością stworzenia gifa
> + **True** - kroki algorytmu zostaną zapisane dzięki czemu stowrzenie gifa będzie możliwe 

***Grid.\_\_str\_\_()***

Na podstawie tablicy ```Grid.maze_map``` tworzona jest tablica o wartościach: <br>
"#" - ściana <br>
" " - ścieżka <br>
"." - ścieżka, komórka znajduje się na stosie 

***maze_generator_animation.Grid.show(title="maze", save=False, fps=60)***

Wyświetla wygenerowany labirynt oraz jeśli potwierdzono zapisuje go do aktualnego folderu.
> **title** <br>
>  Nazwa zapisanego labiryntu/gifu <br>
> **save** <br>
>  Czy zapisać wygenerowany labirynt <br>
> **fps** <br>
>  Szybkość animacji

***maze_generator.Grid.show(save=False, title="maze")***

Wyświetla wygenerowany labirynt oraz jeśli potwierdzono zapisuje go do aktualnego folderu.
> **title** <br>
>  Nazwa zapisanego labiryntu <br>
> **save** <br>
>  Czy zapisać wygenerowany labirynt <br>

***createGif(title)***

Tworzy gif w aktualnym folderze
> **title** <br>
>  Nazwa zapisanego gifu <br>

### Recursive option

Wersja rekurencyjna Jest mniej wydajna niż iteracyjna stąd jest ona tylko w celu zaprezentowania jej implementacji. W celu wygenerowania dużego labiryntu należy powiększyć limit rekurencyjny pythona. Należy jednak uważać bo może to doprowadzić do szybkiego wyczerpania zasobów.

