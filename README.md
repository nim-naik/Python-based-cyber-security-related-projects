## 🔐 Password cracker techniques.

** Password cracker techniques.** is a collection of Python scripts designed to demonstrate common password recovery and security testing techniques. This project provides practical examples of **Brute-Force simulation** and **Dictionary-Based hash cracking** to highlight the importance of strong credential management.

---

### 🔧 Key Features

*   **Randomized Brute-Force**: Simulates a basic brute-force attack by continuously generating random character strings until a match is found[cite: 3].
*   **Dictionary Attack Engine**: Compares a target MD5 hash against a list of common passwords to identify a match[cite: 4].
*   **Hash Verification**: Utilizes the `hashlib` library to convert plain-text entries into **MD5 digests** for secure comparison[cite: 4].
*   **Interactive Input**: Features a GUI-based password entry prompt using `pyautogui` for a user-friendly simulation[cite: 3].
*   **Automated Matching**: Automatically detects password length and character sets to attempt recovery[cite: 3].
*   **Success Logging**: Provides real-time console feedback during the cracking process and confirms the exact password once recovered[cite: 3, 4].

---

### 💻 Project Structure

| File | Description |
| :--- | :--- |
| `brute_force.py` | Script using `random` and `pyautogui` to simulate character-by-character guessing[cite: 3]. |
| `hash_cracker.py` | A script that attempts to crack MD5 hashes using a dictionary file[cite: 4]. |
| `passwords.txt` | A sample dictionary file containing a list of potential passwords for testing[cite: 5]. |

---

### 🚀 Getting Started

#### 1. Installation
1.  **Dependencies**: Install the required libraries via pip:
    ```bash
    pip install pyautogui
    ```
2.  **Files**: Ensure `passwords.txt` is in the same directory as `hash_cracker.py` or provide the full file path when prompted[cite: 4, 5].

#### 2. Running the Tools
*   **For Brute-Force**: Run `python brute_force.py`. A pop-up will ask for a password; the script will then randomly guess until it finds it[cite: 3].
*   **For Hash Cracking**: Run `python hash_cracker.py`. Enter the MD5 hash you wish to crack and point the script to your `passwords.txt` file[cite: 4].

---

### 📘 Core Logic

| Process | Method | Description |
| :--- | :--- | :--- |
| **Random Guessing** | `random.choices` | Picks random characters from a predefined set until they match the target[cite: 3]. |
| **Encoding** | `.encode('utf-8')` | Converts string-based passwords into byte format for hashing[cite: 4]. |
| **Hashing** | `hashlib.md5()` | Generates a 128-bit hash value from dictionary entries[cite: 4]. |
| **Comparison** | `.hexdigest()` | Converts the hash to a readable string to check against user input[cite: 4]. |

---

### ⚠️ Important Notes
*   **Educational Use Only**: These scripts are intended for learning and authorized security testing purposes only.
*   **Efficiency**: The brute-force script uses random selection, which is mathematically inefficient compared to sequential permutation[cite: 3].
*   **Algorithm**: The hash cracker currently supports **MD5**, which is considered cryptographically broken and should not be used for modern security[cite: 4].

---

### 🔮 Future Roadmap
*   **Multiprocessing**: Implement Python's `multiprocessing` module to run multiple brute-force attempts simultaneously, significantly reducing cracking time.

*   **Support for SHA-256**: Update the hash cracker to support more secure algorithms like SHA-256 to reflect modern security standards.

*   **Sequential Brute-Force**: Replace the random generator with an iterative approach (using `itertools`) to ensure all possible combinations are tested systematically.

*   **Salting Simulation**: Add a feature to demonstrate how "salting" passwords makes dictionary attacks significantly harder to execute.
```
