from datetime import datetime
import hashlib

class Bloco:

	def __init__(self, indice, hash_anterior, dados):
		self.indice = indice
		self.timestamp = datetime.utcnow().timestamp()
		self.dados = dados
		self.hash_anterior = hash_anterior
		self.valor_pow = 0
		self.hash = self.calcular_hash()

	def print_bloco(self):
		print("Índice:", self.indice)
		print("Timestamp:", self.timestamp)
		print("Dados:", self.dados)
		print("Hash anterior:", self.hash_anterior)
		print("Hash:", self.hash)
		print("Valor pow:", self.valor_pow)

	def calcular_hash(self):
		hash_calculado = []
		while (hash_calculado[:4] != "aaaa"):
			dados_hash = (str(self.indice) + str(self.timestamp) + str(self.dados) + str(self.hash_anterior) + str(self.valor_pow))
			hash_calculado = hashlib.sha256(dados_hash.encode("UTF-8")).hexdigest()
			self.valor_pow += 1
		return (hash_calculado)

class Blockchain:
	
	blocos = []

	def __init__(self):
		self.criar_bloco_genesis()

	def criar_bloco_genesis(self):
		genesis = Bloco(0, 0, "Gênesis")
		self.blocos.append(genesis)

	def print_blocos(self):
		for bloco in self.blocos:
			bloco.print_bloco()
			print()

	def add_bloco(self, bloco):
		if(self.bloco_valido(bloco)):
			self.blocos.append(bloco)

	def bloco_valido(self, bloco):
		for bl in self.blocos: 
			if bl.indice == bloco.indice:
				return False
		if bloco.hash[:4] != "aaaa":
			return False
		return True

	def get_ultimo_hash(self):
		return self.blocos[-1].hash

	def get_ultimo_indice(self):
		return self.blocos[-1].indice


my_blockchain = Blockchain()

bloco1 = Bloco(my_blockchain.get_ultimo_indice()+1, my_blockchain.get_ultimo_hash(), {"nome": "Roger", "apelido": "Mr.R"});
my_blockchain.add_bloco(bloco1)
bloco2 = Bloco(my_blockchain.get_ultimo_indice()+1, my_blockchain.get_ultimo_hash(), {"nome": "Lúcia", "apelido": "LadyLucy"});
my_blockchain.add_bloco(bloco2)
bloco3 = Bloco(my_blockchain.get_ultimo_indice()+1, my_blockchain.get_ultimo_hash(), {"nome": "Carlos", "apelido": "ElCarlito"});
my_blockchain.add_bloco(bloco3)
bloco4 = Bloco(my_blockchain.get_ultimo_indice()+1, my_blockchain.get_ultimo_hash(), {"nome": "Roger", "apelido": "Moscou"});
my_blockchain.add_bloco(bloco4)

my_blockchain.print_blocos()