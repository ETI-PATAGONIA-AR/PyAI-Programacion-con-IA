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

- Crear una cuenta en Groq ( Ingresa a https://groq.com/ )

- Haz clic en Sign Up / Registrarse y completa tus datos.

- Generar tu API Key; Para ello inicia sesión en tu cuenta Groq / --Ve a Dashboard → API Keys.

- Haz clic en Create API Key / Generar clave.

- Copia la clave generada.

- Guardar la API Key localmente

- Dentro del proyecto, ve a la carpeta config/.

- Crea un archivo llamado api_key.txt si no existe y pega tu API Key dentro y guarda el archivo.

- El archivo debería contener solo tu API Key y nada más.

- Para probar la configuración, ejecuta el proyecto (run_PyAI_v1.bat)... Si todo está correcto, la conexión con Groq funcionará automáticamente.

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

## NOTA (12/02/2026) "Aclaración importante sobre cambios en modelos y servicios externos"***

Ante el cambios de los ecosistema de modelos gratuitos sin previo aviso por parte de los proveedores:

- relajaron filtros

- priorizan chat

- rompen RAG

- empujan pago

Durante el desarrollo de este proyecto, varias de las plataformas y modelos de Inteligencia Artificial que ofrecían acceso gratuito o semi-gratuito cambiaron sus reglas de uso, disponibilidad o políticas de acceso. Esto impactó directamente en muchos proyectos que, como PyAI, funcionaban correctamente en su momento y luego dejaron de hacerlo sin que hubiera cambios en el código.

***En particular, se vieron afectados los siguientes casos.***

En el ecosistema Groq, varios modelos abiertos que antes podían utilizarse de manera simple dejaron de estar disponibles o cambiaron sus condiciones. Los modelos LLaMA 2 en sus variantes de 7B y 13B fueron discontinuados por Meta y, en consecuencia, Groq dejó de ofrecerlos. Proyectos que dependían de estos modelos ya no pueden utilizarlos.

El modelo Mixtral 8x7B Instruct sigue existiendo en Groq, pero ya no funciona como antes. Actualmente requiere una API Key obligatoria, tiene límites de uso más estrictos y ya no puede considerarse un recurso libre o plug and play. Cualquier proyecto que antes funcionara sin clave o con configuraciones mínimas puede fallar debido a estos cambios.

En el caso de los modelos Gemma de Google, el acceso también se volvió más restrictivo. No siempre están disponibles y su comportamiento no es ideal para ciertos usos técnicos, especialmente cuando se requiere precisión estricta o recuperación de información basada en contexto, ya que tienden a generar respuestas más interpretativas.

En paralelo, la API de inferencia gratuita de HuggingFace sufrió una degradación importante. El nivel gratuito clásico se volvió extremadamente limitado o directamente inutilizable en muchos escenarios reales. Es común experimentar tiempos de espera muy largos, modelos que permanecen inactivos, respuestas vacías o directamente fallos de ejecución. Modelos que antes rendían aceptablemente en ese entorno, como Mistral 7B Instruct o LLaMA 2, dejaron de ser una opción viable en el free tier.

La conclusión general es que ya no existe un acceso verdaderamente gratuito, estable y plug and play a modelos grandes a través de estas plataformas, como ocurría meses atrás. PyAI no dejó de funcionar por errores propios, sino que se vio afectado por cambios externos en los servicios de inferencia.

Por este motivo, el proyecto evolucionó y se dividió en distintas variantes. Esta versión On-Line utiliza Groq con API Key obligatoria y modelos actualmente soportados. Otras versiones del proyecto apuntan a resolver estas limitaciones mediante ejecución local y funcionamiento completamente offline.

Si al clonar el repositorio experimentás errores relacionados con modelos, disponibilidad o acceso, revisá que estés utilizando un modelo actualmente soportado y que hayas configurado correctamente tu propia API Key.

## Modelos que probamos y ya no funcionan como antes / se cayeron

❌ ***Groq – llama2-70b-4096*** ✔️ Funcionaba al inicio - ❌ Dejó de estar disponible - Motivo: LLaMA 2 fue discontinuado ... Estado actual: NO EXISTE en Groq

❌ ***Groq – llama2-7b / llama2-13b*** ✔️ Usados en pruebas iniciales - ❌ Retirados  

⚠️ ***Groq – gemma-7b-it*** ✔️ Probado - ❌ Muy verborrágico - ❌ Pésimo siguiendo modo scripting - ❌ Alucina incluso con contexto cargado ... Estado: DESCARTADO

❌ ***HuggingFace – mistral-7b-instruct (Inference API free)*** ✔️ Probado - ❌ Timeouts - ❌ Se “duerme” - ❌ Respuestas incompletas ... Estado: INUTILIZABLE en free

❌ ***HuggingFace – llama-2- (Inference API)*** ✔️ Probado - ❌ Retirado / bloqueado ... Estado: MUERTO

---

## Posibles soluciones:

Bien, veamos un pequeño paso a paso, de como editar nuestro programa y probar otros modelos de Groq sin romper PyAI...

***PASO 1***

Entender qué parte del archivo define el modelo; O sea, en  groq_client.py NO hay ningún modelo hardcodeado. 
El modelo se toma desde este punto:

```python
payload = {
    "model": self.settings["model"],
    "temperature": self.settings["temperature"],
    "max_tokens": self.settings["max_tokens"],
    "messages": messages
}
```

Eso significa que el modelo NO se cambia acá, sino en:

```arduino
config/settings.json
```

***PASO 2 - Ubicar el archivo correcto a editar***

Abrí este archivo del proyecto:

```arduino
config/settings.json
```

Un ejemplo típico puede verse así:

```python
{
    "model": "mixtral-8x7b-32768",
    "temperature": 0.7,
    "max_tokens": 1024
}
```

***PASO 3 - Cambiar el modelo (ejemplos reales)***

Para probar otro modelo de Groq, solo cambiás el valor de "model". Ejemplos válidos (dependen de disponibilidad en tu cuenta Groq):

- Mixtral 8x7B Instruct: "model": "mixtral-8x7b-32768"

- LLaMA 3 8B Instruct: "model": "llama3-8b-8192"

- LLaMA 3 70B Instruct (si tu cuenta lo permite): "model": "llama3-70b-8192"

- Gemma 7B: "model": "gemma-7b-it"

y el resto queda exactamente igual; No hace falta tocar nada más.

***PASO 4 - Ajustar tokens según el modelo (opcional pero recomendado)***

Modelos más grandes toleran más contexto, pero también consumen más. Ejemplo conservador y estable:

```python
{
    "model": "llama3-8b-8192",
    "temperature": 0.6,
    "max_tokens": 800
}
```

Si ponés max_tokens demasiado alto y el modelo no lo soporta → error de API.

***PASO 5 - Guardar y ejecutar PyAI normalmente***

No hay que reiniciar nada raro; Simplemente:

```arduino
python main.py
```

PyAI va a usar el nuevo modelo automáticamente.

***PASO 6 - Cómo saber si el modelo no está disponible***

Si el modelo no existe o no está habilitado, vas a ver errores como:

```arduino
HTTP 400 / 404

"model not found"

"model not available for this account"
```

En ese caso, Volvé a 

```arduino
settings.json
```

y probá otro modelo

***PASO 7 - Qué NO hacer (errores comunes)***

- NO pongas el modelo hardcodeado en groq_client.py
- NO edites la URL
- NO cambies headers
- NO dupliques lógica

---

Lamento en lo mas profundo lo que esta sucediendo, es por ello que voy agilizar las cosas para compartir el modelo OffLINE y no depender de estas cosas insolitas que hacen los proveedores.

Los saludo atte

---

### Desarrollador por
prof.martintorres@educ.ar
