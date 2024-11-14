
# Práctica Corta de Kubernetes

## 1. Verificar el Estado de los Nodos

1. **Comando básico para ver los nodos:**

   ```bash
   kubectl get nodes
   ```
   Este comando muestra todos los nodos en el clúster de Kubernetes y el estado de cada uno (por ejemplo, `Ready`, `NotReady`).

2. **Obtener más información sobre los nodos:**

   ```bash
   kubectl get nodes -o wide
   ```
   Aquí verás detalles adicionales como la dirección IP, la versión del sistema operativo, el nombre del host, y más.

---

## 2. Ver los Componentes de `kube-system`

1. **Listar todos los pods en el espacio de nombres `kube-system`:**

   ```bash
   kubectl get pods -n kube-system
   ```
   Este espacio de nombres contiene componentes esenciales de Kubernetes como `kube-apiserver`, `etcd`, `kube-controller-manager`, y `kube-scheduler`. Explicación rápida de cada uno:
   - **kube-apiserver**: La API principal que recibe todas las interacciones del usuario.
   - **etcd**: El almacenamiento de datos distribuidos de Kubernetes, utilizado para guardar la configuración y el estado del clúster.
   - **kube-controller-manager**: Responsable de controlar los controladores del clúster.
   - **kube-scheduler**: Asigna los pods a los nodos disponibles.

---

## 3. Ver el Espacio de Nombres Actual

1. **Comprobar en qué espacio de nombres te encuentras actualmente:**

   ```bash
   kubectl config view --minify | grep namespace
   ```
   Si no aparece un espacio de nombres específico, significa que estás en el espacio de nombres `default`.

2. **Listar todos los espacios de nombres:**

   ```bash
   kubectl get namespaces
   ```
   Esto muestra todos los espacios de nombres, como `default`, `kube-system`, `kube-public`, etc.

---

## 4. Crear y Describir un Pod

1. **Crear un archivo de configuración de Pod rápido (llámalo `simple-pod.yaml`):**

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: my-first-pod
     labels:
       app: my-app
   spec:
     containers:
     - name: my-container
       image: nginx
       ports:
       - containerPort: 80
   ```
2. **Crear el pod con el archivo de configuración:**

   ```bash
   kubectl apply -f simple-pod.yaml
   ```

3. **Verificar que el pod se ha creado:**

   ```bash
   kubectl get pods
   ```

4. **Describir el pod para obtener más detalles:**

   ```bash
   kubectl describe pod my-first-pod
   ```
   Esto te dará información detallada sobre el estado del contenedor, eventos recientes, y más.

---

## 5. Visualización Rápida del Pod

1. **Ver los logs del contenedor dentro del Pod:**

   ```bash
   kubectl logs my-first-pod
   ```
   Esto muestra los registros generados por el contenedor dentro del Pod.

2. **Acceder a una terminal dentro del contenedor:**

   ```bash
   kubectl exec -it my-first-pod -- /bin/bash
   ```
   Esto abre una terminal dentro del contenedor `nginx`. Puedes usar esto para explorar el sistema de archivos del contenedor.

---

## 6. Eliminar Todo lo Creado

1. **Eliminar el Pod que creaste:**

   ```bash
   kubectl delete pod my-first-pod
   ```
   Esto elimina el Pod `my-first-pod` que configuraste.

2. **Eliminar el archivo de configuración `simple-pod.yaml` (si lo deseas):**

   ```bash
   rm simple-pod.yaml
   ```
   Esto elimina el archivo de configuración del Pod que creaste en tu máquina local.

---

¡Esto debería darte un buen primer vistazo a Kubernetes y sus componentes!
