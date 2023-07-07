def klavye_mesafe(kelime1, kelime2):
    klavye = {
        'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4), 'y': (0, 5), 'u': (0, 6), 'ı': (0, 7), 'o': (0, 8), 'p': (0, 9), 'ğ':(0,10), 'ü':(0,10),
        'a': (1, 0.3), 's': (1, 1.3), 'd': (1, 2.3), 'f': (1, 3.3), 'g': (1, 4.3), 'h': (1, 5.3), 'j': (1, 6.3), 'k': (1, 7.3), 'l': (1, 8.3), 'ş': (1, 9.3), 'i':(1,10.3), ',':(1,11.3),
        '<': (2,0.6), 'z': (2, 1.6), 'x': (2, 2.6), 'c': (2, 3.6), 'v': (2, 4.6), 'b': (2, 5.6), 'n': (2, 6.6), 'm': (2, 7.6), 'ö': (2, 8.6), 'ç': (2, 9.6), '.': (2,10.6)
    }

    mesafe = 0
    for i in range(len(kelime1)):
        x1, y1 = klavye.get(kelime1[i], (0, 0))
        x2, y2 = klavye.get(kelime2[i], (0, 0))

        mesafe += (abs(x1 - x2)**2 + abs(y1 - y2)**2)**1/2

    return mesafe

while True:
    first = input("First:")
    second = input("Second:")
    print(klavye_mesafe(first, second))
