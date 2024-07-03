Давайте разберем более примитивный пример, используя упрощенную версию шифрования и создания блокчейна. Мы будем использовать основные концепции криптографии и блокчейн-технологий, но в упрощенной форме, чтобы лучше понять процесс.

### Шаг 1: Создание блокчейна

1. **Блокчейн**:
   - Блокчейн — это цепочка блоков, где каждый блок содержит список транзакций.
   - Каждый блок имеет хэш предыдущего блока, что обеспечивает целостность цепочки.

```python
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    timestamp = int(time.time())
    return Block(0, "0", timestamp, "Genesis Block", calculate_hash(0, "0", timestamp, "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    previous_hash = previous_block.hash
    hash = calculate_hash(index, previous_hash, timestamp, data)
    return Block(index, previous_hash, timestamp, data, hash)

Давайте разберем более примитивный пример, используя упрощенную версию шифрования и создания блокчейна. Мы будем использовать основные концепции криптографии и блокчейн-технологий, но в упрощенной форме, чтобы лучше понять процесс.

### Шаг 1: Создание блокчейна

1. **Блокчейн**:
   - Блокчейн — это цепочка блоков, где каждый блок содержит список транзакций.
   - Каждый блок имеет хэш предыдущего блока, что обеспечивает целостность цепочки.

```python
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    timestamp = int(time.time())
    return Block(0, "0", timestamp, "Genesis Block", calculate_hash(0, "0", timestamp, "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    previous_hash = previous_block.hash
    hash = calculate_hash(index, previous_hash, timestamp, data)
    return Block(index, previous_hash, timestamp, data, hash)

# Инициализация блокчейна
blockchain = [create_genesis_block()]
```

### Шаг 2: Генерация кошельков

2. **Кошельки и ключи**:
   - Приватный ключ (private key) — это секретный ключ, известный только владельцу кошелька.
   - Публичный ключ (public key) генерируется из приватного ключа и используется для создания адреса кошелька.
   - Мы используем простой хэш-функции для генерации ключей.

```python
import random

def generate_private_key():
    return ''.join([random.choice('0123456789abcdef') for _ in range(64)])

def generate_public_key(private_key):
    return hashlib.sha256(private_key.encode()).hexdigest()

def generate_address(public_key):
    return hashlib.sha256(public_key.encode()).hexdigest()[:16]

# Создание кошелька
private_key = generate_private_key()
public_key = generate_public_key(private_key)
address = generate_address(public_key)

print("Private Key:", private_key)
print("Public Key:", public_key)
print("Address:", address)
```

### Шаг 3: Взаимодействие кошельков

3. **Создание и отправка транзакций**:
   - Транзакция включает отправителя, получателя и сумму.
   - Приватный ключ отправителя используется для подписи транзакции.
   - Транзакция добавляется в блокчейн.

```python
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

def create_transaction(sender_private_key, sender_address, receiver_address, amount):
    # Создание простой транзакции
    transaction = Transaction(sender_address, receiver_address, amount)
    # Подпись транзакции (в данном случае просто хэш)
    signature = hashlib.sha256((sender_address + receiver_address + str(amount) + sender_private_key).encode()).hexdigest()
    return transaction, signature

# Пример транзакции
receiver_address = generate_address(generate_public_key(generate_private_key()))
transaction, signature = create_transaction(private_key, address, receiver_address, 10)

print("Transaction:")
print("  Sender:", transaction.sender)
print("  Receiver:", transaction.receiver)
print("  Amount:", transaction.amount)
print("  Signature:", signature)

# Добавление транзакции в блокчейн
new_block = create_new_block(blockchain[-1], transaction.__dict__)
blockchain.append(new_block)

print("New Block added:")
print("  Index:", new_block.index)
print("  Previous Hash:", new_block.previous_hash)
print("  Timestamp:", new_block.timestamp)
print("  Data:", new_block.data)
print("  Hash:", new_block.hash)
```

### Заключение

Мы рассмотрели упрощенный пример создания блокчейна, генерации кошельков и взаимодействия между кошельками. Этот пример использует основные концепции, такие как хэширование и цифровые подписи, чтобы показать, как данные защищаются и передаются в блокчейн-системе. В реальных криптовалютах используются гораздо более сложные алгоритмы и протоколы для обеспечения безопасности и масштабируемости.
