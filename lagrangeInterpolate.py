from scipy.io import wavfile
from scipy.interpolate import BarycentricInterpolator
#import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import dangerzone as dz
import recognize, utils
import numpy as np

def lagrangeInterpolation():
    sample_rate, sample = wavfile.read('songs/hakuna_matata.wav')
    sample = sample[5000000:5000100]

    sample_rateBAD, sampleBAD = wavfile.read('songs/bad_songs/not_good_song.wav')
    sampleBAD = sampleBAD[5000000:5000100]

    BadSample = sample.copy()

    dz.theEvilMethod(BadSample, 0.7)
    matches = recognize.cheat(sample, BadSample)
    x, y = utils.tovalidxy(BadSample, matches)

    f = BarycentricInterpolator(x,y)
    utils.repair(BadSample, matches, f)

    IwannaSee(sample, BadSample, sampleBAD)

def IwannaSee(sample, BadSample, sampleBAD):

    plt.title('Lagrange interpolation')
    plt.xlabel('Frame')
    plt.ylabel('Amplitude')
    plt.plot(sample, label='real')
    plt.plot(sampleBAD, label='Bad')
    plt.plot(BadSample, label='interpolated')
    plt.legend(loc='best')
    plt.show()

lagrangeInterpolation()