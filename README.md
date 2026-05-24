# Proyecto 6: Computer Vision

Proyecto de Visión por Computadora con DeepFace. Este proyecto utiliza la librería DeepFace para realizar reconocimiento facial en tiempo real mediante una cámara web. El sistema compara los rostros capturados con una base de datos de imágenes almacenadas localmente.

Requisitos: Python 3.10 o superior, cámara web y pip instalado.

Instalación: primero clona el repositorio con el comando git clone https://github.com/izzZk-hub/Computer-Vision.git y entra a la carpeta del proyecto con cd Computer-Vision. Después crea un entorno virtual con python -m venv venv y actívalo en Windows con venv\Scripts\activate. Posteriormente instala las dependencias con pip install -r requirements.txt.

Ejecución: para correr el proyecto ejecuta python main.py.

Estructura del proyecto: el repositorio contiene el archivo main.py que ejecuta el sistema, requirements.txt con las dependencias necesarias, README.md con la documentación del proyecto y la carpeta faces donde se almacenan las imágenes de referencia como checo.jpg o persona1.jpg.

Funcionamiento: el sistema abre la cámara web, detecta rostros en tiempo real, los compara con las imágenes dentro de la carpeta faces y muestra el nombre del archivo reconocido en caso de coincidencia.

Autor: proyecto basado en un fork del repositorio https://github.com/PinedaAlan/Computer-Vision.