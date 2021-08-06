# MCOC2021-P0

# Mi computador principal

* Marca/modelo: Apple MacBook Air
* Tipo: Notebook
* Año adquisición: 2018
* Procesador:
  * Marca/Modelo: Intel Core i5 de Doble Núcleo
  * Velocidad Base: 1.80 GHz
  * Velocidad Máxima: 2.90 GHz
  * Numero de núcleos: 2 
  * Humero de hilos: 1
  * Arquitectura: x86_64
  * Set de instrucciones: Intel® SSE, Intel® SSE2, Intel® SSE3 e Intel® SSE4
* Tamaño de las cachés del procesador
  * L1: 256KB
  * L2: 256KB
  * L3: 3MB
* Memoria 
  * Total: 8 GB
  * Tipo memoria: DDR3
  * Velocidad 1600 MHz
  * Numero de (SO)DIMM: 2
* Tarjeta Gráfica
  * Marca / Modelo: Intel HD Graphics 6000
  * Memoria dedicada: 1536 MB
  * Resolución: 1440 x 900
* Disco 1: 
  * Marca: APPLE SSD SM0128G 
  * Tipo: SSD
  * Tamaño: 121 GB (128 GB)
  * Particiones: 2 (EFI + System)
  * Sistema de archivos: FAT32

  
* Dirección MAC de la tarjeta wifi: d0:81:7a:c9:a0:fe 
* Dirección IP (Interna, del router): 192.168.100.1
* Dirección IP (Externa, del ISP): 181.43.154.109
* Proveedor internet: Entel Chile S.A.




P0E2: Desempeño MATMUL

A continuación, se presenta el rendimiento de mi PC al calcular multiplicaciones de matrices de diferentes tamaños, realizando diez corridas. Se grafica el tiempo transcurrido en segundos que demora en realizar cada operación versus el tamaño de la matriz en el primer subplot. En el segundo, se grafica el uso de memoria versus el tamaño de la matriz, además de la memoria RAM del PC. 

![Desempeño MATMUL](https://github.com/GeoChammas/MCOC2021-P0/blob/main/Rendimiento%20A%40B.png)


1. ¿Cómo difiere del gráfico del profesor/ayudante?  

Viendo el gráfico "tamaño de matriz vs tiempo transcurrido", se nota cómo mi computador se demoró más que el del profesor en realizar las corridas, especialmente los últimos puntos correspondientes a matrices cuadradas de dimensión 10000, donde se alcanzaron tiempos alrededores de 1 minuto, mientras que el profesor se demoró 30 segundos máximo aproximadamente.



2. ¿A qué se pueden deber las diferencias en cada corrida?  





3. El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?  





4. ¿Qué versión de python está usando?  

Estoy usando Python 3.8



5. ¿Qué versión de numpy está usando?  

Estoy usando Numpy 1.19.2



6. Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar.   


