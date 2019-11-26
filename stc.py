from datetime import datetime
import numpy

times = [.1, .2, .3, .4, .5, 1, 3.5, 5, 5.5, 6, 6.5, 7, 8, 9, 10]
times = list(3600 * numpy.array(times))

audioSt = (0 * 3600) + (630 * 60) + (0)
audioLen = (0 * 3600) + (632 * 60) + (47)

dt = datetime.today()  # Get timezone naive now
now = dt.timestamp() + (20 * 60)

now = int(now)

#print(str(now < now + 3600))
#print(dt)
#print(datetime.fromtimestamp(now + 3600).strftime("%A, %B %d, %Y %I:%M:%S"))
#print(now)

wakes = []

for i in range(len(times)):
    ttw = datetime.fromtimestamp(now + times[i]) \
        .strftime("%A @ %I:%M%p") #%B %d, :%S
    ph = (audioSt - times[i])

    #ph = '{0:.0f}:{1:.0f}:{2:.2f}' \
    #    .format(ph // 3600, ((ph - (ph // 3600)) // 60) % 60 \
    #    , (ph - ((ph - (ph // 3600)) // 60)) % 60)

    min = (ph / 60)
    sec = ((ph // 60) % 60)

    ph = '{0:.0f}:{1:.2f}' \
        .format(min, sec)

    duration = times[i] / 3600

    if duration < 1:
        duration = '{0}m'.format(duration * 60)
    else:
        duration = '{0}h'.format(duration)

    wakes.append([duration, ttw, ph])

print('Here is the list of times and playheads: \n')

for o in wakes:
    print(('Sleep Duration: {0:>12} | Wake Time: {1:>24} | ' \
        + 'Playback Head: {2:>12} |\n') \
        .format(o[0], o[1], o[2]))
