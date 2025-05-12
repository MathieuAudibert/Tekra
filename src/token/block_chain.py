#!/usr/bin/python

import hashlib
import datetime


class BlockChain:
  difficulte = 4

  def __init__(self, chaine=[]):
    self.chaine = chaine

  def add(self, block):
    self.chaine.append(block)

  def remove(self, block):
    self.chaine.remove(block)

  def mine(self, block):
    try:
      block.precedent_hash = self.chaine[-1].hash()
    except IndexError:
      pass

    while True:
      if block.hash()[:4] == "0" * self.difficulte:
        self.add(block)
        break
      else:
        block.nonce += 1

  def isValid(self):
    for i in range(1, len(self.chaine)):
      _precedent = self.chaine[i].precedent_hash
      _actuel = self.chaine[i-1].hash()
      if _precedent != _actuel or _actuel[:self.difficulte] != "0" * self.difficulte:
        return False
    
    return True