# Virtulizacion


* Universidad Tecnológica Nacional (UTN)
* **Materia:** Arquitectura y Sistemas Operativos
* **Alumna:** Rodriguez Zulema
  

---

## Descripción del Proyecto
Este Trabajo Final Integrador demuestra la convergencia práctica entre la administración de sistemas operativos empresariales Linux, el aprovisionamiento de servicios web, la parametrización de redes lógicas y el desarrollo de algoritmos automatizados con interacción directa en el sistema de archivos.

El sistema consta de un script adaptativo en Python 3 que interactúa de forma transaccional con estructuras de datos dinámicas en memoria RAM (listas) y almacenamiento persistente (`notas.txt`) para calcular promedios numéricos y renderizar en tiempo real la interfaz dinámica del servidor web HTTP Apache2.

---

##  Contingencia Tecnológica: De Local (Hipervisor Tipo 2) a la Nube (IaaS)
El diseño original del proyecto contemplaba una solución de virtualización local mediante una máquina virtual en **Oracle VirtualBox** (Hipervisor Tipo 2 alojado). Durante la fase de inicialización, las políticas estrictas de aislamiento de núcleo e integridad de memoria nativas de Windows 11 provocaron un bloqueo crítico de tipo `VBoxHardening` (Código de error `0x80004005`), impidiendo el acceso a registros raíz como el CR3.

Priorizando la continuidad operativa, se aplicó un criterio de contingencia profesional migrando la infraestructura hacia el modelo **IaaS (Infrastructure as a Service)** mediante **Google Cloud Shell**. Esta arquitectura implementa virtualización a nivel de Sistema Operativo mediante contenedores ligeros que comparten el kernel del host, reduciendo el *overhead* de hardware y evadiendo los bloqueos locales. Debido a esta optimización, el entorno prescinde del gestor tradicional `systemd` (PID 1), requiriendo la administración pura del Daemon web a través de la CLI.

---

## Especificaciones Técnicas y Comandos Utilizados

### 1. Actualización e Instalación del Servidor Web
```bash
sudo apt-get update && sudo apt-get install apache2 -y
