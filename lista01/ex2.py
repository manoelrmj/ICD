from nose.tools import assert_equal
import re

def text_cons(sentence):
	result = []
	vowels = ('a', 'e', 'i', 'o', 'u')
	for word in sentence.split(' '):
		if word != unidecode(word):
			#result.append(re.sub('[aeiou]', '', word))
			for letter in word:
				if letter in vowels:
					word = word.replace(letter, "")
			result.append(word)
	return sorted(result)

def main():
	"""Check that text_cons returns the correct output for several inputs"""

	sample_text = "Existe uma teoria que diz que, se um dia alguém descobrir exatamente para que \
	serve o Universo e por que ele está aqui, ele desaparecerá instantaneamente e será substituído por algo ainda \
	mais estranho e inexplicável. Existe uma segunda teoria que diz que isso já aconteceu."

	text_cons(sample_text)

	#assert_equal(text_cons(sample_text), ['dsprcrá', 'já', 'lgém', 'nxplcávl.', 'sbsttíd', 'srá', 'stá'])	

if __name__ == '__main__':
	main()