
# 🎨 Random Name Generator Web App — Flask + Docker

A sleek, emoji-enhanced Flask web app that generates fun, fantasy-style names! 💫

Built with simplicity and deployability in mind using Python, Flask, and Docker. Ideal for developers looking to learn how to containerize Python applications or simply want an aesthetic and functional name generator.

---

## 📦 Features

- 🌈 Clean, beautiful user interface with emojis and color accents.
- 🧝‍♂️ Generates names that sound human or fantasy-inspired — not just gibberish.
- 🔁 User-defined number of names to generate.
- 🐳 Dockerized for easy deployment and sharing.
- 🔥 Super lightweight with minimal files and dependencies.

---

## 📂 Project Structure

```
name-generator-app/
│
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker instructions
└── templates/
    └── index.html       # HTML UI rendered by Flask
```

---

## 🔧 Name Generation Algorithm Explained

The goal is to generate **believable, readable, and memorable names** — not just random noise. Here's how we approach it:

### 🎯 Algorithm Design

- **Three syllable components**:
  - `first_syllables`: Start of the name — familiar prefixes like "An", "El", "Ma".
  - `second_syllables`: Middle — soft sounds to add fluidity like "ra", "vi", "ie".
  - `last_syllables`: Ending — family name components like "son", "wood", "ford".

### 💡 Example Logic

```python
first = random.choice(first_syllables) + random.choice(second_syllables)
last = random.choice(first_syllables) + random.choice(last_syllables)
```

This gives us names like:

- **Elra Manford**
- **Mavi Saanley**
- **Jona Danwood**

Names are formed to resemble fantasy or modern Western naming styles. You could extend this for regional name formats, gender filters, etc.

---

## 🖥️ Run Locally (No Docker Required)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/name-generator-app.git
cd name-generator-app
```

### 2. (Optional) Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Web App

```bash
python app.py
```

### 5. Access the App

Open your browser at:

```
http://localhost:5000
```

Use the input box to select how many names you'd like and click **"✨ Generate!"**.

---

## 🐳 Run with Docker

### 1. Build Docker Image

```bash
docker build -t yourusername/name-generator:latest .
```

> Replace `yourusername` with your Docker Hub username.

### 2. Run the App

```bash
docker run -d -p 5000:5000 yourusername/name-generator
```

Visit:

```
http://localhost:5000
```

---

## ☁️ Push to Docker Hub

### 1. Log In to Docker Hub

```bash
docker login
```

### 2. Tag the Docker Image

```bash
docker tag yourusername/name-generator yourusername/name-generator:latest
```

### 3. Push the Image

```bash
docker push yourusername/name-generator:latest
```

---

## 🌍 Pull & Run Anywhere

On any system with Docker:

```bash
docker pull yourusername/name-generator:latest
docker run -d -p 5000:5000 yourusername/name-generator
```

---

## ✨ Sample Output

| First Name | Last Name   |
|------------|-------------|
| Elra       | Manford     |
| Mavi       | Sonley      |
| Jona       | Danwood     |
| Savi       | Johton      |

---

## 📚 Tech Stack

- Python 3.10+
- Flask
- Jinja2 Templates
- HTML5 & CSS
- Docker

---

## 🛠️ Customization

You can modify the name lists inside `app.py`:

```python
first_syllables = ["An", "El", "Jo", "Lu", "Ma", "Sa", "Na", "Da"]
second_syllables = ["na", "ra", "la", "vi", "el", "ah", "ie", "on"]
last_syllables = ["son", "man", "ley", "ton", "berg", "field", "wood", "ford"]
```

You can also change:

- Styling in `index.html`
- Add new syllable rules
- Modify Flask logic for more input controls

---

## 🤝 Contributing

Contributions are welcome! Open an issue or submit a pull request to:

- Add more syllables
- Support other name styles (e.g., Japanese, Sci-Fi)
- Add REST API endpoints

---

## 📄 License

MIT License — use freely and share widely!

---

## 👨‍💻 Author

Crafted with ❤️ by [Prianshu-git](https://github.com/Prianshu-git)

---

## 📷 Screenshot

![Screenshot 2025-05-22 at 06-05-35 🌟 Name Generator](https://github.com/user-attachments/assets/be2ec801-b170-46dc-900d-53a619e0e696)


---

## 🔗 Useful Links
Start Learning today!
https://prianshu-404daily.hashnode.dev/

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Official Docs](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
