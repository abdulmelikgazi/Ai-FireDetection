import cv2
# from playsound import playsound  # playsound modülüyle ses çalma (yoruma alınmış)

# Yangın tespiti için Haar Cascade sınıflandırıcıyı yükleme
fire_cascade = cv2.CascadeClassifier('fire_detection.xml')

# Kameradan görüntü yakalamak için VideoCapture nesnesi oluşturma
cap = cv2.VideoCapture(0)

# Sonsuz döngü başlatma
while(True):
    ret, frame = cap.read()  # Kameradan bir kare okuma
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Görüntüyü gri tona çevirme
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)  # Yangını tespit etme

    for (x, y, w, h) in fire:
        roi_gray = gray[y:y+h, x:x+w]  # Gri tonlamalı görüntüde tespit edilen yangın bölgesi
        roi_color = frame[y:y+h, x:x+w]  # Orijinal görüntüde tespit edilen yangın bölgesi
        print('Yangın tespit edildi')  # Yangın tespit edildiğini konsola yazdırma
        # playsound('audio.mp3')  # Yangın tespit edildiğinde ses çalma (yoruma alınmış)

    cv2.imshow('Rakwan', frame)  # Görüntüyü gösterme

    if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' tuşuna basıldığında döngüyü kırma
        break

# Kaynakları serbest bırakma
cap.release()
cv2.destroyAllWindows()
