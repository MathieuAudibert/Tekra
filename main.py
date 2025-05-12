import src.token.block as tekra_block
import src.token.block_chain as block_chain
import json

blockchain = block_chain.BlockChain()
file_path = "./src/transactions/template.json"

blocks = []
with open(file_path, 'r') as file:
  data = json.load(file)
  transactions_data = data['transactions']
  for idx, transaction in enumerate(transactions_data):
    block_transa = tekra_block.Block(transaction, idx)
    blocks.append(block_transa)

for block in blocks:
  blockchain.mine(block)

for block in blockchain.chaine:
  print(block)

print(blockchain.isValid())
