I recently received some time to work on a passion project of mine.  As a guitar player (perhaps that is a generous description) and a software developer, I have always been interested in attempting to develop a guitar tuner myself.  My goal is to create a simple guitar tuner that works by analyzing a live audio signal via microphone - perfect for a laptop/desktop computer or mobile phone.  This problem touches on numerous different subjects, from music theory, to DSP (digital signal processing), to digital art (a guitar tuner needs to be able to provide visual feedback).  At the heart of any guitar tuner is some sort of pitch detection algorithm.  This post will focus on exploring 3 of those algorithms - zero-crossing, Fast Fourier Transform, and autocorrelation.

### Guitar Basics

Before diving into pitch detection, we need to understand some basics about the guitar.

// TODO: talk about frequencies of six strings, standard tuning, no non-standard tuning - maybe even harmonics? maybe clean vs dirty signals?
// TODO: talk about sine waves? frequency vs amplitude, etc? time domain vs frequency domain?

//TODO pitch is the frequency

### Zero crossing

//TODO good for getting our feet wet

Perhaps the most basic algorithm that can be considered for pitch detection is commonly called the "zero crossing" method.  As the name implies, this technique works by analyzing an audio signal in the time domain and counting the number of times the amplitude of the wave changes from a positive to a negative value.

//TODO show picture of clean signal

Here is a picture of a nice, clean sine wave. With a clean signal we can easily calculate the frequency of the signal. "The frequency of a sine wave is the number of complete cycles that happen every second".  

Here is a naive implementation of a zero-crossing algorithm in Javascript.

```
function getNumZeroCrossings (samples) {
  var numZeroCrossings = 0
  for (var i = 1; i < samples.length; i++) {
    if (samples[i] * samples[i - 1] < 0) {
      numZeroCrossings++
    }
  }
  return numZeroCrossings
}

function getNumCycles (numZeroCrossings) {
  return Math.floor((numZeroCrossings - 1) / 2)
}

function calculateFrequency (signalDurationSeconds, numCycles) {
  return numCycles / signalDurationSeconds
}

function start () {
  var signalDurationSeconds = 1
  var arr = [6, 2, -2, -6, -2, 2, 6, 2, -2, -6, -2, 2, 6, 2, -2] //this should be 2 hz
  var numZeroCrossings = getNumZeroCrossings(arr)
  var numCycles = getNumCycles(numZeroCrossings)
  console.log(numCycles)
  var freq = calculateFrequency(1, numCycles)
  console.log(freq + " Hz")
}

```

The zero crossing method of pitch detection is computationally inexpensive and easy to understand.  It works very well for clean audio signals.  Unfortunately clean audio signals are hard to come by while building a guitar tuner, especially when receiving input from a microphone.

//TODO show picture of realistic signal

Upsides:
- computationally inexpensive
- great for clear signals

Downsides:
- vulnerable to noise in signal
- singals are rarely clean

//Sources https://www.mathopenref.com/trigsinewaves.html#:~:text=The%20frequency%20of%20a%20sine,about%20one%20cycle%20per%20second.&text=One%20Hertz%20(1Hz)%20is%20equal%20to%20one%20cycle%20per%20second
The frequency of a sine wave is the number of complete cycles that happen every second.

https://blogs.arubanetworks.com/industries/frequency-cycle-wavelength-amplitude-and-phase/#:~:text=%22An%20oscillation%2C%20or%20cycle%2C,to%20negative%20to%20positive.%22%20%2D
//An oscillation, or cycle, of this alternating current is defined as a single change from up to down to up, or as a change from positive, to negative to positive.


### FFT

How does it work?

resolution depends on FFT length and sampling rate

resolution = (sample rate) / (fft size)
e.g.
46.875 = 48000 / 1024
The resolution is our bin width. That is WAY too big for a guitar tuner.

To find the frequency, find the largest bin.
e.g.
Sample rate = 48000
fft size = 16384
resolution = bin width = 2.92
If you see a spike in bin 55, then do:
frequency = bin * resolution
so, 160.2 = 55 * 2.92

Downsides:

- require processing power
- low resolution makes it hard to identify lower notes
- hard to distinguish between harmonics
- hard to identify particular octave

### Autocorrelation

- equation
- code
- graphs

### Better options

- combination of the above
- That one Greek algorithm
  Still need visual feedback - will investigate canvas element later
