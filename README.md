# Lab1-Applied Cryptography

## Part 1: Caesar Cipher Decryption (2pts)

### Challenge
Decrypt the ciphertext `"Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."` and analyze the security vulnerabilities of the Caesar cipher.

### Solution Process
- Brute-force attack testing all 25 possible alphabet shifts
- Identify correct key by finding readable English text
- Shift of 12 produces: `"The Quick Brown Fox Jumps Over The Lazy Dog."`

### Security Discussion

**Why Caesar Cipher is Insecure:**
- Extremely small key space (only 25 possible keys) makes brute-force trivial
- Vulnerable to frequency analysis as letter patterns remain unchanged
- No protection against modern cryptanalysis techniques

**Legacy Usage:**
- Found in outdated systems and educational contexts
- ROT13 (shift 13) still used for simple text obfuscation in forums
- Sometimes appears in embedded systems with minimal security requirements
- Not suitable for any real security applications

### Implementation
Python script automates brute-force attack by testing each shift value.

See `Lab1.py` for full code.









## Part 2: XOR Encryption/Decryption (3pts)

### Challenge
Decrypt a multi-layered cryptographic puzzle combining Caesar cipher, anagram solving, and XOR decryption.

### Solution Process
- Brute force Caesar cipher on `mznxpz` reveals `rescue` at shift 5
- Rearrange `rescue` to get the passphrase: `secure`
- Decode base64 ciphertext `Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ=`
- Apply repeating-key XOR decryption using `secure` as the key
- Result: decrypted message

### Implementation
The solution uses Caesar brute force attack, anagram solving, base64 decoding, and XOR cipher with repeating key pattern.

See uploaded `Lab1.py` for full code.
