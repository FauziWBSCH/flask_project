from groq import Groq
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

ai_key = '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'

user = Groq(api_key=ai_key)

def call_ai(year):
    try:
        chat = user.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"berikan satu fakta teknologi menarik pada tahun {year}"
                }
            ],
            model="llama-3.3-70b-versatile",  # Ganti dengan model yang tersedia
            stream=False
        )
        ai_output = chat.choices[0].message.content  # Perbaikan akses atribut
        return ai_output
    except Exception as e:
        print(f"Error: {str(e)}")  # Tambahkan logging untuk debugging
        return "Terjadi kesalahan dalam menghubungkan ke AI"


@app.route('/')
def home():
    web_tittle = 'HALAMAN UTAMA'
    return render_template('home.html', web_tittle=web_tittle)

@app.route('/kalkulator', methods=['GET', 'POST'])
def kalkulator():
    web_tittle = 'HALAMAN KALKULATOR'
    hasil = None
    operasi = None
    angka1 = None
    angka2 = None
    if request.method == 'POST':
        angka1 = float(request.form['angka1'])
        angka2 = float(request.form['angka2'])
        operasi = request.form['operasi']
        if operasi == 'tambah':
            hasil = angka1 + angka2
        elif operasi == 'kurang':
            hasil = angka1 - angka2
        elif operasi == 'kali':
            hasil = angka1 * angka2
        elif operasi == 'bagi':
            hasil = angka1 / angka2
    return render_template('Kalkulator.html', web_tittle=web_tittle, hasil=hasil, operasi=operasi, angka1=angka1,angka2=angka2)

@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    hasil1 = None
    bmi = None
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = weight / ((height / 100)**2)
        if bmi < 18.5:
            hasil1 ='kekurangan berat badan, ayo naikan berat badan anda!'
        elif bmi <= 24.9:
            hasil1 = 'Berat Badan Normal, pertahankan berat badan anda!'
        elif bmi <= 29.9:
            hasil1 = 'Kelebihan Berat Badan, silahkan turunkan berat badan anda!'
        else:
            hasil1 = 'Anda Obesitas, silahkan turunkan berat badan anda sekarang!'
    return render_template('bmi.html', hasil1=hasil1, bmi=bmi)

@app.route('/rumus', methods=['GET', 'POST'])
def rumus():
    hasil = None
    rumus = None
    if request.method == 'POST':
        rumus = request.form['rumus']
        if rumus == 'persegi':
            sisi = request.form['sisi']
            hasil = int(sisi) * int(sisi)
        elif rumus == 'kel-persegi':
            sisi = request.form['sisi2']
            hasil = 4 * int(sisi)
        elif rumus == 'persegi_panjang':
            panjang = request.form['panjang']
            lebar = request.form['lebar']
            hasil = int(panjang) * int(lebar)
        elif rumus == 'kel-persegi_panjang':
            panjang = request.form['panjang2']
            lebar = request.form['lebar2']
            hasil = 2 * (int(panjang) + int(lebar))
        elif rumus == 'segitiga':
            alas = request.form['alas']
            tinggi = request.form['tinggi']
            hasil = 1/2 * int(alas) * int(tinggi)
        elif rumus == 'lingkaran':
            jari_jari = request.form['jari-jari']
            hasil = 3.14 * (int(jari_jari) ** 2)
        elif rumus == 'kel-lingkaran':
            jari_jari = request.form['jari-jari2']
            hasil = 2 * 3.14 * int(jari_jari)
    return render_template('rumus.html', rumus=rumus, hasil=hasil)

@app.route('/umur', methods=['GET', 'POST'])
def umur():
    hasil = None
    umur = None
    ai_output = None
    if request.method == 'POST':
        tahun_lahir = request.form['tahun']
        hasil = datetime.now().year - int(tahun_lahir)
        ai_output = call_ai(tahun_lahir)
        print(ai_output)
    return render_template('age.html', hasil=hasil, umur=umur, ai_output=ai_output)



if __name__ == '__main__':
    app.run(debug=True)
