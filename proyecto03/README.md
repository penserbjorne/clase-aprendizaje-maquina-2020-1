# Práctica 03

__Redes Neuronales Multicapa utilizando el algoritmo backpropagation__

- Aguilar Enriquez, Paul Sebastian
- Cabrera Lopez, Oscar Emilio

## Objetivo

El alumno programara su propia implementación del algoritmo backpropagation con la finalidad de aproximar funciones utilizando redes neuronales multicapa, el alumno conocerá los efectos de añadir neuronas en las capas ocultas, así como también los efectos del learning rate.

## Introducción

### Redes Neuronales de Alimentación Profunda

Las _Deep feedforward networks_, _feedforward neural networks_ (redes neuronales de alimentación profunda) o _multilayer perceptrons_ (perceptrones multicapa) son los modelos de aprendizaje profundo por excelencia.

El objetivo de estas redes es aproximar alguna función _f*_. Por ejemplo, para un clasificador, _y = f*(x)_ mapea una entrada _x_ a una categoria _y_. Una red neuronal de alimentación profunda define un mapeo _y = f(x;θ)_ y aprende el valor del parametro _θ_ que resulta en la mejor aproximación de la función.

Para lo anterior la red se compone de distintas capas que a su vez se conforman de perceptrones, los cuales ajustan sus pesos y sesgos para realizar clasificaciones intermedias hasta llegar a la clasificación final, esto es lo que se conoce como aprendizaje, y es la forma de aproximar la clasificación a la función de mapeo.

Estas redes se componen de una capa de entrada, capas intermedias y una capa de salida, van ejecutándose en ese sentido.

### Aprendizaje basado en el Gradiente

Diseñar y entrenar una red neuronal no es demasiado distinto a entrenar cualquier otro modelo de aprendizaje máquina con el gradiente descendente.

La diferencia entre los modelos lineales y las redes neuronales es que la no linealidad de las redes provoca que las funciones de perdidas más interesantes se vuelvan no convexas.



## Desarrollo

El desarrollo de esta práctica se hizo en un notebook de Jupyter con el lenguaje de programación Julia y utilizando el paquete de AIJulia.

## Resultados

Pesos, bias finales, graficas

## Conclusiones

- __Aguilar Enriquez Paul Sebastian:__
- __Cabrera Lopez Oscar Emilio:__ -

## Bibliografia

- Goodfellow I. , Bengio Y. & Courville A.. (2016). CHAPTER 6. DEEP FEEDFORWARD NETWORKS. En Deep Learning(164 - 223). Massachusetts, Estados Unidos: MIT Press.
