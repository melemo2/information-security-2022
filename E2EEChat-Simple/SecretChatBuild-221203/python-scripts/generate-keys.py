from Crypto import Random
from Crypto.PublicKey import RSA
import base64

def encode_base64(p):
    return base64.b64encode(p).decode('ascii')

# 32바이트 (256비트) 랜덤 비밀키 생성
bytes = bytearray(Random.get_random_bytes(32)) # ascii 변환중 에러로 인해 0-128로 clamping
secret = bytearray([byte % 128 for byte in bytes])

# RSA 2048 키 생성 시작 
rsa = RSA.generate(2048) 
# 공개키 export
pubkey = rsa.public_key().exportKey()
# 개인키 export
prikey = rsa.exportKey()

print(encode_base64(secret) + '\n')
print(encode_base64(pubkey) + '\n')
print(encode_base64(prikey) + '\n')