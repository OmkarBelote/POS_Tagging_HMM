# 🧠 POS Tagging using Hidden Markov Model (HMM)

This project implements a simple **Part-of-Speech (POS) Tagger** using the **Hidden Markov Model (HMM)** algorithm — built from scratch without using advanced NLP libraries like spaCy or NLTK.

It allows users to input sentences and view the predicted POS tags via a user-friendly web interface built using Flask and deployed on Render.

---

## 🔍 What is POS Tagging?

**POS Tagging** is the process of assigning parts of speech (such as noun, verb, adjective, etc.) to each word in a sentence based on both its definition and context.

This project uses:
- **HMM (Hidden Markov Model)** for tagging
- **Viterbi Algorithm** for decoding the best tag sequence
- **Simple training corpus** to learn transition and emission probabilities

---

## 🚀 Live Demo

🌐 [POS_Tagging_HMM](https://pos-tagging-hmm.onrender.com)

---

## 🛠️ Features

- Input a sentence and get POS tags instantly
- Lightweight and fast implementation
- No external NLP libraries
- Deploy-ready Flask app
- Clean and minimal UI

---

## 🧾 Example Input

Input Sentence: He is playing football

Output: [('He', 'PRON'), ('is', 'AUX'), ('playing', 'VERB'), ('football', 'NOUN')]


---

## ⚙️ Built With

- Python 3
- Flask
- Gunicorn (for deployment)
- NumPy, Pandas

---

## 👨‍💻 Author

**Omkar Belote** (📚 B.Tech Computer Engineering | Minor in Data Science)
- LinkedIn: [omkarbelote](https://www.linkedin.com/in/omkarbelote/)
- Mail: [omkarbelote@gmail.com](mailto:omkarbelote@gmail.com)

