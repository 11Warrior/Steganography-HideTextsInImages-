# 🕵️‍♂️ Steganography Tool

A simple Python-based steganography CLI tool that allows you to **hide** secret text messages inside image files and **extract** them later. Built with `Pillow` and `NumPy`.

---

## 📸 What is Steganography?

**Steganography** is the art of concealing messages within other non-secret text or media. In this case, messages are hidden in the **least significant bits (LSBs)** of an image's pixels—making them invisible to the naked eye.

---

## 🚀 Features

- 🔐 Hide secret text inside image files
- 🔍 Extract hidden text from steganographic images
- 📂 Supports common image formats: `.png`, `.jpg`, `.jpeg`, `.bmp`, `.webp`
- ✅ Input validation and error handling
- 📦 CLI-based interaction

---

## 🖼️ Output Screenshots

### 🔐 Hiding Text into an Image

![image](https://github.com/user-attachments/assets/baf9f570-a0c7-4b44-939d-9d3431acd235)


### 🔍 Extracting Hidden Text
![image](https://github.com/user-attachments/assets/30ecd34a-78be-48bc-8b0b-cd1e01b9c651)


![Screenshot 2025-05-13 170240](https://github.com/user-attachments/assets/ca0ab72a-2dfe-40c4-a4e0-a4831f9f2b93)

---

## 🛠️ Requirements

Install dependencies from the provided `requirements.txt`:

```bash
pip install -r requirements.txt
