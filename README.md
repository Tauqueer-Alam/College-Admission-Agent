# College-Admission-Agent

# 🎓 College Admission Agent (RAG-Based)

An AI-powered assistant that streamlines the student admission process using **Retrieval-Augmented Generation (RAG)** and **IBM Cloud Lite / IBM Granite** services.

This project helps prospective students ask natural language questions related to:
- Admission deadlines
- Course eligibility
- Fee structure
- Required documents
- Application process

and receive accurate, real-time responses based on official institutional data.

---

## 🚀 Features

✅ Real-time question answering  
✅ Retrieval from trusted admission documents  
✅ IBM Granite-compatible architecture  
✅ Simple web interface with HTML, CSS, and JavaScript  
✅ Deployable on GitHub Pages and IBM Cloud Functions

---

## 🛠️ Tech Stack

| Layer           | Technology                          |
|----------------|--------------------------------------|
| Backend         | Python (Flask)                      |
| ML Retrieval    | TF-IDF + Cosine Similarity          |
| UI              | HTML, CSS, JavaScript (embedded)    |
| Deployment      | GitHub Pages / IBM Cloud Lite       |
| AI Model        | IBM Granite (Simulated currently)   |

---

## 🧠 How It Works

1. **User asks a question** in natural language via web UI.
2. **Retriever module** finds the most relevant document chunks using TF-IDF.
3. **Generator module** simulates a response using the matched context.
4. Response is shown with the context from institutional policy documents.

---

## 📂 Project Structure

