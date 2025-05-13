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

![Hide Text Screenshot](https://via.placeholder.com/600x300?text=Hide+Text+CLI)

### 🔍 Extracting Hidden Text

![Extract Text Screenshot](https://via.placeholder.com/600x300?text=Extract+Text+CLI)

---

## 🛠️ Requirements

Install dependencies from the provided `requirements.txt`:

```bash
pip install -r requirements.txt
