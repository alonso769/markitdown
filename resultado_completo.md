<!-- Slide number: 1 -->

![/home/claude/ppt/imgs/img-002.jpg](Image0.jpg)

TALLER DE ROBÓTICA  ·  UNIVERSIDAD PRIVADA DEL NORTE
Sistema Autónomo de Drones para Vigilancia y Monitoreo
Diseño, implementación y consideraciones éticas de un prototipo de bajo costo

Alonso Sixto Silva Vidal   ·   Jonatan Hilario Grandez

Lisbeth Verónica Bertran Gutiérrez   ·   Erik Quispe Yovera
Docente: Carlos Ramos Gonzales   ·   4 de julio de 2026

<!-- Slide number: 2 -->
CONTENIDO
Agenda de la exposición

01
02
Introducción
Antecedentes
Contexto y objetivos del proyecto
Investigaciones que sustentan el diseño

03
04
Arquitectura
Hardware y ensamblaje
Propuesta inicial vs. implementación real
Componentes y proceso de construcción

05
06
Ética y resultados
Conclusiones
Principios de diseño responsable y hallazgos
Recomendaciones para futuras iteraciones
Taller de Robótica · UPN · NRC 4273
2

<!-- Slide number: 3 -->
01 · INTRODUCCIÓN
Drones: integración multidisciplinaria
Los vehículos aéreos no tripulados (drones) integran electrónica, mecánica, programación y sistemas de control. Su aplicación se ha expandido a múltiples sectores de la industria y la investigación.
Sectores de aplicación
Agricultura

Seguridad

Topografía
Este proyecto

Prototipo de dron cuadricóptero construido por estudiantes de Ingeniería de Sistemas Computacionales (UPN) en el curso Taller de Robótica, sobre una plataforma de bajo costo basada en Arduino Nano.
Logística

Gestión de desastres

Investigación científica

Taller de Robótica · UPN · NRC 4273
3

<!-- Slide number: 4 -->
02 · ANTECEDENTES
Investigaciones que sustentan el proyecto

Defensa

Seguridad ciudadana
Planas Woll (2025)
Universidad César Vallejo (2024)
Los drones mejoran las capacidades de vigilancia, reconocimiento y toma de decisiones estratégicas en defensa nacional.
Reducción de hasta 35% en tiempos de respuesta ante incidentes en zonas urbanas de alta densidad.

Navegación autónoma

Inspección y seguridad laboral
García, M. (2016)
Del Barrio Tajadura (2017) · Díaz (2015)
Sincronismo por hardware entre cámaras que reduce el retardo de captura a escala de nanosegundos.
Los RPAS reducen el riesgo para inspectores y eliminan la exposición directa del trabajador al peligro.
Taller de Robótica · UPN · NRC 4273
4

<!-- Slide number: 5 -->
03 · ARQUITECTURA
De la propuesta conceptual al prototipo real
| Capa | Propuesta inicial (SIVAD-IA) | Implementación real |
| --- | --- | --- |
| Procesamiento | Raspberry Pi 4 + ROS 2 | Arduino Nano (ATmega328P) |
| Posicionamiento | GPS NEO-M8N | IMU MPU-6050 |
| Comunicación | Radio MAVLink 915 MHz | Bluetooth HC-05 / ZS-040 |
| Alimentación | No especificada | Regulador buck LM2596 |
| Obstáculos | Sensor HC-SR04 | Pendiente de integración |
Motivo del cambio: reducir peso, costo y consumo, priorizando estabilización de vuelo en espacios reducidos y facilidad de integración con componentes disponibles en el mercado peruano.
Taller de Robótica · UPN · NRC 4273
5

<!-- Slide number: 6 -->
04 · HARDWARE
Componentes del prototipo físico

![/home/claude/ppt/imgs/img-008.jpg](Image0.jpg)

![/home/claude/ppt/imgs/img-014.jpg](Image1.jpg)

![/home/claude/ppt/imgs/img-012.jpg](Image2.jpg)

![/home/claude/ppt/imgs/img-018.jpg](Image3.jpg)
Arduino Nano
IMU MPU-6050
Bluetooth HC-05
Regulador LM2596
Unidad central (ATmega328P). Lee sensores y controla motores por PWM.
Acelerómetro + giroscopio de 3 ejes. Estabilización de vuelo vía I2C.
Comunicación inalámbrica. Alcance de hasta 10 m en campo abierto.
Convertidor buck. Estabiliza la batería LiPo a 5V / 3.3V.
Taller de Robótica · UPN · NRC 4273
6

<!-- Slide number: 7 -->
04 · ENSAMBLAJE
Proceso de construcción del prototipo
Apertura del chasis y retiro de la electrónica original

1

![/home/claude/ppt/imgs/img-022.jpg](Image0.jpg)

Fijación del Arduino Nano y del MPU-6050 en la placa base

2
Conexión del regulador de voltaje entre la batería y las líneas de 5V

3
Cableado de los cuatro motores a las salidas PWM del Arduino

4
Conexión del módulo Bluetooth con divisor de tensión en RX

5
Verificación de continuidad y prueba de encendido sin hélices

6
Taller de Robótica · UPN · NRC 4273
7

<!-- Slide number: 8 -->

![/home/claude/ppt/imgs/img-002.jpg](Image0.jpg)
PROTOTIPO FÍSICO
Prototipo ensamblado y encendido
4
motores brushed
10 m
alcance Bluetooth
18×45 mm
tamaño del Arduino Nano
Taller de Robótica · UPN · NRC 4273
8

<!-- Slide number: 9 -->
05 · ÉTICA
Principios de diseño responsable

1

2

3

4
Zonas restringidas
Consentimiento
Protección de datos
Uso limitado
No operar sobre propiedades privadas ni zonas restringidas sin autorización, aún en fase de prototipo académico.
Toda imagen o video capturado debe contar con el consentimiento de las personas presentes en el área de vuelo.
Los datos de telemetría transmitidos por Bluetooth deben protegerse frente a accesos no autorizados.
El prototipo no incorpora ni incorporará capacidad de armamento ni interferencia de comunicaciones de terceros.
Taller de Robótica · UPN · NRC 4273
9

<!-- Slide number: 10 -->
06 · RESULTADOS
Validación del prototipo

Encendido y estabilización
Lectura del sensor inercial
Comunicación Bluetooth
Funcionamiento correcto del Arduino Nano como unidad de control.
Datos estables del MPU-6050 para el control de actitud.
Envío de comandos y telemetría efectivo dentro del alcance esperado.

Los resultados validan la viabilidad de una arquitectura de bajo costo como alternativa funcional a la propuesta conceptual inicial, especialmente para fines educativos y de prototipado rápido.
Taller de Robótica · UPN · NRC 4273
10

<!-- Slide number: 11 -->
07 · TRABAJO FUTURO
Recomendaciones para próximas iteraciones

Incorporar un sensor ultrasónico HC-SR04 para detección básica de obstáculos.

1

Migrar a un módulo Bluetooth de baja energía (BLE, como el HM-10).

2

Documentar el firmware del Arduino con una convención de comentarios clara.

3

Establecer un plan de mantenimiento preventivo de hélices, motores y conectores.

4
Taller de Robótica · UPN · NRC 4273
11

<!-- Slide number: 12 -->
08 · CONCLUSIONES
Principales aportes del proyecto
Es posible construir un prototipo funcional de dron con componentes de bajo costo y amplia disponibilidad, sin comprometer estabilidad ni comunicación.

La sustitución de la arquitectura conceptual (Raspberry Pi + GPS + radio) por Arduino Nano + MPU-6050 + Bluetooth respondió a criterios de costo, peso e integración.

El diseño incorpora principios de ingeniería responsable: privacidad, consentimiento y límites explícitos de uso.

Los resultados sientan una base sólida para incorporar detección de obstáculos y navegación más robusta en futuras iteraciones.

Taller de Robótica · UPN · NRC 4273
12

<!-- Slide number: 13 -->
Gracias
Preguntas y comentarios

Alonso Sixto Silva Vidal · Jonatan Hilario Grandez
Lisbeth Verónica Bertran Gutiérrez · Erik Quispe Yovera
Taller de Robótica · NRC 4273 · Universidad Privada del Norte