#https://stackoverflow.com/questions/55971972/numpy-fast-fourier-transform-fft-does-not-work-on-sine-wave-generated-in-audac
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wave

N = 44100 # added

infile = "440_gen.wav"
rate, data = wave.read(infile)

data = np.array(data)

data_fft = np.fft.fft(data, N)  # added N
frequencies = np.abs(data_fft)
x_freq = np.fft.fftfreq(N, 1/44100)  # added

plt.subplot(2,1,1)
plt.plot(data[:800])
plt.title("Original wave: " + infile)

plt.subplot(2,1,2)
plt.plot(x_freq, frequencies)  # added x_freq 
plt.title("Fourier transform results")

plt.xlim(0, 1000)
plt.tight_layout()
plt.show()