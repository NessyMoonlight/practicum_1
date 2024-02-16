print('Введите плей-лист папы:')
playlist_dad = [
    input(), input(),input(),
    input(), input()
]
playlist_mom = playlist_dad[::-1]
print('Плей-лист мамы:')
for songs in playlist_mom:
    print(songs)