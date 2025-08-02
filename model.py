
def generate_answer(question, context_docs):
    """
    Dummy LLM-based answer generator for demo purposes.
    Replace with IBM Granite LLM API call.
    """
    context = "\n".join(context_docs)
    return f"[Simulated Answer] Based on the context: {context[:200]}..."


# college_admission_agent/retriever.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Dummy dataset
DOCUMENTS = [
    "The last date to apply for B.Tech is 15th July.",
    "The eligibility for MBA is graduation with at least 50%.",
    "The fee for B.Tech in Computer Science is INR 90,000 per year.",
    "Documents required include 10th and 12th marksheets, ID proof, and passport size photo."
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(DOCUMENTS)

def retrieve_context(question, top_k=2):
    query_vec = vectorizer.transform([question])
    similarities = cosine_similarity(query_vec, X).flatten()
    top_indices = similarities.argsort()[::-1][:top_k]
    return [DOCUMENTS[i] for i in top_indices]
