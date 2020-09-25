from functools import reduce
import hashlib
import json
# Initializing our (empty) blockchain list
MINING_REWARD = 20

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Roger'
participants = {'Roger'}


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1: return None
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_sent = reduce(lambda tx_sum, tx_value: tx_sum + (sum(tx_value) if len(tx_value) > 0 else 0), tx_sender, 0)
    amount_received = reduce(lambda tx_sum, tx_value: tx_sum + (sum(tx_value) if len(tx_value) > 0 else 0), tx_recipient, 0)
    
    return amount_received - amount_sent


def verify_transaction(transaction):
     sender_balance = get_balance(transaction['sender'])
     return sender_balance >= transaction['amount']


def add_transaction(sender, recipient, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :sender: The sender of the coins.
        :recipient: The receiver of the coins.
        :amount: The amount of coins sent in the transaction
    """
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}

    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False

def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[0:2] == '00'


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while valid_proof(open_transactions, last_hash, proof):
        proof += 1


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    tx_recipient = input("Nombre del receptor: ")
    tx_amount = float(input("Monto a enviar: "))
    return (tx_recipient, tx_amount)


def hash_block(block):
    return hashlib.sha256(json.dumps(block).encode()).hexdigest()


def reward_mining():
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    return copied_transactions


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    print(hashed_block)
    copied_transactions = reward_mining()
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transactions
    }
    blockchain.append(block)
    return True

def get_user_choice():
    # Get the user input, transform it from a string to a float and store it in user_input
    return input('Opción escogida: ')


def print_blockchain_els():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)


def verify_blockchain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        else:
            if block['previous_hash'] != hash_block(blockchain[index - 1]):
                return False
    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True

while waiting_for_input:
    print("Por favor escoje una opción")
    print("1: Hacer una nueva transacción")
    print("2: Minar bloques")
    print("3: Ver los bloques de la blockchain")
    print("4: Ver participantes")
    print("5: Verificar transacciones")
    print("h: manipular blockchain")
    print("q: Cerrar transacciones y blockchain")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_value()
        tx_recipient, tx_amount = tx_data
        if add_transaction(owner, tx_recipient, tx_amount):
            print("Transacción exitosa!")
        else:
            print("No dispones de saldo suficiente, mina un poco!")
    elif user_choice == "2": 
        if mine_block():
            open_transactions = []
    elif user_choice == "3": 
        print_blockchain_els()
    elif user_choice == "4":
        print(participants)
    elif user_choice == "5":
        if verify_transactions():
            print("Transacciones válidas!")
        else:
            print("Hay transacciones inválidas!")
    elif user_choice == "h":
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("Opción inválida! por favor, elecciona una opción de la lista!")

    balance = get_balance(owner)
    print(f'El balance de {owner} es: {balance:^5.2f}')
    
    if not verify_blockchain():
        print('Error en la blockchain!')
        break
    
    

print('Done!')