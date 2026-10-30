# <p align="center">🚀 DYNAMIC SIGN LANGUAGE TRANSLATOR</p>
## <p align="center">🤟 Trainable, Real-Time Sign Language Translator</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/MediaPipe-00C7B7?style=for-the-badge&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white" />
</p>

<p align="center">
  <a href="#-english"><b>🇬🇧 English</b></a> · <a href="#-türkçe"><b>🇹🇷 Türkçe</b></a>
</p>

---

## 🇬🇧 English

### 📝 About the Project
This project was developed as the final assignment of the **Digital Image Processing** course. Its main focus is to interpret sign language gestures in real time using image segmentation, computer vision and deep learning techniques.

Instead of relying on fixed datasets, the core of the project is a **"Dynamic Training Module"** that lets users teach the system their own signs and train the model directly from the interface.

### 🌟 Key Features
* **📍 Precise tracking:** Real-time tracking of hand and body landmarks with **MediaPipe**.
* **🧠 Motion analysis:** An **LSTM** architecture that processes time-series data and classifies gesture sequences.
* **🖥️ User interface:** A **PyQt5** control panel that manages data collection, model training and prediction.
* **🔊 Text-to-speech:** Recognised phrases are spoken instantly with **gTTS** and **pyttsx3**.
* **📂 Flexible dataset:** Add new words directly from the interface, no coding needed.

### 🛠️ Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Image processing** | MediaPipe | Landmark tracking and feature extraction |
| **Deep learning** | TensorFlow / Keras | LSTM-based gesture recognition |
| **Interface** | PyQt5 & Qt Designer | UI/UX and flow management |
| **Audio** | gTTS & pyttsx3 | Text-to-speech |
| **Language** | Python | Core logic and scripting |

### 🚀 Installation and Usage

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

### 📝 Proje Hakkında
Bu çalışma, **Sayısal Görüntü İşleme** dersi final ödevi kapsamında geliştirilmiştir. Projenin temel odağı; görüntü segmentasyonu, bilgisayarlı görü ve derin öğrenme tekniklerini kullanarak işaret dili hareketlerini gerçek zamanlı olarak anlamlandırmaktır.

Sabit veri setlerine bağlı kalmak yerine, kullanıcının kendi işaretlerini sisteme tanıtmasına ve modelini arayüz üzerinden eğitmesine olanak tanıyan **"Dinamik Eğitim Modülü"** projenin temelini oluşturur.

### 🌟 Temel Özellikler
* **📍 Hassas Takip:** **MediaPipe** aracılığıyla el ve vücut eklem noktalarının (landmarks) anlık takibi.
* **🧠 Hareket Analizi:** Zaman serisi verilerini işlemek ve hareket dizilerini sınıflandırmak için kullanılan **LSTM** mimarisi.
* **🖥️ Kullanıcı Arayüzü:** Veri toplama, model eğitimi ve tahmin süreçlerini yöneten **PyQt5** tabanlı kontrol paneli.
* **🔊 Seslendirme:** Algılanan ifadelerin **gTTS** ve **pyttsx3** kütüphaneleri ile anlık sese dönüştürülmesi.
* **📂 Esnek Veri Seti:** Kod yazmaya gerek kalmadan, doğrudan arayüz üzerinden yeni kelimeler ekleyebilme imkanı.

### 🛠️ Teknoloji Yığını

| Bileşen | Teknoloji | Kullanım Amacı |
| :--- | :--- | :--- |
| **Görüntü İşleme** | MediaPipe | Eklem Takibi ve Öznitelik Çıkarımı |
| **Derin Öğrenme** | TensorFlow / Keras | LSTM Tabanlı Hareket Tanıma |
| **Arayüz** | PyQt5 & Qt Designer | UI/UX ve Akış Yönetimi |
| **Ses** | gTTS & pyttsx3 | Metinden Sese Dönüştürme |
| **Dil** | Python | Çekirdek Mantık ve Betikleme |

### 🚀 Kurulum ve Kullanım

> [!IMPORTANT]
> **Adımları takip edin:**
> 1. Gerekli kütüphaneleri yükleyin: `pip install -r IsaretDiliProjesi/requirements.txt`
> 2. Ana uygulamayı başlatın: `cd IsaretDiliProjesi/src && python ana_program.py` (ya da içindeki Python yolunu güncelledikten sonra `baslat.bat`)
> 3. "Veri Topla" sekmesinden yeni işaretler kaydedin veya mevcut modelle tahmine başlayın.

<p align="center">
  <i>Sayısal Görüntü İşleme Akademik Final Projesi - 2026</i>
</p>
