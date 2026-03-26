# 📄 PDF Text Extractor

> A clean and simple **Streamlit** web application that lets you upload any PDF file and instantly extract all the text content from it.

---

## 🔍 Overview

**PDF Text Extractor** is a lightweight Python web app built with **Streamlit**. Users can upload any `.pdf` file through the browser interface, and the app will extract and display all readable text from every page — no installation of complex software required.

---

## ✨ Features

- 📁 Upload any PDF file directly from your browser
- 📃 Extracts text from **all pages** automatically
- 🖼️ Custom SVG PDF icon rendered inline via Base64
- 🧹 Clean, minimal UI with a scrollable text output area
- ⚡ Instant results — no backend server needed beyond Streamlit

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| `Python 3.11.9` | Core programming language |
| `Streamlit` | Web UI framework |
| `PyPDF2` | PDF reading & text extraction |
| `base64` | Inline SVG icon encoding |

---

## 🚀 How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/ajajmahmudaquil/PDF_Text_Extractor.git
cd PDF_Text_Extractor
```

### 2. Install Dependencies

```bash
pip install streamlit PyPDF2
```

### 3. Run the App

```bash
streamlit run main.py
```

### 4. Open in Browser

Streamlit will automatically open the app at:
```
http://localhost:8501
```

---

## ⚙️ How It Works

1. The app renders a custom **SVG PDF icon** using Base64 encoding alongside the app title.
2. A **file uploader** widget accepts `.pdf` files from the user.
3. Once a file is uploaded, `PyPDF2.PdfReader` reads each page of the PDF.
4. Text is extracted page by page and concatenated into a single string.
5. The extracted text is displayed inside a **scrollable text area** for easy reading and copying.

---

## 👤 Author & Contact

**Ajaj Mahmud Aquil**
- GitHub: [@ajajmahmudaquil](https://github.com/ajajmahmudaquil)
- Portfolio: [aquils-portfolio.vercel.app](https://aquils-portfolio.vercel.app/)

---

> ⭐ If you found this project helpful, please give it a star on GitHub!
