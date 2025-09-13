# Project Setup

Follow these steps to set up the project locally after cloning.

## 1. Clone the repository
```bash
git clone <repo-url>
cd <repo-directory>
```

## 2. Create a virtual environment
It is recommended to use a virtual environment to isolate project dependencies.

```bash
python -m venv .venv
```

## 3. Activate the virtual environment
- **Linux/macOS**
  ```bash
  source .venv/bin/activate
  ```
- **Windows (PowerShell)**
  ```bash
  .venv\Scripts\Activate.ps1
  ```

## 4. Install dependencies
All required Python packages are listed in `requirements.txt`.

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Start development
Make sure the virtual environment is activated whenever you work on this project.

## 6. Updating dependencies
If you add new packages during development, update `requirements.txt` so others can install them:

```bash
pip freeze > requirements.txt
```

Commit the updated `requirements.txt` file to the repository.
