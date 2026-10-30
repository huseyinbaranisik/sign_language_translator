<div align="center">

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Love-You%20Gesture.png" width="110" alt="Love-You Gesture">

# Dynamic Sign Language Translator

<img src="https://readme-typing-svg.demolab.com?font=Space+Grotesk&weight=700&size=22&duration=2600&pause=700&color=00C7B7&center=true&vCenter=true&width=600&lines=Real-time%20sign%20language%20translation;MediaPipe%20%2B%20LSTM%20%2B%20PyQt5;Train%20your%20own%20signs" alt="Real-time sign language translation">

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/MediaPipe-00C7B7?style=for-the-badge&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white" />
</p>

<a href="#-english"><b>🇬🇧 English</b></a> · <a href="#-türkçe"><b>🇹🇷 Türkçe</b></a>

</div>

<br>

<table align="center">
  <tr>
    <td align="center" width="25%"><img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Raised%20Hand.png" width="40" alt="Raised Hand"><br><b>Hand tracking</b><br><sub>MediaPipe</sub></td>
    <td align="center" width="25%"><img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Brain.png" width="40" alt="Brain"><br><b>LSTM</b><br><sub>gesture sequences</sub></td>
    <td align="center" width="25%"><img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Desktop%20Computer.png" width="40" alt="Desktop Computer"><br><b>PyQt5 panel</b><br><sub>collect · train · predict</sub></td>
    <td align="center" width="25%"><img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Speaker%20High%20Volume.png" width="40" alt="Speaker High Volume"><br><b>Speech</b><br><sub>text-to-speech</sub></td>
  </tr>
</table>

---

## 🇬🇧 English

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Memo.png" width="26" align="center"> About the Project
This project was developed as the final assignment of the **Digital Image Processing** course. Its main focus is to interpret sign language gestures in real time using image segmentation, computer vision and deep learning techniques.

Instead of relying on fixed datasets, the core of the project is a **"Dynamic Training Module"** that lets users teach the system their own signs and train the model directly from the interface.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Glowing%20Star.png" width="26" align="center"> Key Features
* **📍 Precise tracking:** Real-time tracking of hand and body landmarks with **MediaPipe**.
* **🧠 Motion analysis:** An **LSTM** architecture that processes time-series data and classifies gesture sequences.
* **🖥️ User interface:** A **PyQt5** control panel that manages data collection, model training and prediction.
* **🔊 Text-to-speech:** Recognised phrases are spoken instantly with **gTTS** and **pyttsx3**.
* **📂 Flexible dataset:** Add new words directly from the interface, no coding needed.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Hammer%20and%20Wrench.png" width="26" align="center"> Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Image processing** | MediaPipe | Landmark tracking and feature extraction |
| **Deep learning** | TensorFlow / Keras | LSTM-based gesture recognition |
| **Interface** | PyQt5 & Qt Designer | UI/UX and flow management |
| **Audio** | gTTS & pyttsx3 | Text-to-speech |
| **Language** | Python | Core logic and scripting |

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" width="26" align="center"> Installation and Usage

> [!IMPORTANT]
> **Follow these steps:**
> 1. Install the required libraries: `pip install -r IsaretDiliProjesi/requirements.txt`
> 2. Start the main application: `cd IsaretDiliProjesi/src && python ana_program.py` (or run `baslat.bat`, after updating the Python path inside it)
> 3. Record new signs from the "Veri Topla" (Collect Data) tab, or start predicting with the existing model.

<p align="center">
  <i>Digital Image Processing — Academic Final Project, 2026</i>
</p>

---

## 🇹🇷 Türkçe

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Memo.png" width="26" align="center"> Proje Hakkında
Bu çalışma, **Sayısal Görüntü İşleme** dersi final ödevi kapsamında geliştirilmiştir. Projenin temel odağı; görüntü segmentasyonu, bilgisayarlı görü ve derin öğrenme tekniklerini kullanarak işaret dili hareketlerini gerçek zamanlı olarak anlamlandırmaktır.

Sabit veri setlerine bağlı kalmak yerine, kullanıcının kendi işaretlerini sisteme tanıtmasına ve modelini arayüz üzerinden eğitmesine olanak tanıyan **"Dinamik Eğitim Modülü"** projenin temelini oluşturur.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Glowing%20Star.png" width="26" align="center"> Temel Özellikler
* **📍 Hassas Takip:** **MediaPipe** aracılığıyla el ve vücut eklem noktalarının (landmarks) anlık takibi.
* **🧠 Hareket Analizi:** Zaman serisi verilerini işlemek ve hareket dizilerini sınıflandırmak için kullanılan **LSTM** mimarisi.
* **🖥️ Kullanıcı Arayüzü:** Veri toplama, model eğitimi ve tahmin süreçlerini yöneten **PyQt5** tabanlı kontrol paneli.
* **🔊 Seslendirme:** Algılanan ifadelerin **gTTS** ve **pyttsx3** kütüphaneleri ile anlık sese dönüştürülmesi.
* **📂 Esnek Veri Seti:** Kod yazmaya gerek kalmadan, doğrudan arayüz üzerinden yeni kelimeler ekleyebilme imkanı.

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Hammer%20and%20Wrench.png" width="26" align="center"> Teknoloji Yığını

| Bileşen | Teknoloji | Kullanım Amacı |
| :--- | :--- | :--- |
| **Görüntü İşleme** | MediaPipe | Eklem Takibi ve Öznitelik Çıkarımı |
| **Derin Öğrenme** | TensorFlow / Keras | LSTM Tabanlı Hareket Tanıma |
| **Arayüz** | PyQt5 & Qt Designer | UI/UX ve Akış Yönetimi |
| **Ses** | gTTS & pyttsx3 | Metinden Sese Dönüştürme |
| **Dil** | Python | Çekirdek Mantık ve Betikleme |

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" width="26" align="center"> Kurulum ve Kullanım

> [!IMPORTANT]
> **Adımları takip edin:**
> 1. Gerekli kütüphaneleri yükleyin: `pip install -r IsaretDiliProjesi/requirements.txt`
> 2. Ana uygulamayı başlatın: `cd IsaretDiliProjesi/src && python ana_program.py` (ya da içindeki Python yolunu güncelledikten sonra `baslat.bat`)
> 3. "Veri Topla" sekmesinden yeni işaretler kaydedin veya mevcut modelle tahmine başlayın.

<p align="center">
  <i>Sayısal Görüntü İşleme Akademik Final Projesi - 2026</i>
</p>


<br>

<div align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Red%20Heart.png" width="22" align="center" alt="Red Heart">
  <sub>Made by <a href="https://github.com/huseyinbaranisik">Hüseyin Baran Işık</a> · Animated emojis: <a href="https://github.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis">Animated Fluent Emojis</a></sub>
</div>
