import datetime
now = datetime.datetime.now()

MARKI = [
    ('DAF', 'DAF'),
    ('MAN', 'MAN'),
    ('VOLVO', 'VOLVO'),
    ('SCANIA', 'SCANIA'),
    ('IVECO', 'IVECO'),
    ('RENAULT', 'RENAULT'),
    ('MERCEDES', 'MERCEDES'),
    ('Krone', 'Krone'),
    ('Schwartzmüller', 'Schwartzmüller'),
    ('Schmitz', 'Schmitz'),
    ('Wielton', 'Wielton'),
    ('Mega', 'Mega'),
    ('Kassbohrer', 'Kassbohrer'),
    ('Kögel', 'Kögel'),
    ('inne', 'inne')
    ]
RODZAJE = [
    ('ciągnik siodłowy', 'ciągnik siodłowy'),
    ('samochód ciężarowy firana', 'samochód ciężarowy firana'),
    ('samochód ciężarowy wywrotka 3-4 osie.', 'samochód ciężarowy wywrotka 3-4 osie'),
    ('samochód ciężarowy tandem', 'samochód ciężarowy tandem'),
    ('przyczepa 2 osie', 'przyczepa 2 osie'),
    ('przyczepa tandem firana', 'przyczepa tandem firana'),
    ('naczepa firana', 'naczepa firana'),
    ('naczepa firana low deck', 'naczepa firana low deck'),
    ('naczepa plandeka burty', 'naczepa plandeka burty'),
    ('naczepa platforma', 'naczepa platforma'),
    ('naczepa szkielet.kontener BDF', 'naczepa szkielet.kontener BDF'),
    ('naczepa samowyładowcza walking-floor', 'naczepa samowyładowcza walking-floor'),
    ('naczepa wywrotka', 'naczepa wywrotka'),
    ('naczepa silos', 'naczepa silos'),
    ('naczepa cysterna ciecz', 'naczepa cysterna ciecz'),
    ('naczepa cysterna gaz', 'naczepa cysterna gaz'),
    ('naczepa cysterna paszowóz', 'naczepa cysterna paszowóz'),
    ('naczepa laweta niskopodwoz.', 'naczepa laweta niskopodwoz.'),
    ('naczepa chłodnia', 'naczepa chłodnia'),
    ('naczepa izoterma', 'naczepa izoterma'),

]

ROCZNIK =[]
actual_year = int(now.year)
for i in range(actual_year+1, actual_year-40, -1):
    inside=[]
    inside.append(i)
    inside.append(str(i))
    inside_tup=tuple(inside)
    ROCZNIK.append(inside_tup)

EURO =[
    ('Euro 7', 'Euro 7'),
    ('Euro 6', 'Euro 6'),
    ('Euro 5', 'Euro 5'),
    ('Euro 4', 'Euro 4'),
    ('Euro 3', 'Euro 3'),
    ('Euro 2', 'Euro 2'),
    ('Euro 1', 'Euro 1'),
    ('Euro 0', 'Euro 0'),
    ('N49', 'N49'),
    ('nie dotyczy', 'nie dotyczy'),
]

