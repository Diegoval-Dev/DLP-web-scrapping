# Web Scraping de Productos de nitro.gt 

Este proyecto realiza web scraping en la página de productos de nitro.gt y extrae información sobre los productos, incluyendo el nombre y la URL de la imagen. La información extraída se guarda en un archivo CSV.

## Descripción del Proyecto

El programa:
- Carga el contenido HTML de un archivo.
- Utiliza expresiones regulares para extraer nombres de productos e imágenes.
- Guarda los datos extraídos en un archivo CSV.

## Archivos en el Proyecto

- `main.py`: Código fuente principal que realiza el web scraping y exporta los datos a CSV.
- `kemik_gaming.html`: Archivo HTML de ejemplo que contiene la lista de productos.
- `products.csv`: Archivo CSV generado con los datos de los productos extraídos.

## Requisitos del Sistema

- Python 3.6 o superior.

## Ejecución

1. Clona este repositorio:
  ```bash
  git clone https://github.com/Diegoval-Dev/DLP-web-scrapping
  cd DLP-web-scrapping
  ```
2. Asegúrate de tener el archivo `kemik_gaming.html` en el mismo directorio que `main.py`.
3. Ejecuta el programa:
  ```bash
  python main.py
  ```
4. Observa la salida en la consola y verifica que el archivo `products.csv` ha sido generado con los productos encontrados.

## Explicación Técnica

El programa utiliza las siguientes funciones:

- **`load_html(file)`**: Carga el contenido HTML desde un archivo.
- **`buffer(html, buffer_size=8192)`**: Procesa el contenido HTML en fragmentos y extrae nombres de productos e imágenes utilizando expresiones regulares.
- **`export_csv(products, output_file)`**: Exporta los datos extraídos a un archivo CSV.

## Ejemplo de Entrada y Salida

**Entrada:**
Archivo `kemik_gaming.html` con contenido HTML de productos.

**Salida:**
Archivo `products.csv`

## Video Explicativo