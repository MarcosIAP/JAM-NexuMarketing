from flask import Flask, render_template_string
import json

app = Flask(__name__)

# Datos de ejemplo desde un archivo JSON
with open('anuncios.json', 'r', encoding='utf-8') as f:
    anuncios = json.load(f)

# Ruta para la página principal
@app.route('/')
def index():
    # Renderiza el HTML con los datos de anuncios
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi Página Mejorada</title>
        <!-- Bootstrap CSS -->
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <header class="bg-primary text-white text-center py-3">
            <h1>Bienvenido a Mi Página Mejorada</h1>
        </header>
        <main class="container mt-5">
            <!-- Sección de Anuncios -->
            <section id="anuncios" class="my-5">
                <h2 class="text-center">Anuncios</h2>
                <div class="row">
                    {% for anuncio in anuncios %}
                    <div class="col-md-4">
                        <div class="card mb-4">
                            <img src="{{ anuncio['imagen'] }}" class="card-img-top" alt="{{ anuncio['nombre'] }}">
                            <div class="card-body">
                                <h5 class="card-title">{{ anuncio['nombre'] }}</h5>
                                <p class="card-text">
                                    Tamaño de Público Estimado: {{ anuncio['publico_estimado'] }}<br>
                                    Importe Gastado: {{ anuncio['importe_gastado'] }}<br>
                                    Impresiones: {{ anuncio['impresiones'] }}<br>
                                    Fecha Inicio: {{ anuncio['fecha_inicio'] }}<br>
                                    Fecha Final: {{ anuncio['fecha_final'] }}<br>
                                    <a href="{{ anuncio['url_producto'] }}" target="_blank">Ver Producto</a><br>
                                    Número de Vistas: {{ anuncio['vistas'] }}
                                </p>
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                </div>
            </section>
        </main>
        <!-- Bootstrap JS and dependencies -->
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
    </html>
    """, anuncios=anuncios)

if __name__ == '__main__':
    app.run(debug=True)
