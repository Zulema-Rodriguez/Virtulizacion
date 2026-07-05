# Virtulizacion


* Universidad Tecnológica Nacional (UTN)
* **Materia:** Arquitectura y Sistemas Operativos
* **Alumna:** Rodriguez Zulema
  

---

I. Descripción del Proyecto

Este Trabajo Final Integrador demuestra la convergencia práctica entre la administración de sistemas operativos empresariales Linux, el aprovisionamiento de servicios web, la parametrización de redes lógicas y el desarrollo de algoritmos automatizados con interacción directa en el sistema de archivos.

El sistema consta de un script adaptativo en Python 3 que interactúa de forma transaccional con estructuras de datos dinámicas en memoria RAM (listas) y almacenamiento persistente (notas.txt) para calcular promedios numéricos y renderizar en tiempo real la interfaz dinámica del servidor web HTTP Apache2.

II. CONTINGENCIA TECNOLÓGICA: MIGRACIÓN DE ENTORNO LOCAL A LA NUBE (IaaS)

El diseño original del proyecto contemplaba una solución de virtualización local mediante una máquina virtual en Oracle VirtualBox (Hipervisor Tipo 2 alojado). Durante la fase de inicialización, las políticas estrictas de aislamiento de núcleo e integridad de memoria nativas de Windows 11 provocaron un bloqueo crítico de tipo VBoxHardening (Código de error 0x80004005), impidiendo el acceso a registros raíz esenciales de la CPU como el CR3.

Priorizando la continuidad operativa, se aplicó un criterio de contingencia profesional migrando la infraestructura hacia el modelo IaaS (Infrastructure as a Service) mediante Google Cloud Shell. Esta arquitectura implementa virtualización a nivel de Sistema Operativo mediante contenedores ligeros que comparten el kernel del host, reduciendo el overhead de hardware y evadiendo los bloqueos locales. Debido a esta optimización, el entorno prescinde del gestor tradicional systemd (PID 1), requiriendo la administración pura del Daemon web a través de la interfaz de línea de comandos (CLI).

III. ESPECIFICACIONES TÉCNICAS Y SECUENCIA DE COMANDOS (CLI)

1. ACTUALIZACIÓN E INSTALACIÓN DEL SERVIDOR WEB
   
Se actualizan los repositorios del gestor de paquetes Advanced Package Tool (APT) para sincronizar las firmas de software de los repositorios e instalar el servidor HTTP Apache2 en el entorno virtual:

Bash

sudo apt-get update && sudo apt-get install apache2 -y

2. PARAMETRIZACIÓN Y REDIRECCIÓN DEL PUERTO LÓGICO
Debido a las restricciones de seguridad perimetral de la infraestructura de Google Cloud, los puertos privilegiados por debajo del 1024 (como el HTTP 80 estándar) están bloqueados para accesos externos directos. Se implementa el editor de flujo sed para modificar la directiva en caliente y mapear la escucha al puerto lógicamente abierto 8080:

Bash

sudo sed -i 's/Listen 80/Listen 8080/g' /etc/apache2/ports.conf

3. ADMINISTRACIÓN Y CONTROL DE EJECUCIÓN DEL DAEMON
Ante la ausencia de los componentes del sistema de inicialización systemctl dentro del contenedor, se interactúa en modo directo con el script de control del binario de Apache para acoplar y arrancar el proceso en segundo plano:

Bash

sudo apache2ctl start

4. ACCESO Y ESCRITURA DEL BACKEND DE PROCESAMIENTO
Se invoca el editor nativo por consola nano elevando privilegios con el comando sudo (SuperUser Do) al espacio de memoria del Kernel (Kernel-mode), permitiendo la escritura y almacenamiento del script en la ruta absoluta indexada por el servidor web:

Bash

sudo nano /var/www/html/promedio.py

5. DESPLIEGUE, VALIDACIÓN Y CICLO DE VIDA DEL PROCESO
Para consolidar la lógica, se invoca al intérprete de Python 3 para que lea el archivo descriptor, procese las operaciones I/O en la memoria RAM y genere el documento dinámico de salida index.html. El éxito de la transacción valida por completo la arquitectura Cliente-Servidor:

Bash

sudo python3 /var/www/html/promedio.py

CONCLUSIÓN GENERAL DEL PROYECTO
La resolución de este Trabajo Integrador demuestra rigurosamente la interconexión práctica de los contenidos mínimos de la materia:

VIRTUALIZACIÓN Y REDES: El correcto aprovisionamiento de servicios de red e interacción de disco dentro de entornos virtuales controlados en la nube, mapeando sockets en puertos alternativos (8080).

PLANIFICACIÓN Y MEMORIA: La asignación dinámica de buffers de memoria RAM para almacenar estructuras de datos eficientes (in-memory), mitigando los costos de latencia mecánica de los discos.

SISTEMA DE ARCHIVOS Y GESTIÓN DE E/S: El control estricto de excepciones de Entrada y Salida (try-except) al manipular descriptores de archivos, asegurando que la interfaz cliente-servidor responda eficientemente con estados HTTP estables.

LINK DEL VIDEO: https://drive.google.com/file/d/1c2voloBOsMYYIGBAlGOVWTkyAujaUyEx/view?usp=sharing
