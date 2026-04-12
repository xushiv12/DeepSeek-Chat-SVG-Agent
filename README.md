# DeepSeek SVG Image Generator

## 🚀 Overview

This project is an AI-powered image generation system based on SVG composition.

Instead of generating images pixel-by-pixel, it uses the DeepSeek Chat API to generate SVG code, which is then rendered into visual images in the browser.

The system combines:

* Natural language prompts
* AI-generated SVG structure
* Pre-prepared image assets
* Browser rendering

👉 Result: Users can generate images from text prompts in a lightweight and controllable way.

---

## 🧠 How It Works

1. User enters a prompt (e.g. "a man in the rain")
2. The backend sends the prompt to DeepSeek API
3. DeepSeek generates SVG code based on the prompt
4. SVG references pre-defined image assets (PNG files)
5. Browser renders the SVG into a final image

---

## 🧩 Key Features

* 🎯 Prompt-based image generation
* 🧱 SVG structure generation (not pixel-based)
* 🖼️ Asset-based composition system
* ⚡ Lightweight (no heavy GPU or training required)
* 🔧 Fully controllable output

---

## 📂 Project Structure

```
.
├── static/          # Image assets (PNG files)
├── templates/       # HTML templates
│   ├── 1.html       # Home page
│   └── 2.html       # Image generator page
├── 1.py             # Main Flask app
├── lib.py           # DeepSeek API logic
```

---

## ⚙️ Installation

```bash
pip install flask openai
```

---

## ▶️ Run the Project

```bash
python 1.py
```

Then open in browser:

```
http://localhost:5000
```

---

## 🖼️ Example

Input:

```
a man in the rain
```

Output:

* AI generates SVG
* Combines assets
* Renders a composed image

---

## 🔥 Innovation

This project introduces a different approach to AI image generation:

👉 Instead of generating pixels, it generates structured SVG code.

👉 Instead of relying on heavy models, it uses lightweight asset composition.

This makes the system:

* More controllable
* More efficient
* Easier to deploy

---

## 🆚 Comparison

| Method         | Description                     |
| -------------- | ------------------------------- |
| Traditional AI | Generates images pixel-by-pixel |
| This Project   | Generates SVG + combines assets |

---

## 📌 Future Improvements

* Add more image assets
* Improve composition logic
* Add randomness for more diversity
* Support more complex scenes

---

## 🧑‍💻 Author

Created by you 🚀

---

## 📄 License

MIT License (you can change this if needed)
