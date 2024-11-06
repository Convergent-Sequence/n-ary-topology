# Calculadora espacios topológicos $n$-arios y espacios topológicos usuales

Aquí encontrará una explicación detallada de cómo ejecutar los algoritmos presentados, en un notebook de Google Colab.

Cómo el título lo indica, usted contará con una ''calculadora'' tanto para espacios topológicos $n$-arios ($n\geq 2$) como para espacios topológicos usuales, con la cual podrá realizar lo siguiente:

- Verificar si una colección es una topología.
- Obtener la clausura y el interior de un conjunto dado.
- Generar una topología a partir de una subbase.

### Configuración de Colab


Para poder usar las funciones, debe configuar el notebook de Colab en el cual trabajará. Para ellos, diríjase a ... y ejecute una celda con el siguiente codigo

```python
#Clonamos el repositorio 
!git clone https://github.com/Convergent-Sequence/n-ary-topology.git

#Cambiamos el directorio al repositorio
%cd n-ary-topology

#Importamos las funciones
import ntop
```

La ejecución de esta celda, debería retornar el siguiente mensaje.

```
Cloning into 'n-ary-topology'...
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (6/6), done.
/content/n-ary-topology/n-ary-topology
```

### Funciones para espacios topológicos $n$-arios

Tenga en cuenta que los conjuntos $n$-arios son listas de conjuntos. Por ejemplo el conjunto binario $(\set{c_1}, \set{p_1})$
 estaría dado por ```[{'c_1'},{'p_1'}]```, y el conjunto 5-ario $(\set{a_3}, \set{b_1, b_2}, \set{c_3, c_4}, \set{d_1}, \set{e_1, e_2})$
 estaría dado por ```[{'a_3'}, {'b_1', 'b_2'}, {'c_3', 'c_4'}, {'d_1'}, {'e_1', 'e_2'}] ```.
 
Para poder usar las funciones debemos definir un espacio topológico $n$-ario y sus respectivos conjuntos subyacentes, los cuales usaremos como conjuntos de python.
Por ejemplo, podemos definir el siguiente espacio topológico $n$-ario.

```python
X1 = {'a', 'b','c','d','e'}

X2 = {1,2,3,4,5,6}

top1 = [[{'a'}, {1, 2, 3, 4, 5, 6}],[{'d'}, {1, 2, 3, 4, 5, 6}],
 [{'e'}, {1, 2, 3, 4, 5, 6}],[{'b', 'c'}, {2, 3}],
 [set(), {1, 2, 3, 4, 5, 6}],[set(), {2, 3}],[{'a', 'd'}, {1, 2, 3, 4, 5, 6}],
 [{'a', 'e'}, {1, 2, 3, 4, 5, 6}],[{'a', 'b', 'c'}, {1, 2, 3, 4, 5, 6}],
 [{'d', 'e'}, {1, 2, 3, 4, 5, 6}],[{'b', 'c', 'd'}, {1, 2, 3, 4, 5, 6}],
 [{'a', 'd', 'e'}, {1, 2, 3, 4, 5, 6}],[{'a', 'b', 'c', 'd'}, {1, 2, 3, 4, 5, 6}],
 [{'b', 'c', 'e'}, {1, 2, 3, 4, 5, 6}],[{'a', 'b', 'c', 'e'}, {1, 2, 3, 4, 5, 6}],
 [{'b', 'c', 'd', 'e'}, {1, 2, 3, 4, 5, 6}],[{'a', 'b', 'c', 'd', 'e'}, {1, 2, 3, 4, 5, 6}],
 [{'b', 'c'}, {1, 2, 3, 4, 5, 6}],[set(), set()]]
```

Ahora, para calcular el interior o la clausura de un conjunto $n$-ario, debemos llamar la función  ```ntop.interior()``` o la funcion ```ntop.closure()```, la función ```ntop.interior()``` recibe como parámetros la topología $n$-aria que hayamos definido y el conjunto $n$-ario al cual le deseamos calcular el interior, y la función ```ntop.closure()``` recibe como parámetros la topología $n$-aria que hayamos definido, el conjunto $n$-ario al cual le deseamos calcular la clausura y los conjuntos subyacentes. Por ejemplo, para obtener la clausura y el interior de $(\set{b,c},\set{2,3,5})$, lo haríamos de la siguiente forma.


```python
interior1 = ntop.interior(top1,[{'b','c'},{2,3,5}])
closure1 = ntop.closure(X1,X2,M=top1,nelement=[{'b','c'},{2,3,5}])
print(interior1, closure1)
```
Para verificar que top1 es efecto una topologia binaria, debemos llamar la función ```ntop.is_n_ary_topology()```, la cual toma por parámetros los conjuntos subyacentes y la topología a verificar, así: ```ntop.is_n_ary_topology(X1,X2,M=top1)```.

Finalmente, para generar una topología $n$-aria a partir de una subbase, demos llamar la función ```ntop.generate_n_ary_topology()``` la cual resibe como parámetros los conjuntos subyacentes y la subbase, por ejemplo, para generar la topología binaria definida anteriormente, lo pdemos hacer por medio de la subbase $\Delta =  \set{(\set{a}, X_2),(\set{d}, X_2),(\set{e}, X_2),(\set{b,c},\set{2,3})}$, así.

```python
delta = [[{'a'}, X2],[{'d'}, X2],[{'e'}, X2],[{'b','c'},{2,3}]] 
top2 = ntop.generate_n_ary_topology(X1,X2,delta=delta)
top2
```

### Funciones para espacios topológicos usuales

Para el caso de espacios topológicos usuales, los conjuntos serán conjuntos de python, y las colecciones serán listas de conjuntos.
Por ejemplo, podemos definir el siguiente espacio topológico.

```python
z = {'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7'}

top3 = [{'p1', 'p5', 'p6'},{'p2', 'p5', 'p6'},{'p3', 'p5', 'p6'},{'p1', 'p3', 'p4', 'p5', 'p6', 'p7'},
 {'p5', 'p6'},{'p1', 'p3', 'p5', 'p6', 'p7'},{'p2', 'p3', 'p5', 'p6', 'p8'},{'p1', 'p2', 'p5', 'p6'},
 {'p1', 'p2', 'p3', 'p5', 'p6', 'p7', 'p8'},{'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'},{'p1', 'p3', 'p5', 'p6'},
 {'p1', 'p2', 'p3', 'p5', 'p6', 'p8'},{'p2', 'p3', 'p5', 'p6'},z,
 {'p1', 'p2', 'p3', 'p5', 'p6', 'p7'},{'p1', 'p2', 'p3', 'p5', 'p6'},set()]
```

Ahora, para calcular el interior o la clausura de un conjunto dado, debemos llamar la función  ```ntop.usual_interior()``` o la funcion ```ntop.usual_closure()```, ambas funciones reciben como parámetros la topología usual que hayamos definido, el conjunto al cual le deseamos calcular el interior o la clausura, y el conjunto subyacente. Por ejemplo, para obtener la clausura y el interior de $\set{p_4, p_5, p_7, p_8}$, lo haríamos de la siguiente forma.


```pythoninterior2 = ntop.usual_interior(z=z, tau=top3, s={'p4', 'p5', 'p7', 'p8'})
closure2 = ntop.usual_closure(z=z, tau=top3, s={'p4', 'p5', 'p7', 'p8'})
print(interior2, closure2)
```
