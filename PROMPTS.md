# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**: 
Chat integrado de VSC, en forma auto.
**Prompt usado**:
> El archivo varibles.py contiene 5 funciones definidas pero no implementadas, necesito implementar cada una de ellas de la siguiente manera: para la funcion "crear_saludo" se requiere retornar por pantalla el mensaje "Hola, [nombre]!", siendo [nombre] el argumento que recibe la funcion, este es de tipo string; para la funcion "suma_enteros" se requiere retornar la suma de 2 argumentos de tipo int, en el mismo formato; para la funcion "es_mayor_de_edad", se requiere retornar, en formato boolean, si el numero en el argumento, de tipo int, es mayor a un numero arbitrario, en este caso 18, en caso contrario, se debe retornar un false; para la funcion "tipo_de_dato" se presenta un argumento de tipo indefinido (puede ser cualquiera) y se necesita retornar el nombre del tipo de dato(int, string, boolean, etc); y finalmente, para la funcion "convertir_a_float" se recibe argumentos de tipo string y se desea convertirlos y retornarlos en formato float, en caso de no recibir argumentos de tipo string, no se debe hacer nada.

**Resultado obtenido**:
se implemento las funciones de manera correcta, aunque utilizando condiciones que no conozco, como "isinstance(valor, value):"

**¿Lo usaste tal cual o lo modificaste?**
Lo use tal cual

---

### 2 - condicionales.py

**Herramienta**: 
Chat integrado de VSC, en forma auto.
**Prompt usado**:
> El archivo condicionales.py contiene 4 funciones definidas y sin implementar, se requiere definir su funcionalidad de la siguiente manera: la funcion "clasificar_numero" retorna el mensaje "positivo", "negativo" o "cero" por pantalla segun el valor del parametro establecido, de tipo int, necesito establecer que, para los valores mayores que cero, se muestre el mensaje "positivo", para los valores menores que cero, se muestre el mensaje "negativo" y si el valor es igual a cero, entonces que se muestre el mensaje "cero"; para la funcion "mayor_de_tres", se necesita comparar 3 parametros dados a la funcion, todos de tipo int, y retornar el mayor de los 3 en el mismo formato, en caso de que todos los valores sean iguales, se debe retornar un cero; para la funcion "clasificar_nota", se recibe como paramentro un valor de tipo float y se debe mostrar por pantalla un mensaje de acuerdo a la siguiente comparacion: si el valor es menor a 6, se debe retornar el mensaje "desaprobado", si el valor es mayor o igual a 6, se debe retornar "aprobado", si el valor es mayor o igual a 7, se debe retornar "bueno" y si el valor es mayor o igual a 9, se debe mostrar "sobresaliente"; para la ultima funcion "es_bisiesto" se recibe como parametro un valor de tipo int y se retorna un valor booleano, el booleano sera verdadero cuando el valor ingresado sea divisible por 4, excepto los divisibles por 100, salvo que tambien lo sean por 400, en caso contrario, se debe retornar falso

**Resultado obtenido**:
Se obtuvo lo descrito, salvo los casos en los que el valor puede ser negativo cuando no tiene sentido que lo sea (clasificar_nota)

**¿Lo usaste tal cual o lo modificaste?**
Lo use tal cual

---

### 3 - listas.py

**Herramienta**: 
Chat de VSC
**Prompt usado**:
> El archivo listas.py contiene 5 funciones a implementar de la siguiente manera: para la funcion "suma_lista" se recibe como parametro una lista y se desea retornar la suma de todos sus elementos en formato int o float, si los elementos de la lista son de tipo string o boolean, no deben sumarse; para la funcion "filtrar_pares" se desea retornar, dada una lista como paramentro, una nueva lista con solamente los numeros pares; para la funcion "invertir_lista" se recibe como parametro una lista y se requiere retornar la lista invertida sin modificar la original; para la funcion "eliminar_duplicados" se requiere eliminar todos los elementos duplicados de una lista dada como parametro, sin modificar el orden de aparicion; para la funcion "aplanar_lista" se evalua una lista de listas y se requiere retornar todos los elementos de todas las listas en una unica lista, respetando el orden de aparicion.

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**
no lo modifique

---

### 4 - diccionarios.py

**Herramienta**: 
Chat de VCS en auto
**Prompt usado**:
> El archivo diccionarios.py contiene 4 funciones definidas, mas no implementadas, se requiere implementar las funciones de la siguiente manera: para la funcion "contar_palabras", se recibe como parametro un texto de tipo string y lo retorna en formato dict, para el parametro ingresado, se lo debe pasar todo a minuscula y se desea contar la cantidad de palabras iguales que hay en en el texto, y mostrarlo por pantalla; para la funcion "invertir_diccionario", se recibe como parametro un diccionario y se retorna otro en igual formato, la funcionalidad consiste en cambiar palabras, letras o claves por otras definidas de manera arbitraria, en este caso, cambiaremos todas las letras "a" por una "e"; para la funcion "merge_diccionarios", se reciben 2 diccionarios distintos y se retorna uno con la combinacion de ambos, con la condicion de que, si hay palabras o claves repetidas, prevalece solo la del segundo diccionario ingresado; para la funcion "filtrar_por_valor", se recibe un diccionario y un valor int y se retorna otro diccionario con la siguiente condicion: que los valores del nuevo diccionario sean pares y cuyo valor sea mayor al parametro int de la funcion.

**Resultado obtenido**:
cumple con los test, utiliza llamadas que no conozco

**¿Lo usaste tal cual o lo modificaste?**
No lo modifique

---

### 5 - loops.py

**Herramienta**: 
chat de VSC en auto
**Prompt usado**:
> el archivo loops.py contiene 5 funciones sin implementar, que se deben hacer de la siguiente manera: para la funcion "contar_hasta", se recibe como parametro un valor int y se retorna una lista con todos los numeros del 1 hasta el valor, incluyendolo; para la funcion "tabla_multiplicar" se recibe un parametro numerico int y la funcion debe retornar una lista con los 10 primeros multiplos del parametro; para la funcion "suma_digitos" se ingresa como parametro un numero y se requiere que la funcion retorne la suma de los digitos involucrados, si el numero del parametro no es entero positivo, se debe retornar un cero; para la funcion "es_primo" se evalua un numero int del parametro y se necesita retornar verdadero o true si el numero es primo; para la funcion "fibonacci" se recibe un parametro numerico y se desea retornar los valores de fibonacci hasta el parametro ingresado, se deben retornar como una lista.

**Resultado obtenido**:
los resultados pasan las pruebas

**¿Lo usaste tal cual o lo modificaste?**
lo use tal cual

---

### 6 - funciones.py

**Herramienta**: 
Chat de VSC en auto
**Prompt usado**:
> El archivo funciones.py contiene 4 funciones sin implementar y se requiere establecer la funcionalidad de la siguiente manera: para la funcion "aplicar_funcion" se requiere aplicar a cada elemento de una lista determinada, una funcion y retornar la lista modificada, la funcion recibe como parametro una lista y la funcion que se debe aplicar;  para la funcion "componer" se recibe como parametro 2 funciones distintas y se desea retornar otra que contenga la composicion de ambas, de manera que se aplique primero "f" y luego "g"; para la funcion "memorizar" se desea cachear los resultados de una funcion, de tal forma que si se la invoca con los mismos argumentos, se retorne el resultado cacheado; para la funcion "reducir" se reciben como parametros a una lista, una funcion y una inicial y se desea aplicar la funcion a la lista de forma acumulativa, comenzando por la inicial, se requiere no utilizar functools.reduce.

**Resultado obtenido**:
los resultados pasan los tests

**¿Lo usaste tal cual o lo modificaste?**
no lo modifique

---

### 7 - operaciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
Que deben ser muy explicitos y detallados
- ¿En qué casos la IA fue útil y en cuáles no?
En la mayoria de los casos, la ia fue util, mas cuando no sabes la sintaxis de un lenguaje
- ¿Qué harías diferente la próxima vez?
hacer prompts mas cortos y mas consisos.