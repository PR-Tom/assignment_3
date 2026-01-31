def make_acronym(phrase):
    acronym = ""

    for word in phrase.split():

        acronym += word[0].upper()

    return acronym


print(make_acronym("unidentified foreign object"))
