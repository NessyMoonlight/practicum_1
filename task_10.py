print('номер рейса:')
flight_number = input()
print('название авиакомпании (на русском языке):')
avianame_rus = input()
print('название авиакомпании (на английском языке):')
avianame_eng = input()
print('город прилета (на русском языке):')
town_rus = input()
print('город прилета (на английском языке):')
town_eng = input()
print('Заканчивается посадка на рейс', flight_number,
      avianame_rus, 'до', town_rus)
print('This the final boarding call for', avianame_eng,
      'flight', flight_number, 'to', town_eng)