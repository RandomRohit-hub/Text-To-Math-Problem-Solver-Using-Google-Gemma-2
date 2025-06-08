
```markdown
# 🧮 Text-to-Math Problem Solver using Google Gemma 2

This project is an AI-powered application that interprets and solves mathematical problems written in natural language. It leverages **Google's Gemma 2 LLM** via the **Groq API** for ultra-fast and intelligent reasoning, paired with **LangChain** for task chaining and execution.

## 🚀 Features

- 🧠 Converts natural language math queries into solvable expressions.
- ⚡ Uses **Google Gemma 2** model via **Groq API** for high-speed inference.
- 🔁 LangChain-powered chains for smart prompt handling and execution.
- 📊 Accurate responses to arithmetic and algebraic queries.
- 🎯 Simple Streamlit interface for easy interaction.

## 📸 Demo

![Demo](demo_screenshot.png)  
*Note: Add your app screenshot or a short GIF here.*

## 🧱 Tech Stack

- **[Streamlit](https://streamlit.io/)** – Frontend Web UI
- **[LangChain](https://www.langchain.com/)** – Prompt orchestration and tools
- **[Groq API](https://console.groq.com/)** – LLM hosting for Google Gemma 2
- **[Python](https://www.python.org/)** – Core logic and app development

## 📂 Project Structure

```

.
├── app.py                     # Main Streamlit app
├── .env                       # Stores GROQ\_API\_KEY
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

````

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/RandomRohit-hub/Text-To-Math-Problem-Solver-Using-Google-Gemma-2.git
cd Text-To-Math-Problem-Solver-Using-Google-Gemma-2
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the App


## ✨ Example Inputs

> **Q:** What is the square root of 144?
> **A:** The square root of 144 is 12.

> **Q:** If a car travels 60 km in 2 hours, what is its speed?
> **A:** Speed = Distance / Time = 60 km / 2 h = 30 km/h

## 🔒 API Usage

This app requires a valid `GROQ_API_KEY` to access the Google Gemma 2 model via Groq’s platform. You can get your API key from [Groq Console](https://console.groq.com/).

## 🙌 Acknowledgements

* [Groq](https://www.groq.com/) – for lightning-fast LLM inference
* [LangChain](https://www.langchain.com/) – for powerful language model chains
* [Streamlit](https://streamlit.io/) – for rapid web app prototyping

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

