from scipy.io import wavfile
from scipy.interpolate import InterpolatedUnivariateSpline
import dangerzone as dz
import recognize, utils

def cubicSplineInterpolation():
    sample_rate, sample = wavfile.read('songs/hakuna_matata.wav')

    BadSample = sample.copy()

    dz.theEvilMethod(BadSample, 0.5)
    matches = recognize.cheat(sample, BadSample)
    x, y = utils.tovalidxy(BadSample, matches)
    f = InterpolatedUnivariateSpline(x,y)

    xNotValid = utils.invalidx(matches)
    fixedy = f(xNotValid)
    utils.replace(BadSample, xNotValid, fixedy)
    wavfile.write('songs/generator_song/regen_splineUnivariate_song.wav', sample_rate, BadSample)

cubicSplineInterpolation()