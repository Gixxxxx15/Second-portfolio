from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/kalkulator', methods=['GET', 'POST'])
def kalkulator():
    hasil = ""
    if request.method == 'POST':
        try:
            angka1 = float(request.form.get('angka1', 0))
            angka2 = float(request.form.get('angka2', 0))
            operasi = request.form.get('operasi')

            if operasi == 'tambah':
                hasil = angka1 + angka2
            elif operasi == 'kurang':
                hasil = angka1 - angka2
            elif operasi == 'kali':
                hasil = angka1 * angka2
            elif operasi == 'bagi':
                if angka2 == 0:
                    hasil = "Error: tidak bisa dibagi dengan 0"
                else:
                    hasil = angka1 / angka2

            if isinstance(hasil, float) and hasil.is_integer():
                hasil = int(hasil)

        except ValueError:
            hasil = "Error: Input tidak valid"

    return render_template('kalkulator.html', hasil=hasil)

@app.route('/images')
def images_page():
    return render_template('images.html')

@app.route('/porto')
def porto_page():
    return render_template('porto.html')

@app.route('/profile')
def profile_page():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
