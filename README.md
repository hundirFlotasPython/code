# Hundir la Flota<br>
*Autores:*<br>
*Ana Genua*<br>
*Federico Ruiz*<br>
<br>
Este proyecto se ha desarrollado usando Python 3.7 y en el mismo se han empleado los siguientes módulos de la Standard Library de Python:
- os
- re
- pandas
- numpy
- random
- sys
- json
- copy
<br>

## Arquitectura de la aplicación.<br>
Hemos intentado crear una arquitectura orientada a objetos, aunque no ha sido necesario usar conceptos como la herencia, resultando el siguiente esquema:<br>
<br>
![Esquema de clases](./imgs/hf_20211219182502_esquema_clases.png)<br><br>

Propósito de cada clase:

- Partida: 
  - Almacenar los objetos jugador. 
  - Generar aleatoriamente los datos sobre las barcos.
  - Proporcionar los datos sobre los barcos para generar la flota de cada jugador.
  - Generar estadísticas sobre la partida.

- Jugagor:
  - Almacenar los datos sobre la flota.
  - Almacenar los datos sobre los disparos realizados.
  - Proporcionar métodos para realizar disparos.

- Barco:
  - Almacena la información de los daños y el estado de cada barco.
  - Proporciona un método para comprobar los daños provocados y el estado del barco.
<br>
No se ha implementado una clase Flota para almacenar los barcos; simplemente se han almacenado los objetos barco en una lista.<br>

Se han usado dos clases auxiliares:
- Celdas barco
- Fronteras barco

Respectivamente se usan para, calcular las celdas que ocupará cada barco y las fronteras que tendrá cada barco. De esta forma al generar el tablero de cada jugador, evitamos que los barcos entren en conflicto.<br>

Adicionalmente existe un archivo utils.py donde se han ubicado funciones que serán usadas por los distintos objetos, para operaciones como:
- Almacenar constantes
- Solicitar inputs del usuario
- Imprimir la pantalla de juego
- Generar valores random
- Traducir coordenadas

##  Esquema de archivos<br>
Los archivos en los que se han implementado dichas clases están ubicados en el directorio **src** y se relacionan como muestra el siguiente gráfico:<br>

![Esquema de archivos](./imgs/hf_20211219173335_esquema_archivos.png)<br><br>

![Ejecución del script principal](./imgs/hf_20211219132451.png)<br><br>
![Introducción del nombre del jugador](./imgs/hf_20211219132526.png)<br><br>
![Introducción del nivel de dificultad](./imgs/hf_20211219132633.png)<br><br>
![Control del nivel de dificultad](./imgs/hf_20211219132718.png)<br><br>
![Comienzo de partida](./imgs/hf_20211219132759.png)<br><br>
![Pantalla inicial](./imgs/hf_20211219132854.png)<br><br>
![Control de coordendas](./imgs/hf_20211219134727_control_coordenadas.png)<br><br>
![Salida juego](./imgs/hf_20211219134830_salida_partida.png)<br><br>
![Información primer disparo del jugador](./imgs/hf_20211219132917.png)<br><br>
![Información de la primera jugada del ordenador](./imgs/hf_20211219133002.png)<br><br>
![Mensaje de finalización de partida](./imgs/hf_20211219133058.png)<br><br>
![Resumen de la partida](./imgs/hf_20211219133127.png)<br><br>
