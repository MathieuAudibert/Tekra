import src.token.block as tekra_block
import src.token.block_chain as block_chain

blockchain = block_chain.BlockChain()
db = ['hello world', 'caca', 'frappadingue', 'crocodilo bombardillo']

num = 0
for data in db:
  num += 1
  blockchain.mine(tekra_block.Block(data, num))

for block in blockchain.chaine:
  print(block)

print(blockchain.isValid())