- zero crossing
- FFT
- auto correlation

### Goal

Make a real-time guiter tuner via microphone
Rely on pitch-detection algorithms

### Guitar basics
Talk about frequencies
Talk about harmonics

### Zero crossing

Perhaps the most basic algorithm that can be considered for detecting the frequency of an audio signal is commonly called a "zero crossing" method.

//TODO show picture of clean signal
//TODO show picture of realistic signal


# https://www.mathopenref.com/trigsinewaves.html#:~:text=The%20frequency%20of%20a%20sine,about%20one%20cycle%20per%20second.&text=One%20Hertz%20(1Hz)%20is%20equal%20to%20one%20cycle%20per%20second
The frequency of a sine wave is the number of complete cycles that happen every second.

An extremely naive version of the code is shown below:
```
function calculateNumCycles (samples) {
  var numZeroCrossings = 0
  var numCycles = 0
  for (var i = 1; i < samples.length; i++) {
    if (samples[i] * samples[i - 1] < 0) { numZeroCrossings++ }
    if (numZeroCrossings === 3) {
      numCycles++
      numZeroCrossings = 1
    }
  }
  return numCycles
}

function calculateFrequencyInHz (signalDurationSeconds, numCycles) {
  return numCycles / signalDurationSeconds
}

function start () {
  var signalDurationSeconds = 1
  var arr = [6, 2, -2, -6, -2, 2, 6, 2, -2, -6, -2, 2, 6, 2, -2]
  var numCycles = calculateNumCycles(arr)
  var freq = calculateFrequencyInHz(1, numCycles)
  console.log(freq) // out puts "2"
}
```

The zero crossing algorithm is great for clean signals.  Unfortunately clean signals are difficult to achieve, especially with a microphone.




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
