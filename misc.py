import requests


def get_word_definitions(word: str) -> list:
    """
    This function returns a list with definitions of the word passed as an argument.
    :param word: a word (string) that you want to find definitions (and examples of use) of.
    :return: returns a list with definitions. Returns None in case of unsuccessful request.
    """

    if word.isalpha():
        word_url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'

        resp = requests.get(word_url)
        if resp.status_code == 200:
            definitions_full_list = resp.json()[0].get('meanings')[0].get('definitions')
            # pprint()
            definitions = [definition.get('definition') for definition in definitions_full_list]
            # examples = [example.get('example') for example in definitions_full_list]
            return definitions
