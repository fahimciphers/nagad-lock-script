
# 🔒 Nagad Lock Script

A Python-based script designed for simulating account locking actions on Nagad accounts. This script demonstrates how HTTP request manipulations work and is intended **only for educational purposes**.

---

## ⚠️ Disclaimer
This script is developed strictly for **educational and ethical purposes**. Unauthorized use or malicious activities using this tool are **strictly prohibited**. Please act responsibly.

---

## ✨ Features
- Automates repeated login failures to simulate account locking.
- Interactive **Rich terminal interface**.
- Works seamlessly on **Termux**, **Linux**, and **Ubuntu**.
- Lightweight and straightforward to set up.

---

## 🔧 Requirements
- Python 3.x
- **Required Python Libraries**:
  - `requests`
  - `rich`
- Internet connection

---

## 📥 Installation and Usage

### 📱 For Termux
1. **Install Termux**: [Download Termux](https://termux.com/)
2. **Update Termux packages**:
   ```bash
   pkg update && pkg upgrade -y
   ```
3. **Install Python and Git**:
   ```bash
   pkg install python git -y
   ```
4. **Clone the repository**:
   ```bash
   git clone https://github.com/fahimciphers/nagad-lock-script.git
   cd nagad-lock-script
   ```
5. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
6. **Run the script**:
   ```bash
   python muntasir.py
   ```

---

### 💻 For Linux/Ubuntu
1. **Update your system**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```
2. **Install Python and Git**:
   ```bash
   sudo apt install python3 python3-pip git -y
   ```
3. **Clone the repository**:
   ```bash
   git clone https://github.com/fahimciphers/nagad-lock-script.git
   cd nagad-lock-script
   ```
4. **Install required Python libraries**:
   ```bash
   pip3 install -r requirements.txt
   ```
5. **Run the script**:
   ```bash
   python3 muntasir.py
   ```

---

## 🎯 Usage Example
When you run the script, it will prompt for the **target phone number** and attempt to lock the associated account. Here's how the script behaves:

1. Enter the target phone number.
2. The script will simulate multiple failed login attempts.
3. It will display whether the account was successfully locked or not.

---

## 🛠 Troubleshooting
If you encounter issues, ensure the following:
- Python is installed and up-to-date.
- Required libraries (`requests`, `rich`) are installed.
- You have a stable internet connection.

---

## 🌟 Contribution
Contributions are welcome! To contribute:
1. Fork the repository.
2. Make your changes.
3. Submit a pull request.

---

## 📜 License
This project is licensed under the **MIT License**. You are free to use and modify this project, but remember to give credit to the original author.

---

## ❤️ Acknowledgments
Special thanks to the contributors and testers who made this project possible!

---

### 🖇 Commands Summary Table

| Platform        | Commands                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------|
| **Termux**      | `pkg update && pkg upgrade -y && pkg install python git -y && git clone <repo> && cd <repo>`      |
| **Linux/Ubuntu**| `sudo apt update && sudo apt install python3 python3-pip git -y && git clone <repo> && cd <repo>` |

---

**Enjoy using the Nagad Lock Script responsibly!**
```

