# Setup Guide — Python, pip & IDE

## 1. Install Python

### Ubuntu / Debian
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version   # should show 3.8+
```

### Windows
Download from https://www.python.org/downloads/  
**Check "Add Python to PATH"** during install.

### macOS
```bash
brew install python3
```

---

## 2. Verify Installation
```bash
python3 --version
pip3 --version
```

---

## 3. pip — Python Package Manager

```bash
# Install a package
pip3 install requests

# Install from requirements file
pip3 install -r requirements.txt

# List installed packages
pip3 list

# Upgrade a package
pip3 install --upgrade requests

# Uninstall
pip3 uninstall requests

# Show package info
pip3 show requests
```

---

## 4. Virtual Environments (best practice)

Always use a virtual environment per project to avoid dependency conflicts.

```bash
# Create
python3 -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install packages inside venv
pip install flask

# Deactivate
deactivate

# Save dependencies
pip freeze > requirements.txt
```

---

## 5. IDE Setup — VS Code (recommended)

1. Download VS Code: https://code.visualstudio.com/
2. Install the **Python extension** by Microsoft (Ctrl+Shift+X → search "Python")
3. Open your project folder: `File → Open Folder`
4. Select interpreter: `Ctrl+Shift+P → Python: Select Interpreter` → choose your venv

### Useful VS Code shortcuts
| Action | Shortcut |
|--------|----------|
| Run file | `F5` or `Ctrl+F5` |
| Open terminal | `` Ctrl+` `` |
| Format code | `Shift+Alt+F` |
| Go to definition | `F12` |
| IntelliSense | `Ctrl+Space` |

---

## 6. Other IDE Options

| IDE | Best for |
|-----|----------|
| **PyCharm** | Full-featured Python IDE (free Community edition) |
| **Jupyter Notebook** | Data science / interactive code |
| **Thonny** | Beginners — built-in debugger |
| **Spyder** | Scientific computing |

---

## 7. Run Your First Script

```bash
# Create a file
echo 'print("Hello, Python!")' > hello.py

# Run it
python3 hello.py
```

Output:
```
Hello, Python!
```
