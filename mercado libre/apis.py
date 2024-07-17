from flask import Flask, request, jsonify

app = Flask(__name__)
anuncios = [
    {
        'id': 1,
        'titulo': 'Laptop Asus Asus Tuf Gaming A15 Amd R5 Rtx2050 16gb 512gb Color Negro',
        'tamano_publico_estimado': '10 mil',
        'importe_gastado': 'S/.600',
        'impresiones': '4 mil',
        'fecha_inicio': '2023-01-01',
        'fecha_final': '2023-01-31',
        'url_imagen': 'http://http2.mlstatic.com/D_774375-MLU76509333540_052024-I.jpg',
        'url_producto': 'https://www.mercadolibre.com.mx/laptop-asus-asus-tuf-gaming-a15-amd-r5-rtx2050-16gb-512gb-color-negro/p/MLM37283669',
        'numero_vistas': 1647
    },
    {
        'id': 2,
        'titulo': 'Notebook 245 G9 14in Negro 16gb De Ram - 512gb Ssd - Amd Ryzen 3',
        'tamano_publico_estimado': '20 mil',
        'importe_gastado': 'S/.1000',
        'impresiones': ' 5 mil',
        'fecha_inicio': '2023-02-01',
        'fecha_final': '2023-02-28',
        'url_imagen': 'http://http2.mlstatic.com/D_676170-MLA74065928204_012024-I.jpg',
        'url_producto': 'https://www.mercadolibre.com.mx/notebook-245-g9-14in-negro-16gb-de-ram-512gb-ssd-amd-ryzen-3/p/MLM27440340',
        'numero_vistas': 1501
    },
    {
        'id': 3,
        'titulo': 'Laptop Gamer Thunderobot 911mt 12th Intel Core I7 12650h 16gb De Ram 512gb Ssd, Nvidia Geforce Rtx 3050 165 Hz 1920x1080px Windows 11 Pro',
        'tamano_publico_estimado': '15 mil',
        'importe_gastado': 'S/.800',
        'impresiones': '4 mil',
        'fecha_inicio': '2023-03-01',
        'fecha_final': '2023-03-31',
        'url_imagen': 'http://http2.mlstatic.com/D_901042-MLU76249680093_052024-I.jpg',
        'url_producto': 'https://www.mercadolibre.com.mx/laptop-gamer-thunderobot-911mt-12th-intel-core-i7-12650h-16gb-de-ram-512gb-ssd-nvidia-geforce-rtx-3050-165-hz-1920x1080px-windows-11-pro/p/MLM28131164',
        'numero_vistas': 490
    },
    {
        'id': 4,
        'titulo': 'Laptop Hp 245 G9 Amd Ryzen 3 3250u Hasta 3,5 Ghz, Memoria Ram De 16 Gb Ddr4, Ssd 256 Gb, Windows 11 Home 64-bit, Teclado En Español, 14 Pulgadas, Negro',
        'tamano_publico_estimado': '10 mil',
        'importe_gastado': 'S/.600',
        'impresiones': '2 mil',
        'fecha_inicio': '2023-04-01',
        'fecha_final': '2023-04-30',
        'url_imagen': 'http://http2.mlstatic.com/D_661047-MLU73159073286_122023-I.jpg',
        'url_producto': 'https://www.mercadolibre.com.mx/laptop-hp-245-g9-amd-ryzen-3-3250u-hasta-35-ghz-memoria-ram-de-16-gb-ddr4-ssd-256-gb-windows-11-home-64-bit-teclado-en-espanol-14-pulgadas-negro/p/MLM28615515',
        'numero_vistas': 264
    },
    {
        'id': 5,
        'titulo': 'Laptop Lenovo Ideapad Slim 3 15.6\'\' Ci5 8gb + 512gb Ssd',
        'tamano_publico_estimado': '30 mil',
        'importe_gastado': 'S/.1500',
        'impresiones': '5 mil',
        'fecha_inicio': '2023-05-01',
        'fecha_final': '2023-05-31',
        'url_imagen': 'http://http2.mlstatic.com/D_621621-MLU73824611655_012024-I.jpg',
        'url_producto': 'https://www.mercadolibre.com.mx/laptop-lenovo-ideapad-slim-3-156-ci5-8gb-512gb-ssd/p/MLM28619487',
        'numero_vistas': 585
    },
    {
        'id': 6,
        'titulo': 'Laptop Acer Aspire 3 15.6 Ryzen 7, 16gb/512gb, Windows 11 Color Plateado',
        'tamano_publico_estimado': '40 mil',
        'importe_gastado': 'S/.1600',
        'impresiones': '12 mil',
        'fecha_inicio': '2023-06-01',
        'fecha_final': '2023-06-30',
        'url_imagen': 'http://http2.mlstatic.com/D_701272-MLU75124279282_032024-I.jpg',
        'url_producto': 'https://www.mercadolibre.com.mx/laptop-acer-aspire-3-156-ryzen-7-16gb512gb-windows-11-color-plateado/p/MLM34680070',
        'numero_vistas': 4509
    },
    {
        'id': 7,
        'titulo': 'Laptop Asus Vivobook F15 15.6 Core I7 1255u 16g 512g Ssd W11 Color Azul',
        'tamano_publico_estimado': '40 mil ',
        'importe_gastado': 'S/.1700',
        'impresiones': '14 mil',
        'fecha_inicio': '2023-07-01',
        'fecha_final': '2023-07-31',
        'url_imagen': 'http://http2.mlstatic.com/D_976166-MLU73572150103_122023-I.jpg',
        'url_producto': 'https://www.mercadolibre.com.mx/laptop-asus-vivobook-f15-156-core-i7-1255u-16g-512g-ssd-w11-color-azul/p/MLM29184265',
        'numero_vistas': 4335
    },
    {
        'id': 8,
        'titulo': 'Laptop Hp 240 G9 Intel Core I3 1215u 512gb Ssd 16gb Ram 1366x768px Windows 11 Home + Antivirus Norton 360',
        'tamano_publico_estimado': '20 mil',
        'importe_gastado': 'S/.1000',
        'impresiones': '4 mil',
        'fecha_inicio': '2023-08-01',
        'fecha_final': '2023-08-31',
        'url_imagen': 'http://http2.mlstatic.com/D_656246-MLU77088905699_062024-I.jpg',
        'url_producto': 'https://www.mercadolibre.com.mx/laptop-hp-240-g9-intel-core-i3-1215u-512gb-ssd-16gb-ram-1366x768px-windows-11-home-antivirus-norton-360/p/MLM37794644',
        'numero_vistas': 469
    },
    {
        'id': 9,
        'titulo': '14.1\'\' Laptop 8 Ram+512gb Ssd Intel Celeron N4000 Windows 11',
        'tamano_publico_estimado': '10 mil',
        'importe_gastado': 'S/.600',
        'impresiones': '2 mil',
        'fecha_inicio': '2023-09-01',
        'fecha_final': '2023-09-30',
        'url_imagen': 'http://http2.mlstatic.com/D_653954-MLM76337017754_052024-I.jpg',
        'url_producto': 'https://articulo.mercadolibre.com.mx/MLM-3048177446-141-laptop-8-ram512gb-ssd-intel-celeron-n4000-windows-11-_JM',
        'numero_vistas': 541
    },
    {
        'id': 10,
        'titulo': 'Notebook Victus 15-fb1013dx 15.6  Gris 16gb De Ram - 512gb Ssd - Amd Ryzen 5',
        'tamano_publico_estimado': '40 mil',
        'importe_gastado': 'S/.1700',
        'impresiones': '14 mil',
        'fecha_inicio': '2023-09-01',
        'fecha_final': '2023-09-30',
        'url_imagen': 'http://http2.mlstatic.com/D_988145-MLA73121991789_112023-I.jpg',
        'url_producto': 'https://www.mercadolibre.com.mx/notebook-victus-15-fb1013dx-156-gris-16gb-de-ram-512gb-ssd-amd-ryzen-5/p/MLM28527799',
        'numero_vistas': 541
    }
]

# Datos simulados (anuncios iniciales)
@app.route('/anuncios', methods=['GET'])
def get_anuncios():
    return jsonify(anuncios)

@app.route('/anuncios', methods=['POST'])
def create_anuncio():
    anuncio = request.get_json()
    anuncios.append(anuncio)
    return jsonify(anuncio), 201

@app.route('/anuncios/<int:anuncio_id>', methods=['GET'])
def get_anuncio(anuncio_id):
    if anuncio_id >= len(anuncios) or anuncio_id < 0:
        return jsonify({'error': 'Anuncio no encontrado'}), 404
    return jsonify(anuncios[anuncio_id])

@app.route('/anuncios/<int:anuncio_id>', methods=['PUT'])
def update_anuncio(anuncio_id):
    if anuncio_id >= len(anuncios) or anuncio_id < 0:
        return jsonify({'error': 'Anuncio no encontrado'}), 404
    anuncio = request.get_json()
    anuncios[anuncio_id] = anuncio
    return jsonify(anuncio)

@app.route('/anuncios/<int:anuncio_id>', methods=['DELETE'])
def delete_anuncio(anuncio_id):
    if anuncio_id >= len(anuncios) or anuncio_id < 0:
        return jsonify({'error': 'Anuncio no encontrado'}), 404
    anuncio = anuncios.pop(anuncio_id)
    return jsonify(anuncio)

if __name__ == '__main__':
    app.run(debug=True)
