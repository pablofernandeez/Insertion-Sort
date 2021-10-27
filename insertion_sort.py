# -*- coding: utf-8 -*-
"""Insertion Sort.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GKQwAUAOJMmlr3DdlKoppk48d8yFzvJ7

#<center>**Insertion Sort-Algoritmo de Inserción**

**Antonio Sevillano, Pablo Fernández**

##**Introducción**

El Algoritmo de Inserción es un algoritmo de ordenación en el que se compara uno de los elementos del vector con el resto. A este elemento se le llama llave. Conforme se va ordenando, la llave va cambiando hasta finalmente obtener el vector completamente ordenado.

<p style='text-align: justify;'> El algoritmo definitivo está formado por un bucle, pero para comprender su funcionamiento, vamos a realizar la ordenación del vector [9, 5, 1, 4, 3] paso a paso. Para ello, hemos escrito en código cada iteración del bucle, de forma que quede de forma mucho más gráfica cómo funciona el algoritmo de inserción. </p>

###**Funcionamiento del algoritimo de inserción**
<p style='text-align: justify;'> Una vez definido el vector "data" que vamos a ordenar, obtenemos la primera llave o "key" del algoritmo. Como el algoritmo funciona comparando la llave con los elementos de su izquierda, la primera llave se corresponde con el segundo elemento del vector ([1]='5')  </p>
<p style='text-align: justify;'> Comparamos la llave con el elemento de su izquiera, en este caso, como la llave es menor que el primer elemento ([0]=9), intercambia de posición el '5' y el '9'.  </p>
"""

data = [9, 5, 1, 4, 3]
step = 1
key = data[step]
j = step-1

while j >= 0 and key < data[j]:
      data[j + 1] = data[j]
      j = j - 1
      data[j + 1] = key
print(data)

"""Ahora ya sabemos que los dos primeros elementos del vector están ordenados. La siguiente llave se corresponderá con el tercer elemento del vector. Su valor es '1'. Este tercer elemento, lo situaremos justo antes del siguiente elemento que tenga un valor más pequeño que él. Si no se da el caso (como ocurre en este ejemplo), lo colocaremos al comienzo del vector."""

data = [5, 9, 1, 4, 3]
step = 2
key = data[step]
j = step-1

while j >= 0 and key < data[j]:
      data[j + 1] = data[j]
      j = j - 1
      data[j + 1] = key
print(data)

"""Como se puede observar ya están ordenados los tres primeros elementos [1, 5, 9, 4, 3] por lo que la nueva llave será el cuarto elemento del vector. Desplazamos a la derecha el '9' y el '5' porque son mayores que el '4'. El '1' al ser menor se quedará a su izquierda. La nueva posición del '4' será la posición [1].

"""

data = [1, 5, 9, 4, 3]
step = 3
key = data[step]
j = step-1

while j >= 0 and key < data[j]:
      data[j + 1] = data[j]
      j = j - 1
      data[j + 1] = key
print(data)

"""Finalmente, queda por ordenar el último elemento del vector. Repetimos el proceso. En esta ocasión se desplazan a la derecha el '4', '5' y '9' y el tres se situa entre el '1' y el '4' quedando el vector completamente ordenado."""

data = [1, 4, 5, 9, 3]
step = 4
key = data[step]
j = step-1

while j >= 0 and key < data[j]:
      data[j + 1] = data[j]
      j = j - 1
      data[j + 1] = key
print(data)

"""La generalización del algoritmo sería la siguiente. Se utiliza un bucle para ir cambiando automáticamente los valores de las llaves."""

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)

"""###**Complejidad del algoritmo**
<p style='text-align: justify;'> Al haber dos bucles, la complejidad media es de O(n^2). Se podría dar el caso de que el vector ya estuviera ordenado y por lo tanto no hiciera falta entrar en el 'while'. Si esto ocurriera, su complejidad sería O(n), sin embargo, lo normal es que sea necesario utilizar los dos bucles por lo que su complejidad media es O(n^2).  </p>
<p style='text-align: justify;'> También podemos estudiar su complejidad a través de la función de coste temporal. Para ello, estudiamos los bucles y cómo recorren el vector. </p>
<p style='text-align: justify;'> En primer lugar, el for, recorre el vector desde la primera posición hasta la última por lo que podemos decir que tiene 'n' iteraciones. Además tiene tres lineas de código luego podríamos multiplicar 'n' por la constante 3.  </p>
<p style='text-align: justify;'> En segundo lugar, el while, al igual que el for, recorre todo el vector por lo que podemos decir que también tiene 'n' iteraciones. Como ocurre en el for, tiene tres líneas de código luego también podemos multiplicar la 'n' por la constante 3. </p>
<p style='text-align: justify;'> El resultado de multiplicar los dos bucles sería 9n^2. Es cierto que cuanto más grande sea el vector a ordenar la constante es más despreciable pero siendo rigurosos, esta es la función temporal; aunque cada línea de código requerirá un tiempo de procesado diferente que habría que tener en cuenta. De esta función se puede observar claramente que su complejidad es O(n^2). </p>
"""