import itertools

def generate_variations(word):
    # Reemplazar las letras con números
    replacements = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5'}
    variations = [word]
    for i in range(1, len(word)):
        # Cambiar mayúsculas y minúsculas
        for combination in itertools.combinations(range(len(word)), i):
            for replacement in itertools.product([0, 1], repeat=i):
                new_word = list(word)
                for index, r in zip(combination, replacement):
                    if r == 0:
                        new_word[index] = new_word[index].upper()
                new_word = ''.join(new_word)
                for letter, number in replacements.items():
                    new_word = new_word.replace(letter, number)
                variations.append(new_word)
    return variations

word = 'palabra_2020'
variations = generate_variations(word)
print(variations)
