# write a function local_greet that takes a locale as input, and returns a greeting.
def greet(isolang):
    match isolang:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'
        case _:
            return 'Invalid ISO Language Code'


def extract_language(locale):
    return locale[:2]


def extract_region(locale):
    return locale.split('.')[0].split('_')[1]


def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match region:
        case 'US':
            return 'Hey!'
        case 'GB':
            return 'Hello!'
        case 'AU':
            return 'Howdy'
        case _:
            return greet(language)


print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!
