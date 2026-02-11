# PyAI - El asistente técnico de programación que emplea IA -

## Para que sirve esta herramienta?

PyAI es una herramienta de asistencia basada en Inteligencia Artificial desarrollada en Python, pensada desde el inicio como una aplicación de escritorio real y usable, no como un simple chatbot de prueba ni una demo de modelos de lenguaje. El proyecto nace de la necesidad de contar con un asistente que pueda acompañar procesos técnicos, educativos y creativos de manera flexible, manteniendo contexto y adaptándose a la persona que lo utiliza.

Pueden ver el video con los primeros pasos ( https://youtu.be/04bbXQ0UP4U )

[![Míralo en YouTube](https://i.ytimg.com/an_webp/04bbXQ0UP4U/mqdefault_6s.webp?du=3000&sqp=CKDTr8wG&rs=AOn4CLDT5_CojV5bQdD6dyjhIHkPGYlKHw)](https://youtu.be/04bbXQ0UP4U)


La idea central detrás de PyAI es que la inteligencia artificial se adapte al usuario y a su forma de trabajar, aprender o razonar, y no que el usuario tenga que amoldarse a las limitaciones de la IA.



Este repositorio corresponde exclusivamente a la versión On-Line de PyAI, que funciona mediante el consumo de modelos de lenguaje ejecutados en la nube a través de la plataforma Groq; La versión Off-Line, me reservo los derechos a compartirlo solo con los que son seguidores activos y que no solo me acompañan alentándome en cada trabajo, en cada proyecto, sino que también me inspiran con sus mensajes de aliento, e incluso ideas de mejoras funcionales.

La versión On-Line de PyAI está orientada principalmente a la asistencia técnica, el desarrollo de software, el análisis de código y la resolución de problemas complejos. Aprovecha la infraestructura de Groq para obtener inferencias de muy baja latencia y alta calidad, sin necesidad de ejecutar modelos pesados de forma local ni contar con hardware especializado.

PyAI fue diseñado con una arquitectura modular, lo que permite que distintas versiones del proyecto compartan una misma base conceptual y estructural, pero se adapten a distintos entornos y públicos. Actualmente, el ecosistema PyAI contempla tres líneas / versiones principales de desarrollo.



https://github.com/user-attachments/assets/d937c7b1-c7b4-431d-8ca4-1f618e9e21ec



---

## Las distintas Versiones de una misma base:

- La primera es esta versión On-Line (PyAI_v1), enfocada en usuarios técnicos y desarrolladores, que prioriza potencia, velocidad de respuesta y precisión. Es ideal para programación, scripting, análisis técnico y asistencia contextual en proyectos reales de programación en Python, como asi también, en C++/Arduino y estoy en fase beta probando otros lenguajes mas.

- La segunda es una versión Off-Line (PyAI_v2), desarrollada para funcionar completamente sin conexión a internet. Esta variante utiliza modelos descargables que se ejecutan de manera local y está pensada para entornos donde no hay conectividad, o donde se requiere control total sobre los datos y el modelo. Esta versión se publicará como un proyecto independiente, y como mencione anteriormente, estará semi-restringida.

- La tercera es una versión educativa (ProfeAI), orientada a niños y adolescentes de nivel primario y secundario. En esta variante se incorporaron TTS (herramientas de Text To Speech - Generación de de Texto a Voz) y un fuerte trabajo pedagógico, con el objetivo de que la IA pueda actuar como un profesor particular de matemáticas. En esta versión, la inteligencia artificial se adapta al alumno, a su nivel y a su ritmo de aprendizaje, explicando los conceptos de distintas maneras hasta lograr comprensión, evitando un enfoque rígido o académico tradicional.

---

## PyAI_v1:

En la versión On-Line, PyAI utiliza modelos de lenguaje de gran escala provistos por Groq. El modelo principal empleado es LLaMA 3 de 70 mil millones de parámetros, en variantes como llama3-70b-8192 según disponibilidad. Groq permite trabajar con modelos de alto nivel de razonamiento, excelente desempeño en tareas técnicas y una latencia muy baja, lo que mejora notablemente la experiencia de uso.
Para utilizar PyAI en modo On-Line es obligatorio contar con una API Key personal de Groq. El archivo api_key.txt incluido en el proyecto no contiene ninguna clave válida por defecto. Cada usuario debe generar su propia clave desde su cuenta de Groq y colocarla manualmente en ese archivo. Es importante no subir nunca la API Key a un repositorio público.
PyAI está desarrollado en Python y requiere Python versión 3.10 o superior. Las dependencias necesarias se encuentran definidas dentro del proyecto y están orientadas a mantener una estructura clara, modular y fácil de extender.
Actualmente, la versión On-Line de PyAI permite mantener conversaciones con contexto, asistir en tareas técnicas complejas, trabajar sobre proyectos reales y servir como base para futuras extensiones. Este repositorio representa una parte fundamental del ecosistema PyAI, pero no agota el alcance total del proyecto.

PyAI es un proyecto en evolución constante. Todas sus variantes comparten una misma filosofía: utilizar la inteligencia artificial como una herramienta que acompaña, explica y se adapta, en lugar de imponer un modelo rígido de interacción.

---

** Recuerden que deben generar sus propias api key de Groq y pegarla en un archivo TXT llamado "api_key.txt" y alojarlo dentro de la carpeta "PyAI_onLINE\config" **

## 🔑 Configuración de Groq API Key

Para que PyAI funcione correctamente, necesitas una cuenta en Groq y una API Key. Sigue estos pasos:

-- Crear una cuenta en Groq ( Ingresa a https://groq.com/ )

-- Haz clic en Sign Up / Registrarse y completa tus datos.

-- Generar tu API Key; Para ello inicia sesión en tu cuenta Groq / --Ve a Dashboard → API Keys.

-- Haz clic en Create API Key / Generar clave.

-- Copia la clave generada.

-- Guardar la API Key localmente

-- Dentro del proyecto, ve a la carpeta config/.

-- Crea un archivo llamado api_key.txt si no existe y pega tu API Key dentro y guarda el archivo.

-- El archivo debería contener solo tu API Key y nada más.

-- Para probar la configuración, ejecuta el proyecto (run_PyAI_v1.bat)... Si todo está correcto, la conexión con Groq funcionará automáticamente.

⚠️ Importante: No compartas tu API Key con nadie y no la subas al repositorio público.

---

** Paso los CMD para instalar las dependencias: **

 1️⃣ Actualizar pip a la última versión

python -m pip install --upgrade pip

---

 2️⃣ Instalar dependencias globales del proyecto

pip install PyQt5==5.15.11

pip install requests==2.32.5

pip install Pygments==2.19.2

pip install pyttsx3

---
