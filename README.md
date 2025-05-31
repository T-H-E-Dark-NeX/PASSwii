![](a.gif)
<JUST LIKE THE CAT IS MUNCHING , DATA BROKERS AND HACKERS ARE MUNCHING ON YOUR LEAKED PASSWORDS>

Enter PASSwii




🚀 Features

- **Breach Detection**: Check passwords against the HaveIBeenPwned database using secure k-anonymity
- **Quantum-Resistant Generation**: Generate secure passwords using post-quantum cryptographic techniques (KKDF)
- **Privacy-First**: Your passwords are never sent in full to any server - only the first 5 characters of the SHA-1 hash
- **Multiple Lengths**: Get password suggestions in various lengths (original length + 16, 24, 32 characters)
- **Batch Processing**: Check multiple passwords at once

## 🔧 Installation

### Prerequisites
- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended)

### Using uv (recommended)
```bash
git clone https://github.com/T-H-E-Dark-NeX/PASSwii.git
cd passwii
uv sync
```

### Using pip
```bash
git clone https://github.com/T-H-E-Dark-NeX/PASSwii.git
cd passwii
pip install -e .
```

## 📖 Usage

### Command Line
```bash
# Check a single password
python main.py <your_password_here>

# Check multiple passwords
python main.py "password1" "password2" "password3"
```

### Example Output

#### Safe Password:
```
good News ! your pass MySecureP@ssw0rd is safe for now 
you may consider updating : MySecureP@ssw0rd with one of the post quantum passwords for maximum safety
Length 16: K9mX#7vBnQ2$pLz8
Length 16: A8nY&4wCmR1!qMx9
Length 24: P3rT@9sBkL6#uVx2N8mY&4wC
Length 32: Q7nM!5vBpK9@sWx3R2mY&8uCqL6#
the longer the pass you set , the better
```

#### Breached Password:
```
YOUR PASS : password123 HAS BEEN BREACHED 2670741 TIMES !
YOU MUST UPDATE password123 WITH ONE OF THE FOLLOWING :
Length 11: X9mK#5vBpL2
Length 16: A8nY&4wCmR1!qMx9
Length 24: P3rT@9sBkL6#uVx2N8mY&4wC
Length 32: Q7nM!5vBpK9@sWx3R2mY&8uCqL6#
the longer the pass you set , the better
```



### Password Generation
- **Post-Quantum Security**: Uses KKDF (Kyber Key Derivation Function) from the `quantcrypt` library
- **Cryptographically Secure**: Built on `secrets` module for true randomness
- **Customizable**: Generates passwords of various lengths based on your needs
- **Character Variety**: Includes lowercase, uppercase, numbers, and special characters



## 🔐 Security Features

- **No Network Exposure**: Full passwords never leave your machine
- **K-Anonymity Protocol**: Uses the industry-standard approach for secure breach checking
- **Post-Quantum Ready**: Generated passwords use quantum-resistant cryptographic techniques
- **Memory Safe**: Passwords are handled securely in memory

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch 
3. Commit your changes 
4. Push to the branch 
5. Open a Pull Request


## 🙏 Acknowledgments

- [HaveIBeenPwned](https://haveibeenpwned.com/) for providing the breach detection API
- [quantcrypt](https://github.com/quantcrypt/quantcrypt) for post-quantum cryptographic functions
- The "wii wii cat" meme for the inspiration and name 🐱

## ⚠️ Disclaimer

While passwii uses secure methods to check password breaches and generate strong passwords, no tool can guarantee 100% security. Always follow good password hygiene practices:

- Use unique passwords for each account
- Enable two-factor authentication where possible
- Regularly update passwords for sensitive accounts
- Store passwords in a reputable password manager

---

Made with ❤️ and quantum-resistant randomness
