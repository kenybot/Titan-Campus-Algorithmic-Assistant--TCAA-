import tkinter as tk
from tkinter import filedialog, messagebox
import time
import docx
import PyPDF2

# --- File loaders ---
def load_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_docx(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def load_pdf(path):
    text = ""
    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

# --- Algorithms ---
def naive_search(text, pattern):
    matches = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            matches.append(i)
    return matches

def rabin_karp(text, pattern, prime=101):
    matches = []
    m, n = len(pattern), len(text)
    pat_hash = sum(ord(pattern[i]) * (prime**i) for i in range(m))
    text_hash = sum(ord(text[i]) * (prime**i) for i in range(m))

    for i in range(n - m + 1):
        if pat_hash == text_hash and text[i:i+m] == pattern:
            matches.append(i)
        if i < n - m:
            text_hash = (text_hash - ord(text[i])) // prime + ord(text[i+m]) * (prime**(m-1))
    return matches

def kmp_search(text, pattern):
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    matches = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j-1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            matches.append(i - j + 1)
            j = lps[j-1]
    return matches

# --- Comparison Runner ---
def run_search(text, pattern, mode="ALL"):
    results = {}
    algos = {
        "Naive": naive_search,
        "Rabin-Karp": rabin_karp,
        "KMP": kmp_search
    }

    if mode == "ALL":
        chosen_algos = algos
    else:
        chosen_algos = {mode: algos[mode]}

    for name, func in chosen_algos.items():
        start = time.perf_counter()
        matches = func(text, pattern)
        elapsed = time.perf_counter() - start
        results[name] = {"matches": matches, "time": elapsed}
    return results

# --- Tkinter UI ---
def create_search_ui():
    root = tk.Tk()
    root.title("Notes Search Engine")

    text_data = {"content": ""}

    # File upload
    def upload_file():
        file_path = filedialog.askopenfilename(filetypes=[("Documents", "*.txt *.docx *.pdf")])
        if not file_path:
            return
        try:
            if file_path.endswith(".txt"):
                text_data["content"] = load_txt(file_path)
            elif file_path.endswith(".docx"):
                text_data["content"] = load_docx(file_path)
            elif file_path.endswith(".pdf"):
                text_data["content"] = load_pdf(file_path)
            messagebox.showinfo("File Loaded", f"Loaded {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

    # Search
    def search():
        if not text_data["content"]:
            messagebox.showwarning("No File", "Please upload a file first.")
            return
        pattern = pattern_entry.get().strip()
        if not pattern:
            messagebox.showwarning("No Pattern", "Please enter a search pattern.")
            return
        mode = algo_var.get()
        results = run_search(text_data["content"], pattern, mode)

        output_text.delete("1.0", tk.END)
        for algo, data in results.items():
            output_text.insert(tk.END, f"{algo}:\n")
            output_text.insert(tk.END, f"  Matches at indices: {data['matches']}\n")
            output_text.insert(tk.END, f"  Time taken: {data['time']:.6f} seconds\n\n")

    # Widgets
    tk.Button(root, text="Upload File", command=upload_file).pack(pady=5)

    tk.Label(root, text="Search Pattern:").pack()
    pattern_entry = tk.Entry(root, width=40)
    pattern_entry.pack(pady=5)

    algo_var = tk.StringVar(value="ALL")
    tk.Label(root, text="Choose Algorithm:").pack()
    tk.OptionMenu(root, algo_var, "Naive", "Rabin-Karp", "KMP", "ALL").pack(pady=5)

    tk.Button(root, text="Run Search", command=search).pack(pady=10)

    output_text = tk.Text(root, height=20, width=80)
    output_text.pack(padx=10, pady=10)


# Run the UI
if __name__ == "__main__":
    create_search_ui()