# 📦 Muscle-AI Project

This repository contains the code for **Muscle-AI**, a project that uses
**Node.js, TypeScript**, and integration with **AI (OpenAI/DeepSeek)**.\
The dependency environment is managed with **Poetry** to ensure
reproducibility and standardization.

------------------------------------------------------------------------

## ⚙️ Requirements

Before starting, make sure you have the following tools installed:

-   [Python 3.10+](https://www.python.org/downloads/)
-   [Poetry](https://python-poetry.org/docs/#installation)
-   [Node.js 18+](https://nodejs.org/en)

------------------------------------------------------------------------

## 📥 Installing Poetry

### Linux / macOS

``` bash
curl -sSL https://install.python-poetry.org | python3 -
```

Add Poetry to PATH (if needed):

``` bash
export PATH="$HOME/.local/bin:$PATH"
```

### Windows (PowerShell)

``` powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

If the `poetry` command is not recognized, manually add it to PATH:

    C:\Users\<YOUR_USERNAME>\AppData\Roaming\Python\Scripts

------------------------------------------------------------------------

## 🚀 Running the project

Clone the repository:

``` bash
git clone https://github.com/your-username/muscle-ai.git
cd muscle-ai
```

Install dependencies:

``` bash
poetry install
```

Activate the virtual environment:

``` bash
poetry shell
```

------------------------------------------------------------------------

## 🧪 Running scripts

Run tests:

``` bash
poetry run pytest
```

Run application (example):

``` bash
poetry run python src/muscle_ai/main.py
```

------------------------------------------------------------------------

## 📚 Documentation

-   [Poetry Documentation](https://python-poetry.org/docs/)
-   [Node.js Guide](https://nodejs.org/en/docs/)
-   [OpenAI API](https://platform.openai.com/docs/)

------------------------------------------------------------------------

## 🤝 Contributing

1.  Fork this project
2.  Create a feature branch (`git checkout -b feature/new-feature`)
3.  Commit your changes (`git commit -m 'feat: new feature'`)
4.  Push to the branch (`git push origin feature/new-feature`)
5.  Open a Pull Request

------------------------------------------------------------------------

## 📄 License

This project is licensed under the **MIT License**. See the
[LICENSE](LICENSE) file for more information.