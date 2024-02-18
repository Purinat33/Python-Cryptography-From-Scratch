# https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/
# https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_quick_guide.htm
class Caesar:
    def __init__(self) -> None:
        print("Caesar Cipher Initiated")

    # E_n(x)=(x+n)mod 26
    # (Encryption Phase with shift n)
    # foreach letter
    @staticmethod
    def encrypt(plainText: str, shift: int) -> str:
        cipherText = ""
        for letter in plainText:
            # Encrypt UpperCase Letter (ASCII Of A must be subtracted as well)
            if (letter.isupper()):
                cipherText = cipherText + chr(
                    ((ord(letter) - ord('A') + shift) % 26 + ord('A'))
                )
            elif (letter.islower()):
                cipherText = cipherText + chr(
                    ((ord(letter) - ord('a') + shift) % 26 + ord('a'))
                )
            else:
                cipherText += letter

        return cipherText

    # Decrypt same but subtract
    @staticmethod
    def decrypt(cipherText: str, shift: int) -> str:
        plainText = ""
        for letter in cipherText:
            # Encrypt UpperCase Letter (ASCII Of A must be subtracted as well)
            if (letter.isupper()):
                plainText = plainText + chr(
                    ((ord(letter) - ord('A') - shift) % 26 + ord('A'))
                )
            elif (letter.islower()):
                plainText = plainText + chr(
                    ((ord(letter) - ord('a') - shift) % 26 + ord('a'))
                )
            else:
                plainText += letter

        return plainText

    @staticmethod
    def bruteForce(cipherText: str):
        for i in range(0, 26):
            print(
                f"Shift={i} : {Caesar.decrypt(cipherText=cipherText, shift=i)}")
