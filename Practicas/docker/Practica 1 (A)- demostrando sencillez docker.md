
# Práctica 1: Ejemplo Rápido de Despliegue de una Aplicación en Docker

**Objetivo**: Esta práctica rápida demuestra la facilidad de usar Docker para descargar, iniciar y visualizar una aplicación web en pocos pasos.

---

## Paso 1: Descargar una Imagen de Docker

Para este ejemplo, vamos a utilizar una imagen de Nginx que despliega un servidor web básico.

```bash
docker pull nginx
```

## Paso 2: Ejecutar un Contenedor con Nginx

Iniciemos un contenedor con Nginx para desplegar el servidor web.

```bash
docker run -d -p 10001:80 --name mi_nginx nginx
```

- **Explicación de los parámetros**:
  - `-d`: Ejecuta el contenedor en segundo plano.
  - `-p 10001:80`: Mapea el puerto 80 del contenedor al puerto 8080 de la máquina local.
  - `--name mi_nginx`: Asigna un nombre específico al contenedor.

## Paso 3: Verificar el Despliegue

Para visualizar la aplicación, abre un navegador e ingresa la siguiente URL:

```
http://tidpnube-b.rediris.es:10001
```

Deberías ver la página de bienvenida de Nginx, lo que confirma que el servidor está funcionando correctamente.

---

## Paso 4: Detener y Eliminar el Contenedor

Cuando hayas terminado de probar la aplicación, puedes detener y eliminar el contenedor de la siguiente forma:

```bash
docker stop mi_nginx
docker rm mi_nginx
```

---

¡Con esta práctica rápida, has desplegado y visualizado una aplicación usando Docker en unos pocos comandos!
