# Tarea_Mineria_de_Datos_Segundo_Parcial

# Respuestas de regresión lineal simple

## 1. Pregunta conceptual

### ¿Qué es una regresión?

Una regresión es un método para **estimar o predecir un valor de salida** usando datos pasados. En las diapositivas, la idea es usar una variable de entrada, por ejemplo el **peso**, para estimar una variable de salida, por ejemplo la **altura**.

### ¿Qué es una función de costo?

La función de costo mide **qué tan grande es el error** entre lo que predice el modelo y el valor real. En regresión lineal simple se usa el **error cuadrático medio**, cuya forma en las diapositivas es:

$$
J(\theta_0,\theta_1)=\frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x_i)-y_i)^2
$$

Mientras más pequeño sea $J(\theta_0,\theta_1)$, mejor ajusta la recta a los datos.

### ¿Qué son los parámetros $\theta_1$ y $\theta_0$?

En la ecuación

$$
h_\theta(x)=\theta_1 x+\theta_0
$$

* $\theta_1$ es la **pendiente** de la recta.
* $\theta_0$ es la **intersección con el eje vertical**, también llamada ordenada al origen.

---

## 2. Pregunta resolutiva 1

### Datos

* $(300,3000)$
* $(800,8000)$
* $(900,9000)$

### Proponga dos ecuaciones y encuentre el costo de las dos regresiones

Voy a proponer estas dos rectas:

#### Ecuación 1

$$
h_1(x)=10x
$$

Predicciones:

* $h_1(300)=3000$
* $h_1(800)=8000$
* $h_1(900)=9000$

Errores:

* $3000-3000=0$
* $8000-8000=0$
* $9000-9000=0$

Costo:

$$
J=\frac{1}{2(3)}(0^2+0^2+0^2)=0
$$

#### Ecuación 2

$$
h_2(x)=9x+500
$$

Predicciones:

* $h_2(300)=3200$
* $h_2(800)=7700$
* $h_2(900)=8600$

Errores:

* $3200-3000=200$
* $7700-8000=-300$
* $8600-9000=-400$

Errores al cuadrado:

* $200^2=40000$
* $(-300)^2=90000$
* $(-400)^2=160000$

Suma:

$$
40000+90000+160000=290000
$$

Costo:

$$
J=\frac{290000}{2(3)}=\frac{290000}{6}=48333.33
$$

### Mejor recta posible para ese conjunto de datos

La mejor recta es:

$$
\boxed{h(x)=10x}
$$

porque pasa exactamente por los tres puntos y su costo es:

$$
\boxed{J=0}
$$

---

## 3. Pregunta resolutiva 2

### Datos

* $(300,170)$
* $(800,180)$
* $(900,175)$

Recta dada:

$$
h(x)=3x+5
$$

### Grafique los puntos en el espacio y la recta

Los puntos a colocar son:

* $(300,170)$
* $(800,180)$
* $(900,175)$

Y para la recta $h(x)=3x+5$, algunos puntos de apoyo son:

* $(300,905)$
* $(800,2405)$
* $(900,2705)$

Con eso puedes trazar la línea sobre el plano.

### Encontrar el valor de la función de costo

Predicciones:

* $h(300)=3(300)+5=905$
* $h(800)=3(800)+5=2405$
* $h(900)=3(900)+5=2705$

Errores:

* $905-170=735$
* $2405-180=2225$
* $2705-175=2530$

Errores al cuadrado:

* $735^2=540225$
* $2225^2=4950625$
* $2530^2=6400900$

Suma:

$$
540225+4950625+6400900=11891750
$$

Costo:

$$
J(\theta_0,\theta_1)=\frac{1}{2(3)}(11891750)=\frac{11891750}{6}=1981958.33
$$

### Resultado

$$
\boxed{J(5,3)=1981958.33}
$$

### Grafique cinco valores de la función de costo variando solamente $\theta_0$

Aquí fijo $\theta_1=3$ y cambio solo $\theta_0$:

| $\theta_0$ | Recta          |  Costo $J$ |
| ---------- | -------------- | ---------: |
| -2500      | $h(x)=3x-2500$ |  535320.83 |
| -2200      | $h(x)=3x-2200$ |  377820.83 |
| -1825      | $h(x)=3x-1825$ |  307508.33 |
| -1500      | $h(x)=3x-1500$ |  360320.83 |
| 5          | $h(x)=3x+5$    | 1981958.33 |

Con esos cinco valores puedes hacer la gráfica de $J$ contra $\theta_0$. Se observa que el costo baja mucho cerca de $\theta_0=-1825$.

---

## 4. Pregunta resolutiva 3

### Enunciado

Con las ecuaciones siguientes, realice 5 iteraciones para minimizar la función de costo a partir de la actualización de los pesos. Considere que los pesos al principio se eligen de manera aleatoria.

### Aclaración

Como esa diapositiva no trae un conjunto de datos específico ni el valor de $\alpha$, voy a usar los datos del ejemplo de la presentación:

* $(74,170)$
* $(80,180)$
* $(75,175)$

Tomaré una inicialización aleatoria:

* $\theta_0=60$
* $\theta_1=1$

Y una tasa de aprendizaje:

$$
\alpha=0.0001
$$

### Modelo

$$
h_\theta(x)=\theta_1 x+\theta_0
$$

### Función de costo

$$
J(\theta_0,\theta_1)=\frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x_i)-y_i)^2
$$

### Gradientes

$$
\frac{\partial J}{\partial \theta_0}=\frac{1}{m}\sum_{i=1}^{m}(h_\theta(x_i)-y_i)
$$

$$
\frac{\partial J}{\partial \theta_1}=\frac{1}{m}\sum_{i=1}^{m}(h_\theta(x_i)-y_i)x_i
$$

### Regla de actualización

$$
\theta_j=\theta_j-\alpha \frac{\partial J}{\partial \theta_j}
$$

### Iteración 1

Modelo inicial:

$$
h(x)=1x+60
$$

Predicciones:

* $h(74)=134$
* $h(80)=140$
* $h(75)=135$

Errores:

* $134-170=-36$
* $140-180=-40$
* $135-175=-40$

Costo:

$$
J=749.33
$$

Gradientes:

$$
\frac{\partial J}{\partial \theta_0}=\frac{-36-40-40}{3}=-38.6667
$$

$$
\frac{\partial J}{\partial \theta_1}=\frac{(-36)(74)+(-40)(80)+(-40)(75)}{3}=-2954.6667
$$

Actualización:

$$
\theta_0=60-0.0001(-38.6667)=60.0038667
$$

$$
\theta_1=1-0.0001(-2954.6667)=1.2954667
$$

### Iteración 2

Parámetros actuales:

* $\theta_0=60.0038667$
* $\theta_1=1.2954667$

Costo:

$$
J=130.9067
$$

Actualización:

$$
\theta_0=60.0054776
$$

$$
\theta_1=1.4185384
$$

### Iteración 3

Parámetros actuales:

* $\theta_0=60.0054776$
* $\theta_1=1.4185384$

Costo:

$$
J=23.6096
$$

Actualización:

$$
\theta_0=60.0061488
$$

$$
\theta_1=1.4698019
$$

### Iteración 4

Parámetros actuales:

* $\theta_0=60.0061488$
* $\theta_1=1.4698019$

Costo:

$$
J=4.9935
$$

Actualización:

$$
\theta_0=60.0064287
$$

$$
\theta_1=1.4911549
$$

### Iteración 5

Parámetros actuales:

* $\theta_0=60.0064287$
* $\theta_1=1.4911549$

Costo:

$$
J=1.7636
$$

Actualización final:

$$
\theta_0=60.0065456
$$

$$
\theta_1=1.5000491
$$

### Tabla resumen de las 5 iteraciones

| Iteración | $\theta_0$ | $\theta_1$ | Costo $J$ |
| --------- | ---------: | ---------: | --------: |
| 1         |  60.000000 |   1.000000 |  749.3333 |
| 2         |  60.003867 |   1.295467 |  130.9067 |
| 3         |  60.005478 |   1.418538 |   23.6096 |
| 4         |  60.006149 |   1.469802 |    4.9935 |
| 5         |  60.006429 |   1.491155 |    1.7636 |

### Conclusión

Después de 5 iteraciones, la función de costo **disminuye de 749.3333 a 1.7636**, así que el modelo sí se está ajustando mejor a los datos. La recta obtenida al final queda aproximadamente como:

$$
\boxed{h(x)=1.5000x+60.0065}
$$
