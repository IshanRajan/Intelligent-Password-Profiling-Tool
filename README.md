# Intelligent Password Profiling Tool

A Python-based educational tool that demonstrates how personal information can be used to generate predictable usernames and passwords, highlighting the importance of strong, unique credentials that don't rely on easily guessable personal data.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ⚠️ Ethical Use Statement

This tool is designed **strictly for educational purposes** to demonstrate password security vulnerabilities. It should only be used:

- With your own personal information
- With explicit consent from individuals whose data you're analyzing
- For security awareness training and education
- To demonstrate the risks of predictable password patterns

**DO NOT use this tool for:**
- Unauthorized access attempts
- Credential stuffing attacks
- Any malicious or illegal activities

## 🎯 Purpose

This tool helps security professionals, educators, and individuals understand:

- How attackers can exploit personal information to guess credentials
- Common patterns people use when creating passwords
- Why passwords based on personal data are inherently weak
- The importance of using password managers and truly random passwords

## ✨ Features

- **Username Generation**: Creates common username patterns from personal data (first name, last name, nicknames, birth year, hobbies, company)
- **Username Variations**: Expands base usernames with realistic variations (separators, capitalization, prefixes, numeric suffixes)
- **Password Generation**: Generates typical password patterns people create using personal information
- **Password Strength Analysis**: Categorizes passwords into weak, medium, strong, and very strong based on:
    - Length
    - Character diversity (uppercase, lowercase, numbers, special characters)
    - Presence of personal information
    - Common weak patterns
- **Multiple Input Formats**: Supports interactive CLI, CSV, JSON, and TXT file inputs
- **Multiple Output Formats**: Generate reports in CLI, JSON, CSV, or TXT formats
- **Comprehensive Error Handling**: Validates inputs and provides helpful error messages
- **Batch Processing**: Analyze multiple profiles at once

## 📋 Requirements

- Python 3.8 or higher
- pip(Python package installer)

### Python Dependencies
```
pandas>=1.3.0
```

## 🚀 Installation
1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/Intelligent-Password-Profiling-Tool.git
cd Intelligent-Password-Profiling-Tool
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Verify installation:**
```bash
python main.py --help

Intelligent-Password-Profiling-Tool/
├── main.py                          # Main entry point
├── input/
│   ├── __init__.py
│   └── cli_input.py                 # Interactive user input handling
├── generator/
│   ├── __init__.py
│   ├── username_generator.py       # Username generation logic
│   └── password_generator.py       # Password generation logic
├── analzyer/
│   ├── __init__.py
│   └── profile_analyzer.py         # Password strength analysis
├── data/
│   ├── __init__.py
│   └── data_loader.py              # CSV/JSON/TXT file loaders
├── reporter/
│   ├── __init__.py
│   └── report_generator.py         # Report generation (all formats)
├── reports/                         # Generated reports (auto-created)
├── tests/
│   └── test_suite.py               # Comprehensive test suite
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## 💻 Usage

### Interactive Mode

Run the tool in interactive mode to manually enter profile information:
```bash
python main.py
```

You'll be prompted to:
1. Provide consent for ethical use
2. Enter personal information (first name, last name, nickname, birth year, hobby, company)
3. Add multiple profiles if desired
4. View results in the terminal

### File Input Mode

Process profiles from a file (CSV, JSON, or TXT):
```bash
# CSV input
python main.py -i profiles.csv -o json

# JSON input
python main.py -i profiles.json -o csv

# TXT input
python main.py -i profiles.txt -o txt
```

### Command-Line Options
```bash
python main.py [OPTIONS]

Options:
  -i, --input PATH          Path to input file (CSV, JSON, or TXT)
  -o, --output-format TYPE  Output format: cli, json, csv, txt (default: cli)
  -h, --help               Show help message
```

## 📝 Input File Formats

### CSV Format
```csv
first,last,nick,year,hobby,company
John,Doe,JD,1990,gaming,TechCorp
Jane,Smith,Janey,1985,reading,BookC
```

### JSON Format
```json
[
  {
    "first": "John",
    "last": "Doe",
    "nick": "JD",
    "year": "1990",
    "hobby": "gaming",
    "company": "TechCorp"
  },
  {
    "first": "Jane",
    "last": "Smith",
    "nick": "Janey",
    "year": "1985",
    "hobby": "reading",
    "company": "BookCo"
  }
]
```

### TXT Format

Space-separated values (one profile per line):
```
John Doe JD 1990 gaming TechCorp
Jane Smith Janey 1985 reading BookCo
```

**Note:** Use `null` for any fields you want to skip:
```
John Doe null 1990 null TechCorp
```

## 📊 Output Examples

### CLI Output
```
==================================================
Intelligent Password Profiling Tool
Ethical Demonstration Report
==================================================

Summary
--------------------------------------------------
Profiles processed: 1
Total usernames: 15
Total variations: 15
Total passwords: 25

--------------------------------------------------
Profile 1
Name: John Doe
Nickname: JD
Year: 1990
Hobby: gaming
--------------------------------------------------

Base Usernames (15)
  • johndoe
  • jdoe
  • jd
  • john1990
  ...

Username Variations (15)
  • john_doe
  • JohnDoe
  • john-doe
  ...

Password Candidates (25)
  • john123
  • Doe1990
  • jd!
  ...

Password Analysis
--------------------------------------------------
  🔴 Weak (25)
    • john123
    • Doe1990
    • jd!
    ...
```

### JSON Output

Saved to `reports/people_expanded.json`:
```json
[
  {
    "profile": {
      "first": "john",
      "last": "doe",
      ...
    },
    "usernames": ["johndoe", "jdoe", ...],
    "username_variations": ["john_doe", "JohnDoe", ...],
    "passwords": ["john123", "Doe1990", ...],
    "weak_passwords": [...],
    "medium_passwords": [],
    "strong_passwords": [],
    "very_strong_passwords": []
  }
]
```

### CSV Output

Saved to `reports/people_expanded.csv` with columns:
- `first`, `last`, `nick`, `year`, `hobby`, `company`
- `type` (username, username_variation, or password)
- `value` (the actual username/password)

## 🧪 Running Tests

The project includes a comprehensive test suite with 26 tests covering:

- Username generation
- Username variations
- Password generation
- Password analysis
- Data loading (CSV/JSON/TXT)
- Report generation
- Full workflow integration

**Run all tests:**
```bash
python tests/test_suite.py
```

**Expected output:**
```
======================================================================
TEST SUMMARY
======================================================================
Tests run: 26
Successes: 26
Failures: 0
Errors: 0
======================================================================
```

## 🔒 Password Strength Scoring

The tool categorizes passwords based on the following criteria:

### Automatic Weak Classification
Passwords are automatically marked as **weak** if they contain:
- Any personal information (first name, last name, nickname, birth year, hobby, company)
- Any generated username or variation

### Scoring System (for non-personal passwords)

Points are awarded for:
- **Length**: 
  - 0 points: < 8 characters
  - 1 point: 8-12 characters
  - 2 points: > 12 characters
- **Uppercase letters**: 
  - 2 points: mixed case
  - 1 point: all uppercase
  - 0 points: no uppercase
- **Numbers**: 
  - 2 points: contains some digits
  - 0 points: all digits or no digits
- **Special characters**: 
  - 2 points: contains special characters
  - 0 points: no special characters

Penalties:
- -1 point for common patterns: `12345`, `aaaaa`, `abcd`

### Categories
- **Weak**: Score ≤ 2
- **Medium**: Score 3-5
- **Strong**: Score 6-8
- **Very Strong**: Score > 8

## 🛠️ Advanced Configuration

### Disable Python Bytecode Cache

To prevent `__pycache__` directories from being created:

**Linux/Mac:**
```bash
export PYTHONDONTWRITEBYTECODE=1
python main.py
```

**Windows (Command Prompt):**
```cmd
set PYTHONDONTWRITEBYTECODE=1
python main.py
```

**Windows (PowerShell):**
```powershell
$env:PYTHONDONTWRITEBYTECODE = "1"
python main.py
```

### Clean Cache Files
```bash
# Remove all __pycache__ directories
find . -type d -name "__pycache__" -exec rm -rf {} +

# Windows PowerShell
Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force
```

## 🐛 Troubleshooting

### Import Errors

**Problem:** `ModuleNotFoundError: No module named 'generator'`

**Solution:** Ensure you're running from the project root directory and each folder has an `__init__.py` file:
```bash
touch generator/__init__.py
touch analzyer/__init__.py
touch data/__init__.py
touch reporter/__init__.py
touch input/__init__.py
```

### Permission Errors

**Problem:** `ERROR: Permission denied when writing to reports/`

**Solution:** Ensure the `reports/` directory has write permissions:
```bash
chmod 755 reports/  # Linux/Mac
```

### Stale Cache Issues

**Problem:** Changes to code aren't reflected when running

**Solution:** Delete `__pycache__` directories and `.pyc` files:
```bash
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -name "*.pyc" -delete
```

## 📚 Educational Use Cases

1. **Security Awareness Training**: Demonstrate to employees why company policies prohibit personal information in passwords

2. **Penetration Testing Education**: Show security students how attackers might use OSINT to guess credentials

3. **Password Policy Development**: Generate test cases to validate password strength requirements

4. **Personal Security Audit**: Analyze your own passwords to identify weak patterns

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚖️ Legal Disclaimer

This tool is provided for educational and research purposes only. The authors and contributors are not responsible for any misuse or damage caused by this tool. Users must ensure they have proper authorization before analyzing any personal information and must comply with all applicable laws and regulations.

## 👨‍💻 Author

**Ishan Rajan**
- GitHub: [@IshanRajan28](https://github.com/IshanRajan28)
- Email: irajan@terpmail.umd.edu

## 🙏 Acknowledgments

- Built using Python and pandas
- Inspired by common password security research
- Thanks to the cybersecurity community for raising awareness about password vulnerabilities
- Assisted by ChatGPT and Claude

## 📈 Future Enhancements

Potential features for future versions:

- [ ] GUI interface for easier use
- [ ] Integration with Have I Been Pwned API
- [ ] Password entropy calculation
- [ ] Dictionary attack simulation
- [ ] Export to Excel format
- [ ] Password strength visualization charts
- [ ] Custom pattern definitions
- [ ] Multi-language support

---
**Remember:** The best password is one that's long, random, unique, and stored in a password manager. Never use personal information in your passwords!