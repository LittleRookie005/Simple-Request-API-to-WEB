from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)


@app.route('/')
def transaksi():
    url = 'http://127.0.0.1:5000/api/mastertransaksi'
    response_info = requests.get(url)
    response = response_info.json()

    data_j = response['data']

    lis = []
    for i in data_j:
        id_produk = i['id_produk']
        id_transaksi = i['id_transaksi']
        jumlah_barang = i['jumlah_barang']
        nama_produk = i['nama_produk']
        profit_bersih = i['profit_bersih']
        tanggal_transaksi =i['tanggal_transaksi']
        total_harga = i['total_harga']
        lis.append(i)

    data_i = response['total_profit_bersih']
    return render_template('index.html', data=lis, datas=data_i)

if __name__ == '__main__':
    app.run(debug=True, port=5055)