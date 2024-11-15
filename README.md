
# 🛡️ **Password Strength Checker**

🎉 Welcome to the **Password Strength Checker** project! This fun and interactive tool helps you assess the strength of your passwords with just a few clicks. 🚀

---

## ✨ **Features** ✨
✔️ **Validate Password Length**: Ensures your password is of sufficient length.  
🔒 **Special Characters Check**: Checks for special characters to enhance security.  
🔁 **Repetition Detector**: Identifies repetitive patterns in your password.  
⚡ **Real-Time Feedback**: Get instant updates on password strength!  

---

## 📂 **File Descriptions** 📂

### 1. `pass_ly.py` 📜
- 💡 **Purpose**: The brain behind the password strength logic.  
- 🛠️ **Key Functions**:  
  - `_acc_len_warn`: Classifies passwords based on length.  
  - `_acc_con`: Checks for special characters.  
  - `_return_check`: Combines all evaluations into one output.

### 2. `passwd.py` 🎨
- 🖌️ **Purpose**: The heart of the graphical interface.  
- 🧑‍💻 **Features**:  
  - Accepts user input.  
  - Displays password strength using `pass_ly.py` logic.  

---

## ▶️ **How to Run** ▶️

1. 🐍 **Install Python**: Make sure Python 3 is installed on your system.  
2. 📦 **Dependencies**: No additional installations needed; Tkinter is built-in.  
3. 📁 **Setup**: Place both `pass_ly.py` and `passwd.py` in the same directory.  
4. 🚀 **Run**: Open a terminal and type:  
   ```bash
   python passwd.py
   ```

---

## 💡 **Usage** 💡

1. 🖥️ Launch the application.  
2. 🔑 Enter your password in the text field.  
3. 🎯 Instantly see how strong your password is!  

---

## 🌟 **Future Enhancements** 🌟
🔢 **Advanced Metrics**: Add entropy and dictionary-based checks.  
💡 **Password Suggestions**: Generate strong passwords for users.  
🎨 **Enhanced GUI**: Improve visuals and add themes.  

---
