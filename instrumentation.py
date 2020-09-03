import math


def full(num):
    flute = round(num * 0.09)
    oboe = math.trunc(num * 0.03)
    bassoon = math.trunc(num * 0.03)
    clarinet = round(num * 0.20)
    bass_clarinet = math.trunc(num * 0.04)
    alto = round(num * 0.08)
    tenor = round(num * 0.03)
    bari = math.trunc(num * 0.02)
    trumpet = round(num * 0.16)
    french_horn = round(num * 0.06)
    trombone = round(num * 0.08)
    euphonium = round(num * 0.04)
    tuba = round(num * 0.04)
    percussion = round(num * 0.10)

    total = flute + oboe + bassoon + clarinet + bass_clarinet + alto + tenor + bari + trumpet + french_horn + trombone + euphonium + tuba + percussion
    print('original total:', total)

    if total > num:
        extra = total - num
        clarinet = clarinet - extra
        new_total = flute + oboe + bassoon + clarinet + bass_clarinet + alto + tenor + bari + trumpet + french_horn + trombone + euphonium + tuba + percussion
        print("too many at first. new:", new_total)

    elif num > total:
        extra = num - total
        clarinet = clarinet + extra
        new_total = flute + oboe + bassoon + clarinet + bass_clarinet + alto + tenor + bari + trumpet + french_horn + trombone + euphonium + tuba + percussion
        print("Too little at first. new:", new_total)

    result = [flute, oboe, bassoon, clarinet, bass_clarinet, alto, tenor, bari, trumpet, french_horn, trombone, euphonium, tuba, percussion]
    return result


def reduced(num):
    flute = round(num * 0.12)
    clarinet = round(num * 0.27)
    alto = round(num * 0.13)
    trumpet = round(num * 0.21)
    trombone = round(num * 0.11)
    euphonium = round(num * 0.06)
    percussion = round(num * 0.10)

    total = flute + clarinet + alto + trumpet + trombone + euphonium + percussion
    print('original total:', total)

    if total > num:
        extra = total - num
        clarinet = clarinet - extra
        new_total = flute + clarinet + alto + trumpet + trombone + euphonium + percussion
        print("too many at first. new:", new_total)

    elif num > total:
        extra = num - total
        clarinet = clarinet + extra
        new_total = flute + clarinet + alto + trumpet + trombone + euphonium + percussion
        print("Too little at first. new:", new_total)

    result = [flute, clarinet, alto, trumpet, trombone, euphonium, percussion]
    return result


def categorical(num):
    flute = round(num * 0.13)
    single_reeds = math.trunc(num * 0.39)
    high_brass = math.trunc(num * 0.21)
    low_brass = round(num * 0.17)
    percussion = math.trunc(num * 0.10)

    total = flute + single_reeds + high_brass + low_brass + percussion
    print('original total:', total)

    if total > num:
        extra = total - num
        single_reeds = single_reeds - extra
        new_total = flute + single_reeds + high_brass + low_brass + percussion
        print("too many at first. new:", new_total)

    elif num > total:
        extra = num - total
        single_reeds = single_reeds + extra
        new_total = flute + single_reeds + high_brass + low_brass + percussion
        print("Too little at first. new:", new_total)

    result = [flute, single_reeds, high_brass, low_brass, percussion]
    return result
