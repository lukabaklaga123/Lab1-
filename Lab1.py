def caesar_decrypt(ciphertext, shift):


    decrypted_text = ""
    for char in ciphertext:
        if 'a' <= char <= 'z':
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            decrypted_text += shifted_char
        elif 'A' <= char <= 'Z':
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

ciphertext_part1 = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."

print("--- Brute-forcing Part 1 Ciphertext ---")
for i in range(26):
    decrypted = caesar_decrypt(ciphertext_part1, i)
    print(f"Shift +{i:2d}: {decrypted}")

print("\n✅ გაშიფრული არის (Shift +12):")
print(caesar_decrypt(ciphertext_part1, 12))


# Part 2


import base64

def caesar_decrypt(ciphertext, shift):
    """Decrypt Caesar cipher with given shift"""
    result = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def brute_force_caesar(ciphertext):
    """Brute force all 26 possible Caesar shifts"""
    return [(shift, caesar_decrypt(ciphertext, shift)) for shift in range(26)]

def repeating_key_xor(data, key):
    """XOR decrypt data with repeating key"""
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

def main():
    cipher = "mznxpz"
    print(f"Ciphertext: {cipher}\n")
    
    candidates = brute_force_caesar(cipher)
    for shift, plaintext in candidates:
        print(f"Shift {shift:2d}: {plaintext}")
    
    print("\n" + "="*50)
    for shift, plaintext in candidates:
        if plaintext == "rescue":
            print(f"✓ Shift {shift} gives 'rescue'")
            break
    
    print("Anagram of 'rescue' -> 'secure'")
    print("="*50)
    
    # Step 3: XOR Decryption
    b64_ct = "Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ="
    ct_bytes = base64.b64decode(b64_ct)
    passphrase = "secure"
    
    pt_bytes = repeating_key_xor(ct_bytes, passphrase.encode('ascii'))
    
    print(f"\nPassphrase: {passphrase}")
    print(f"Decrypted: {pt_bytes.decode('utf-8')}")

if __name__ == "__main__":
    main()