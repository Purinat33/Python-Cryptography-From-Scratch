import matplotlib.pyplot as plt
from crypto.Caesar import Caesar
from crypto.FrequencyAnalysis import getFreq
from crypto.SHA import SHA
from crypto.RSA import RSA

# Caesar cipher and freq analysis
inputText = 'Tqxxa Iadxp'
# Caesar.bruteForce(inputText)
getFreq(inputText)
getFreq("Hello World")

# SHA

# RSA
sender = RSA("Sender")
print(sender)
receiver = RSA("Receiver")
print(receiver)

message = "Hello World!"
# Alice send using Bob public information (N, E)
receiver_N = receiver.getPublicKeyPair()[0]
receiver_E = receiver.getPublicKeyPair()[1]

encrypted_message = sender.encryption(message, N=receiver_N, E=receiver_E)
print(f"Sender encrypted message using Receiver's public (N, E): ")
print(f"Ciphertext: {RSA.format_text_to_hex(encrypted_message)}\n")


decrypted_message = receiver.decryption(encrypted_message)
print(f"Receiver decrypted message using Receiver's private (N, D): ")
print(f"Plaintext: {decrypted_message}")

# We need plt.show() at the end of the program and that's it to make draw() work
# plt.show()


def main():
    pass
