# ---------- WARRIORS BATTLE ----------

import random
import math

# 剑客
class Warriors:

	def __init__(self, name, Kungfu, attkMax, defendMax):
		self.name = name
		self.energyValue = Kungfu
		self.attkMax = attkMax
		self.defendMax = defendMax

	# 攻击力
	def attack(self):
		return self.attkMax * (random.random() + .5)

	# 防守力
	def defend(self):
		return self.defendMax * (random.random() + .5)

# 比武
class Battles:

	def launchAtack(self, warrior1, warrior2):

		while True:

			if self.fight(warrior1, warrior2) == 'Game over':
				print('Game over')
				break
			if self.fight(warrior2, warrior1) == 'Game over':
				print('Game over')
				break

	@staticmethod
	def fight(warriorA, warriorB):

		attkAmount = warriorA.attack()
		defendAmount = warriorB.defend()

		damage2warriorB = math.ceil(attkAmount - defendAmount)
		warriorB.energyValue = warriorB.energyValue - damage2warriorB

		print('\n{}进攻, {}防守\n这次过招的伤害值{}\n{}的战斗力下降到{}\n'.format(
		warriorA.name, warriorB.name, damage2warriorB, warriorB.name, warriorB.energyValue))

		if warriorB.energyValue <= 0:
			return 'Game over'
		else:
			return 'Continue fight'

blowSnow = Warriors('西门吹雪', 50, 20, 10)
loneCity = Warriors('叶孤城', 50, 20, 10)

forbidenCity = Battles()
forbidenCity.launchAtack(blowSnow, loneCity)