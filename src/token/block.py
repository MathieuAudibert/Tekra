import hashlib


def updatehash(*args):
  texte = ""
  h = hashlib.sha256()
  for arg in args:
    texte += str(arg)
  h.update(texte.encode('utf-8'))
  return h.hexdigest()


class Block:

  def __init__(self, transactions, nombre=0):
    self.transactions = transactions
    self.nombre = nombre
    self.precedent_hash = "0" * 64
    self.nonce = 0

  def hash(self):
    return updatehash(self.precedent_hash, self.nombre, self.transactions,
                      self.nonce)

  def __str__(self):
    return "Block#: %s\nHash: %s\nPrecedent: %s\nNonce: %s\nTransactions: %s\n" % (
        self.nombre, self.hash(), self.precedent_hash, self.nonce,
        self.transactions)
