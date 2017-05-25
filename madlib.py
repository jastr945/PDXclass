# This is a Mad Lib lab

name = input('Enter a name: ').capitalize()
adverb = input('Enter an adverb: ').lower()
car = input('Enter a car model: ').lower()
adj = input('Enter an adjective: ').lower()
adj2 = input('Enter another adjective: ').lower()
adverb2 = input('Enter another adverb: ').lower()
place = input('Enter the name of the city: ').capitalize()


text = """
Hi {}! he said {} as he jumped into his convertible {} and drove off
with his {} wife... I looked at them an said: 'Have a {} day guys!'
Then he stopped the car and exclaimed {}: 'Would you like to go to {} with
us?'
""". format(name, adverb, car, adj, adj2, adverb2, place)
print(text)