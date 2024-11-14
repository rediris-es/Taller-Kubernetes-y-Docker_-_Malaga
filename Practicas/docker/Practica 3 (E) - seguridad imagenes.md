
# Práctica: Exploración y Verificación de Imágenes con Docker

En esta práctica, aprenderemos cómo extraer y verificar imágenes en Docker, observar su estructura en capas, y cómo utilizar el manifiesto de Docker para verificar la autenticidad y la integridad de una imagen descargada.

## Objetivos de la Práctica
- Comprender la estructura en capas de una imagen Docker.
- Usar el manifiesto de Docker para verificar la autenticidad y detalles de una imagen.
- Familiarizarse con los comandos de Docker relacionados con imágenes y capas.

## Requisitos Previos
- Tener Docker instalado y configurado en tu máquina.
- Acceso a internet para descargar imágenes de Docker Hub.

---

### Paso 1: Descargar una Imagen de Docker Hub

1. Abre la terminal y ejecuta el siguiente comando para descargar una imagen oficial de Docker Hub:

   ```bash
   docker pull nginx
   ```

2. Una vez descargada, verifica que la imagen está en tu sistema:

   ```bash
   docker images
   ```

---

### Paso 2: Verificar la Estructura en Capas de la Imagen

1. Utiliza el siguiente comando para ver las capas de la imagen:

   ```bash
   docker history nginx
   ```

2. Observa cada capa. Aquí podrás ver el tamaño y las instrucciones utilizadas en cada capa durante la creación de la imagen.

> **Nota**: Cada capa representa una acción del Dockerfile usado para construir la imagen.

---

### Paso 3: Verificar la Autenticidad de la Imagen usando el Digest

1. Cuando descargamos una imagen de Docker Hub, el digest (identificador criptográfico) de la imagen aparece en el terminal. Para verificar este digest en tu sistema, ejecuta:

   ```bash
   docker images --digests
   ```

2. Verifica que el digest que aparece en esta lista coincide con el digest mostrado durante el proceso de `pull`. Esto asegura que la imagen descargada no ha sido alterada y es la versión oficial.

---

## Práctica Avanzada: Uso del Manifiesto de Docker para Examinar una Imagen

### Paso 4: Inspeccionar el Manifiesto de la Imagen

1. Usa el siguiente comando para ver el manifiesto de la imagen `nginx`:

   ```bash
   docker manifest inspect nginx
   ```

2. Observa la información mostrada en el manifiesto:
   - **Layers**: Lista de capas con sus respectivos identificadores, que conforman la imagen.
   - **Platform**: Información sobre la arquitectura y el sistema operativo para los que está diseñada la imagen.
   - **MediaType**: Tipo de contenido que describe el manifiesto.

> **Pregunta para reflexionar**: ¿Qué ventajas tiene que Docker permita definir la plataforma y las capas de una imagen a través de un manifiesto?


---

### Paso 5: Bonus - Explora el Controlador de Almacenamiento de Docker

1. Para ver cómo se gestionan las capas y el almacenamiento en tu sistema, utiliza:
   ```
   docker info
   ```

2. En el campo **Storage Driver**, observa el controlador de almacenamiento que Docker utiliza en tu máquina.

> **Nota**: Este controlador gestiona cómo y dónde se almacenan las imágenes y sus capas. En sistemas Linux, puedes encontrarlas en `/var/lib/docker`.

---

## Resumen y Conclusiones

Esta práctica te ha permitido comprender cómo Docker organiza las imágenes en capas, cómo se verifican usando el digest, y cómo explorar el manifiesto de una imagen para verificar detalles específicos. Esto asegura que tienes un mejor control sobre la autenticidad y estructura de las imágenes que utilizas, una habilidad esencial para trabajar de forma segura en entornos de Docker.
