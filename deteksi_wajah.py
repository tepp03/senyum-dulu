import cv2
import random

# Fungsi pilih teks lucu random
def random_text():
    texts = [
        "Halo, manusia!",
        "Wajah terdeteksi!",
        "Keren nih wajahnya!",
        "Smile dulu dong!",
        "Aku bisa lihat kamu!",
        "Jangan lari ya!",
        "Wajah kece detected!"
    ]
    return random.choice(texts)

# Load model deteksi wajah Haarcascade bawaan OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Buka kamera default
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Gagal menangkap gambar dari kamera.")
        break

    # Ubah frame ke grayscale (syarat deteksi wajah)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi wajah
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Gambar kotak kuning dan teks di sekitar wajah yang terdeteksi
    for (x, y, w, h) in faces:
        color = (0, 255, 255)  # kuning dalam format BGR
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 3)
        text = random_text()
        cv2.putText(frame, text, (x, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    # Tampilkan hasilnya
    cv2.imshow("Deteksi Wajah Sederhana", frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bersihkan dan tutup jendela
cap.release()
cv2.destroyAllWindows()
