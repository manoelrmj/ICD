import collections
from nose.tools import assert_equal

def sort_lists(list1, list2):
	list3 = list(zip(list1, list2))
	dictSal = {}
	for tp in list3:
		if tp[1] not in dictSal:
			dictSal[tp[1]] = []			
		dictSal[tp[1]].append(tp[0])

	orderedDictSal = collections.OrderedDict(sorted(dictSal.items(), reverse=True))
	result = []
	for salary in orderedDictSal.keys():
		tmpList = orderedDictSal[salary]
		tmpList.sort()
		for item in tmpList:
			result.append(item)

	return result

def main():
	"""Check that sort_lists returns the correct output for several inputs"""

	player = ["Neymar", "Piqué", "Benzema", "Neuer", "Iniesta", "Sergio Ramos", "Messi", "Oscar", "Griezmann", "Cavani", "Bale", "Pogba", "Cristiano Ronaldo", "Sanchez", "Kroos", "Lewandowski", "Lavezzi", "Ibrahimovic", "Muller", "Suarez"]
	player_salary = [81.5, 29, 23.5, 20.8, 25.5, 27.5, 126, 22.2, 26, 22.5, 44, 22, 96, 23.55, 28.2, 22.2, 25.3, 26.8, 23, 26]

	#sort_lists(player, player_salary)

	assert_equal(sort_lists(player, player_salary), ['Messi', 'Cristiano Ronaldo', 'Neymar', 'Bale', 'Piqué', 'Kroos', 'Sergio Ramos', 'Ibrahimovic', 'Griezmann', 'Suarez', 'Iniesta', 'Lavezzi', 'Sanchez', 'Benzema', 'Muller', 'Cavani', 'Lewandowski', 'Oscar', 'Pogba', 'Neuer'])

if __name__ == '__main__':
	main()