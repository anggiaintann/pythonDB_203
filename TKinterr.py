import tkinter as tk # Mengimpor tkinter untuk pembuatan GUI
import sqlite3 # Mengimpor sqlite3 untuk berinteraksi dengan SQLite Database
from tkinter import messagebox # Untuk menampilkan pesan dialog

def hasil_prediksi():
    # Mendapatkan nilai dari input
    nama = entry_nama.get()
    # Mendapatkan nilai dari 10 mata pelajaran
    nilai_matematika = float(entry_matematika.get())
    nilai_fisika = float(entry_fisika.get())
    nilai_kimia = float(entry_kimia.get())
    nilai_biologi = float(entry_biologi.get())
    nilai_indonesia = float(entry_inggris.get())
    nilai_inggris = float(entry_inggris.get())
    nilai_ekonomi = float(entry_ekonomi.get())
    nilai_geografi = float(entry_geografi.get())
    nilai_sosiologi = float(entry_sosiologi.get())
    nilai_komputer = float(entry_komputer.get())

    # Menentukan hasil prediksi berdasarkan nilai tertinggi
    nilai_tinggi = max(nilai_matematika, nilai_fisika, nilai_kimia, nilai_biologi, nilai_indonesia,
                       nilai_inggris, nilai_ekonomi, nilai_geografi, nilai_sosiologi,
                       nilai_komputer)

    # Kondisi untuk setiap mata pelajaran
    if nilai_tinggi == nilai_biologi:
        hasil_fakultas = "Kedokteran"
    elif nilai_tinggi == nilai_fisika:
        hasil_fakultas = "Teknik"
    elif nilai_tinggi == nilai_inggris:
        hasil_fakultas = "Bahasa"
    elif nilai_tinggi == nilai_matematika:
        hasil_fakultas = "FMIPA"
    elif nilai_tinggi == nilai_kimia:
        hasil_fakultas = "Farmasi"
    elif nilai_tinggi == nilai_indonesia:
        hasil_fakultas = "Bahasa"
    elif nilai_tinggi == nilai_ekonomi:
        hasil_fakultas = "FEB"
    elif nilai_tinggi == nilai_geografi:
        hasil_fakultas = "Ilmu Sosial"
    elif nilai_tinggi == nilai_sosiologi:
        hasil_fakultas = "Ilmu Sosial"
    elif nilai_tinggi == nilai_komputer:
        hasil_fakultas = "Ilmu Komputer"
    # Kondisi jika kondisi sebelumnya tidak terpenuhi
    else:
        hasil_fakultas = "Belum dapat diprediksi"

    # Menampilkan hasil prediksi
    hasil.config(text=f"Prodi Pilihan: {hasil_fakultas}")

    # Membuka koneksi ke database SQLite
    conn = sqlite3.connect('prediksi_fakultas_.db')
    # Membuat objek cursor untuk mengeksekusi perintah SQL
    cursor = conn.cursor()
    # Mengeksekusi perintah SQL
    cursor.execute('''CREATE TABLE IF NOT EXISTS prediksi_fakultas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama_siswa TEXT,
                        matematika REAL,
                        fisika REAL,
                        kimia REAL,
                        biologi REAL,
                        indonesia REAL,
                        inggris REAL,
                        ekonomi REAL,
                        geografi REAL,
                        sosiologi REAL,
                        komputer REAL,
                        prediksi_fakultas TEXT
                    )''')
    cursor.execute('''INSERT INTO prediksi_fakultas (nama_siswa, matematika, fisika, kimia, biologi,
                    indonesia, inggris, ekonomi, geografi, sosiologi, komputer, prediksi_fakultas)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (nama, nilai_matematika, nilai_fisika, nilai_kimia, nilai_biologi, nilai_indonesia,
                    nilai_inggris, nilai_ekonomi, nilai_geografi, nilai_sosiologi,
                    nilai_komputer, hasil_fakultas))
    conn.commit() # Mengonfirmasi perubahan ke database
    conn.close() # Menutup koneksi ke database

# Menampilkan pesan sukses setelah data disimpan
    messagebox.showinfo("Info", "Data berhasil disimpan dengan baik")

root = tk.Tk() # Membuat objek utama Tkinter
root.title("Aplikasi Prediksi Prodi Pilihan") # Memberi judul pada jendela utama
root.geometry("500x600")  # Mengatur ukuran jendela utama

# Label judul
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
label_judul.pack(pady=10) # Menempatkan label dan menetapkan jarak sebesar 10 piksel

# Input nilai mata pelajaran
label_nama = tk.Label(root, text="Nama Siswa: ") # Membuat label untuk Nama Siswa
label_nama.pack() # Menempatkan label dalam jendela
entry_nama = tk.Entry(root) # Kotak entry untuk memasukkan Nama
entry_nama.pack() # Menempatkan kotak entri dalam jendela

# Membuat 10 label dan entry baru untuk 10 mata pelajaran
label_matematika = tk.Label(root, text="Nilai Matematika: ") # Membuat label 'Nilai Matematika:'
label_matematika.pack() # Menempatkan label Matematika dalam jendela
entry_matematika = tk.Entry(root) # Membuat widget entri untuk memasukkan nilai Matematika
entry_matematika.pack() # Menempatkan widget entri Matematika dalam jendela

label_fisika = tk.Label(root, text="Nilai Fisika: ") # Membuat label 'Nilai Fisika:'
label_fisika.pack() # Menempatkan label Fisika dalam jendela
entry_fisika = tk.Entry(root) # Membuat widget entri untuk memasukkan nilai Fisika
entry_fisika.pack() # Menempatkan widget entri Fisika dalam jendela

label_kimia = tk.Label(root, text="Nilai Kimia: ") # Membuat label 'Nilai Kimia:'
label_kimia.pack() # Menempatkan label Kimia dalam jendela
entry_kimia = tk.Entry(root) # Membuat widget entri untuk memasukkan nilai Kimia
entry_kimia.pack() # Menempatkan widget entri Kimia dalam jendela

label_biologi = tk.Label(root, text="Nilai Biologi: ") # Membuat label 'Nilai Biologi:'
label_biologi.pack() # Menempatkan label Biologi dalam jendela
entry_biologi = tk.Entry(root) # Membuat widget entri untuk memasukkan nilai Biologi
entry_biologi.pack() # Menempatkan widget entri Biologi dalam jendela

label_indonesia = tk.Label(root, text="Nilai Indonesia: ") # Membuat label 'Nilai Indonesia:'
label_indonesia.pack() # Menempatkan label Indonesia dalam jendela
entry_indonesia = tk.Entry(root) # Membuat widget entri untuk memasukkan nilai Indonesia
entry_indonesia.pack() # Menempatkan widget entri Indonesia dalam jendela

label_inggris = tk.Label(root, text="Nilai Inggris: ") # Membuat label 'Nilai Inggris:'
label_inggris.pack() # Menempatkan label Inggris dalam jendela
entry_inggris = tk.Entry(root) # Membuat widget entri untuk memasukkan nilai Inggris
entry_inggris.pack() # Menempatkan widget entri Inggris dalam jendela

label_ekonomi = tk.Label(root, text="Nilai Ekonomi: ") # Membuat label 'Nilai Ekonomi:'
label_ekonomi.pack() # Menempatkan label Ekonomi dalam jendela
entry_ekonomi = tk.Entry(root) # Membuat widget entri untuk memasukkan nilai Ekonomi
entry_ekonomi.pack() # Menempatkan widget entri Ekonomi dalam jendela

label_geografi = tk.Label(root, text="Nilai Geografi: ") # Membuat label 'Nilai Geografi:'
label_geografi.pack() # Menempatkan label Geografi dalam jendela
entry_geografi = tk.Entry(root) # Membuat widget entri untuk memasukkan nilai Geografi
entry_geografi.pack() # Menempatkan widget entri Geografi dalam jendela

label_sosiologi = tk.Label(root, text="Nilai Sosiologi: ") # Membuat label 'Nilai Sosiologi:'
label_sosiologi.pack() # Menempatkan label Sosiologi dalam jendela
entry_sosiologi = tk.Entry(root) # Membuat widget entri untuk memasukkan nilai Sosiologi
entry_sosiologi.pack() # Menempatkan widget entri Sosiologi dalam jendela

label_komputer = tk.Label(root, text="Nilai Komputer: ") # Membuat label 'Nilai Komputer:""
label_komputer.pack() # Menempatkan label Komputer dalam jendela
entry_komputer = tk.Entry(root) # Membuat widget entri untuk memasukkan nilai Komputer
entry_komputer.pack() # Menempatkan widget entri Komputer dalam jendela

# Button Submit Nilai
button_submit = tk.Button(root, text="Submit Nilai", command=hasil_prediksi) # Membuat tombol submit
button_submit.pack(pady=10) # Menempatkan tombol dan menetapkan jarak sebesar 10 piksel

# Label luaran hasil prediksi
hasil = tk.Label(root, text="Prodi Pilihan: ", font=("Arial", 12)) # Label untuk menampilkan hasil
hasil.pack() # Menempatkan label hasil dalam jendela

# Memulai loop utama Tkinter
root.mainloop()
