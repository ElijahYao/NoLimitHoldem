import sys, random 


class FlopFactory(object):
	

	def __init__(self):

		self.cards = ['2', '3', '4', '5' ,'6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
		pass

	def generate_all_flops(self):

		n = len(self.cards)
		flop_texture = []
		for i in range(n - 1, -1, -1):
			for j in range(i, -1, -1):
				for k in range(j, -1, -1):
					for l in range(5):
						if self.is_valid(i, j, k, l):
							flop_texture.append(self.make_flop(i, j, k, l))

	def is_valid(self, high_card, mid_card, low_card, flop_type):
 
		if flop_type == 0:  # rainbow board 
			return True
 
		if flop_type == 4:	# monotonous board
			if high_card == mid_card or mid_card == low_card:
				return False
			return True

		if flop_type == 1:  # high suit = mid suit 
			if high_card == mid_card:
				return False
			return True

		if flop_type == 2:
			if high_card == low_card:
				return False
			return True

		if flop_type == 3:
			if mid_card == low_card:
				return False
			return True

		return False

	def make_flop(self, high_card, mid_card, low_card, flop_type):

		if flop_type == 0:
			return "%s%s%sr" % (self.cards[high_card], self.cards[mid_card], self.cards[low_card])

		if flop_type == 4:
			return "%s%s%ssss" % (self.cards[high_card], self.cards[mid_card], self.cards[low_card])

		if flop_type == 1:
			return "%ss%ss%s" % (self.cards[high_card], self.cards[mid_card], self.cards[low_card])

		if flop_type == 2:
			return "%ss%s%ss" % (self.cards[high_card], self.cards[mid_card], self.cards[low_card])

		if flop_type == 3:
			return "%s%ss%ss" % (self.cards[high_card], self.cards[mid_card], self.cards[low_card])


if __name__=="__main__":

	flop_factory = FlopFactory()
	flops = flop_factory.generate_all_flops()
	print len(flops)
	print flops
	while True:
		pass

		
