import sys, random


class CardRange(object):

    """Ranges"""

    def __init__(self):

        self.valid_card = ['2', '3', '4', '5' ,'6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        self.card_number = 13

        self.valid_suit = ['s', 'h', 'c', 'd']
        self.suit_number = 4

        self.card_index = {}
        for i in range(len(self.valid_card)):
            self.card_index[self.valid_card[i]] = i

        self.card_range = []

    def add_range_from(self, range_string):

        range_interval = range_string.split(',')
        for interval in range_interval:
            self.card_range.extend(self.produce_card_range(interval))

    def produce_card_range(self, interval):

        res = []
        if '~' in interval:

            if len(interval) != 7 and len(interval) != 5:
                return []

            if len(interval) == 5: # like 44~QQ

                if interval[0] != interval[1] or interval[3] != interval[4]:
                    return []

                if interval[0] not in self.valid_card or interval[3] not in self.valid_card:
                    return []

                start_index = self.card_index[interval[0]]
                end_index = self.card_index[interval[3]] + 1

                for i in range(start_index, end_index):
                    for j in range(self.suit_number):
                        for k in range(j + 1, self.suit_number):
                            res.append("%s%s%s%s" % (self.valid_card[i], self.valid_suit[j], self.valid_card[i], self.valid_suit[k]))

                return res

            if len(interval) == 7:

                if interval[0] == interval[4]:   # A2o~A8o, K5s~K8s

                    if interval[0] not in self.valid_card or interval[1] not in self.valid_card or interval[5] not in self.valid_card:
                        return []

                    if interval[2] != interval[6]:
                        return []

                    fix_card_index = self.card_index[interval[0]]
                    low_card_index = self.card_index[interval[1]]
                    high_card_index = self.card_index[interval[5]] + 1

                    for i in range(low_card_index, high_card_index):

                        if interval[2] == 'o':
                            for j in range(self.suit_number):
                                for k in range(self.suit_number):
                                    if j == k:
                                        continue
                                    res.append("%s%s%s%s" % (self.valid_card[fix_card_index], self.valid_suit[j], self.valid_card[i], self.valid_suit[k]))

                        if interval[2] == 's':
                            for j in range(self.suit_number):
                                res.append("%s%s%s%s" % (self.valid_card[fix_card_index], self.valid_suit[j], self.valid_card[i], self.valid_suit[j]))


                else:  # 98s~JTs, 65o~98o

                    if interval[0] not in self.valid_card or interval[1] not in self.valid_card or interval[4] not in self.valid_card or interval[5] not in self.valid_card:
                        return []

                    if interval[2] != interval[6]:
                        return []

                    a_high_card_index = self.card_index[interval[0]]
                    a_low_card_index = self.card_index[interval[1]]
                    b_high_card_index = self.card_index[interval[4]]
                    b_low_card_index = self.card_index[interval[5]]

                    delta = a_high_card_index - a_low_card_index

                    if delta <= 0:
                        return []

                    if b_high_card_index - b_low_card_index != a_high_card_index - a_low_card_index:
                        return []

                    if a_high_card_index >= b_high_card_index:
                        return []

                    for i in range(a_high_card_index, b_high_card_index + 1):

                        for j in range(self.suit_number):
                            for k in range(self.suit_number):
                                if j == k and interval[2] == 's':
                                    res.append("%s%s%s%s" % (self.valid_card[i], self.valid_suit[j], self.valid_card[i - delta], self.valid_suit[k]))
                                if j != k and interval[2] == 'o':
                                    res.append("%s%s%s%s" % (self.valid_card[i], self.valid_suit[j], self.valid_card[i - delta], self.valid_suit[k]))

        elif '+' in interval:

            n = len(interval)
            if n == 3:  # pocket pair: like JJ+, 77+,

                if interval[0] != interval[1]:
                    return []

                if interval[0] not in self.valid_card:
                    return []

                start_index = self.card_index[interval[0]]
                end_index = self.card_number

                for i in range(start_index, end_index):
                    for j in range(self.suit_number):
                        for k in range(j + 1, self.suit_number):
                            res.append("%s%s%s%s" % (self.valid_card[i], self.valid_suit[j], self.valid_card[i], self.valid_suit[k]))

            if n == 4:   # suited: A2o+, K8s+

                if interval[0] not in self.valid_card or interval[1] not in self.valid_card:
                    return []

                high_card_index = self.card_index[interval[0]]
                low_card_index = self.card_index[interval[1]]

                if high_card_index <= low_card_index:
                    return []

                for i in range(low_card_index, high_card_index):

                    for j in range(self.suit_number):
                        for k in range(self.suit_number):
                            if j == k and interval[n - 2] == 's':
                                res.append("%s%s%s%s" % (self.valid_card[high_card_index], self.valid_suit[j], self.valid_card[i], self.valid_suit[k]))
                            if j != k and interval[n - 2] == 'o':
                                res.append("%s%s%s%s" % (self.valid_card[high_card_index], self.valid_suit[j], self.valid_card[i], self.valid_suit[k]))

        return res

if __name__=="__main__":

    BTN_RFI = CardRange()
    #BTN_RFI.add_range_from("98s~JTs")
    #BTN_RFI.add_range_from("44~QQ")
    BTN_RFI.add_range_from("A2o+")
    print BTN_RFI.card_range

