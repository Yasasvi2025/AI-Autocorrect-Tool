```markdown
# 🤖 Intelligent AI Autocorrect Tool

An interactive, Python-powered web application built with **Streamlit** and **TextBlob** that cleans up unstructured text messages, heavy typos, shorthand slang, and confusing contextual word mix-ups, translating them into standard, grammatically correct English sentences.

---

## 🚀 Key Features
* **Dual-Layer Correction Pipeline:** Combines a targeted vocabulary mapper for shorthand/slang with natural language processing (`TextBlob`) for structural sentence context.
* **Context-Aware Processing:** Fixes real-word semantic errors where words are spelled correctly but used incorrectly in context (e.g., changing *fare* to *for* or *wall* to *well*).
* **Live Web Interface:** Interactive text input field with dynamic, instant feedback UI built entirely in Streamlit.
* **Smart Grammar Capitalization:** Automatically formats sentence-starting characters and isolated pronouns (e.g., converting "i" to "I").

---

## 📐 System Architecture & Data Flow

The Intelligent AI Autocorrect Tool uses a hybrid, multi-stage processing pipeline to transform heavily flawed text inputs into meaningful English sentences. By decoupling structural syntax evaluation from literal translation mapping, the architecture remains lightweight, runs instantaneously without heavy hardware requirements, and avoids system-specific library blocks.

### 1. System Architecture Layers
* **User Interface Layer (Front-End):** Built entirely using standard modern Streamlit layouts. It manages session state hooks, live textbox entry capture, dynamic loading indicators (`st.spinner`), and rendering of responsive success states (`st.success`).
* **Hybrid Processing Logic Layer (Middleware Engine):** The operational core of the application. It consists of a sequential rule-based deterministic mapper combined with a statistical language parsing sub-layer (`TextBlob`).
* **Lexicon Validation Layer (Data Backend):** Powered locally by the Natural Language Toolkit (NLTK) Corpora data dictionary packages. It checks spelling structures against contextual sentence parts (nouns, verbs, prepositions).

### 2. End-to-End Data Flow Pipeline

When a user types a raw message string into the browser window, the data passes sequentially through the following pipeline:

[ Raw User Input String ]
           │
           ▼
┌────────────────────────────────────────┐
│     Step A: Uniform Pre-Processing     │
│  - Strip trailing/leading spaces       │
│  - Convert text entirely to lowercase  │
└────────────────────────────────────────┘
           │
           ▼
┌───────────────────────────────────────────┐
│    Step B: Deterministic Dictionary       │
│  - Scans string against Slang Map         │
│  - Expands abbreviations (clg -> college) │
│  - Preserves token patterns (codng)       │
└───────────────────────────────────────────┘
           │
           ▼
┌────────────────────────────────────────┐
│      Step C: Statistical NLP Parsing   │
│  - Passes cleaned string to TextBlob   │
│  - Computes spelling distance weights  │
│  - Adjusts dynamic phrase structure    │
└────────────────────────────────────────┘
           │
           ▼
┌────────────────────────────────────────┐
│     Step D: Structural Override Map    │
│  - Mitigates over-correction bugs      │
│  - Explicit context fix-up rules       │
│  - Resolves semantic homophone slips   │
└────────────────────────────────────────┘
           │
           ▼
┌───────────────────────────────────────────┐
│      Step E: Grammar Capitalization       │
│  - Capitalizes index[0] of array          │
│  - Normalizes lone objective pronoun 'I'  │
└───────────────────────────────────────────┘
           │
           ▼
[ Displayed Meaningful Output String ]

```

---

## 🎓 Industry Engineering Competencies & Methodology

Building this mini-project provided significant hands-on experience mirroring industry-standard product development lifecycles, debugging workflows, and implementation frameworks.

### 1. Project Workflows (SDLC & CI/CD Fundamentals)

* **Environment Isolation:** Utilized Python virtual environment boundaries (`venv`) to containerize and isolate project dependencies, ensuring the local production ecosystem remained free from global package conflicts.
* **Repository Hygiene & Configuration Management:** Practiced professional version control habits by establishing an explicit codebase blueprint. Successfully maintained a clean production branch by ensuring only source files (`main.py`) and standard manifest tracking files (`requirements.txt`) were compiled, intentionally eliminating OS-specific binary packages (`.exe`) to match universal cloud architecture protocols.
* **Cloud Orchestration Workflow:** Configured standard runtime hooks allowing automated Linux cloud architectures to ingest, unpack, and dynamically construct identical hosting environments globally.

### 2. Strategic Technical Implementation

* **Decoupled System Architecture:** Designed the application following a modular tier strategy (User Interface Layer ➔ Engine Processing Layer ➔ Data Validation Lexicon Backend).
* **Hybrid Multitasking Engine:** Avoided the common pitfall of a single monolithic approach. Instead, a hybrid system was built: combining a deterministic algorithm (for fast slang/shorthand lookup mappings) with a statistical machine learning abstraction model (for contextual spelling edit-distances). This mirrors real-world NLP implementations found in enterprise search engine auto-completion systems.

### 3. Practical Problem-Solving & Triage Approaches

* **System Environment Auditing:** Diagnosed and triaged standard script-execution roadblocks and environment path mismatches (`Error: Invalid value: File does not exist`). Learned to audit the command shell's active working directory pointer relative to physical folder trees to resolve directory target conflicts cleanly.
* **Defensive Edge-Case Programming:** Encountered standard NLP library limitations where statistical probability models mistakenly over-corrected technical domains (e.g., mapping the token `codng` to `coming`). Successfully neutralized algorithmic anomalies by embedding manual override heuristic loops, a strategy commonly used in industry to patch edge cases and manage algorithmic biases.

---

## 📊 Validated Test Matrix

The hybrid framework has been fully validated against diverse and irregular test sentences to verify semantic correctness:

| Raw User Input | Corrected System Output | Target Error Resolved |
| --- | --- | --- |
| `i m net feelng wall` | **I am not feeling well** | Shorthand expansion + Context correction (`net` ➔ `not`, `wall` ➔ `well`) |
| `i m geing te hespitel` | **I am going to the hospital** | Heavy phonetic typo clustering and slang translation |
| `You are late fare college` | **You are late for college** | Homophone confusion resolution (`fare` ➔ `for`) |
| `i m net geing to clg bcz i m leaning codng coursas` | **I am not going to college because I am learning coding courses** | Complex multi-word correction & custom programming word mapping (`codng` ➔ `coding`) |

---

## 📂 Project Directory Structure

```text
Mini Project/
│
├── main.py                  # Primary application file containing core logic & UI
├── requirements.txt         # Production dependency tracking file
└── README.md                # Project documentation file

```

---

## 🛠️ Local Installation & Setup Instructions

To run this project on your local machine, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/Yasasvi2025/AI-Autocorrect-Tool.git
cd AI-Autocorrect-Tool

```

### 2. Install Project Dependencies

```bash
pip install streamlit textblob

```

### 3. Download the NLP Corpora Datasets

```bash
python -m textblob.download_corpora

```

### 4. Launch the Streamlit App

```bash
streamlit run main.py

```

Your local browser window will automatically launch the web interface at `http://localhost:8501`.

---

## ⚙️ Dependencies (`requirements.txt`)

```text
streamlit
textblob

```

---

## 🛠️ Built With

* **Python**
* **Streamlit** - For building the interactive front-end web layout.
* **TextBlob (NLTK)** - For structural English phrase tokenization and spell checking.

```
