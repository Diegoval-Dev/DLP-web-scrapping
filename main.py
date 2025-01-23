import re
import csv
#https://nitro.gt/categoria-producto/gaming/
def load_html(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()

def buffer(html, buffer_size=8192):
    start = 0
    result = []
    sentinel = "EOF"

    while start < len(html):
        buffer = html[start:start + buffer_size]
        if len(buffer) < buffer_size:
            buffer += sentinel

        regex_name = r'<h2[^>]*class="woocommerce-loop-product__title"[^>]*>(.*?)</h2>'
        regex_image = r'<img[^>]*src="(https://[^"]+)"[^>]*class="[^"]*woocommerce_thumbnail[^"]*"'

        names = re.findall(regex_name, buffer)
        images = re.findall(regex_image, buffer)

        print("Contenido del buffer:", buffer[:200])
        print("Nombres en el buffer:", names)
        print("Imagenes en el buffer:", images)

        result.extend(zip(names, images))
        start += buffer_size

    return result

def export_csv(products, output_file):
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nombre Producto", "URL imagen"])
        writer.writerows(products)

def main():
    html_file = "./kemik_gaming.html"
    csv_file = "products.csv"

    html = load_html(html_file)
    print("Se cargo el html")

    products = buffer(html)

    if products:
        print("Productos extraidos:", products)
        export_csv(products, csv_file)
        print(f"El archivo {csv_file} ha sido generado con los productos encontrados.")
    else:
        print("No se encontraron productos. Verifique las expresiones regulares y el HTML.")

if __name__ == "__main__":
    main()
