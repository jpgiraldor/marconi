from scipy.io import wavfile
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import dangerzone as dz
import recognize, utils

def linearRregression():
    sample_rate, sample = wavfile.read('songs/hakuna_matata.wav')
    sample = sample[5000000:5000100]

    BadSample = sample.copy()
    dz.theEvilMethod(BadSample, 0.5, blocksize=2)

    matches = recognize.cheat(sample, BadSample)
    x, y = utils.tovalidxy(BadSample, matches)
    model = LinearRegression().fit(x,y)
    utils.repair(BadSample, matches, model)
    wavfile.write('songs/generator_song/regen_song.wav', sample_rate, BadSample)
    IwannaSee(sample, BadSample)

def IwannaSee(sample, BadSample):

    plt.title('Linear Regression')
    plt.xlabel('Frame')
    plt.ylabel('Amplitude')
    plt.plot(sample, label='real')
    plt.plot(BadSample, label='interpolated')
    plt.legend(loc='best')
    plt.show()

linearRregression()