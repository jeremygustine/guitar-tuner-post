import numpy as np
import matplotlib.pyplot as plt

N = 8192
t = np.arange(N)

m = 4
nu = float(m)/N
# f = np.sin(2*np.pi*nu*t)
# ft = np.fft.fft(f)
# freq = np.fft.fftfreq(N)


arr = [0,0,0,0,0,0,0,0,0,0,0,2,3,10,19,15,3,0,7,19,40,51,50,47,49,48,53,56,35,44,75,65,59,83,79,54,52,64,56,25,10,4,15,42,42,34,40,53,58,62,74,78,71,76,72,76,78,68,73,70,67,82,75,68,67,55,59,49,47,52,50,53,58,58,55,28,43,46,59,52,44,67,84,117,134,126,95,50,31,41,45,42,24,34,29,14,31,31,12,25,29,27,9,5,14,5,20,30,30,31,13,26,29,29,25,33,46,59,70,65,45,14,19,34,27,8,29,41,42,40,53,57,43,15,0,28,42,33,8,0,19,26,19,32,38,31,17,23,36,25,13,4,24,40,43,43,33,26,50,60,54,38,23,63,70,66,104,157,174,161,115,57,63,62,8,35,48,55,45,35,13,14,44,47,39,28,24,14,0,5,16,5,0,0,0,1,8,0,27,43,19,32,52,44,20,47,34,20,23,25,28,42,47,48,49,50,16,42,48,50,53,48,33,9,8,31,47,44,49,47,14,25,22,26,43,41,51,48,42,33,67,76,71,61,55,41,40,65,58,27,108,161,178,166,120,31,63,79,69,26,35,54,50,34,47,49,30,28,49,59,55,43,19,0,16,39,41,7,0,17,42,42,32,29,14,13,0,22,27,35,22,10,0,0,25,4,12,33,21,25,47,69,77,65,53,51,37,23,9,0,18,2,0,29,28,7,35,47,36,0,34,39,22,38,54,59,46,24,56,66,60,33,39,62,102,162,181,169,124,38,59,45,54,44,29,40,39,35,28,7,0,19,20,29,37,27,20,30,38,27,12,0,11,0,14,26,28,28,20,21,40,38,23,0,33,36,23,22,26,21,0,0,0,0,0,22,39,34,15,0,0,0,0,19,18,0,0,0,0,0,3,11,9,0,0,0,0,0,0,0,5,7,18,27,30,25,3,23,29,94,122,119,86,28,25,0,13,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,7,17,21,20,11,6,11,5,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,9,4,0,0,0,0,4,0,0,0,0,7,29,51,58,45,16,10,14,0,0,1,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,12,0,26,33,28,34,29,12,17,9,0,7,17,7,0,18,18,17,24,27,24,15,18,7,0,6,19,0,28,49,57,46,35,20,21,0,24,44,37,12,28,35,0,14,5,18,3,13,0,0,0,18,1,0,10,14,0,0,0,5,1,0,0,6,1,0,0,10,7,0,0,0,0,0,0,0,0,0,0,0,19,26,0,0,0,3,6,3,3,11,23,29,32,26,0,0,8,29,35,13,28,36,42,53,44,47,63,54,46,61,42,52,72,98,131,141,122,74,53,13,56,68,70,68,53,37,29,28,33,40,38,27,5,32,45,47,45,41,28,12,31,40,31,6,0,2,0,0,15,27,27,25,14,0,0,0,0,1,6,2,0,0,11,19,0,0,9,28,22,16,34,32,23,11,6,7,20,23,39,31,0,36,41,32,23,46,58,56,58,56,31,54,69,58,45,62,73,88,67,121,138,124,88,83,72,5,25,50,53,69,67,64,57,30,0,26,4,36,32,26,38,49,37,10,0,0,0,0,0,0,18,19,11,16,30,21,0,0,0,0,0,4,4,1,0,0,0,0,0,0,28,32,15,0,0,0,0,0,0,0,0,0,0,10,17,0,19,25,6,13,35,38,21,4,14,33,43,47,68,75,78,75,84,99,127,138,121,84,65,44,38,61,71,68,50,16,19,26,30,16,19,15,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,2,21,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,20,20,0,1,0,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,5,24,24,49,64,47,0,27,45,75,71,37,0,0,0,0,6,37,38,21,6,10,22,26,15,1,0,0,2,4,0,10,4,0,6,9,8,15,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,23,30,15,15,22,20,2,0,6,19,10,0,0,0,8,0,28,40,19,35,49,27,42,59,57,49,58,65,74,76,59,76,75,96,134,142,121,73,48,5,52,39,65,76,68,61,60,56,47,34,17,24,33,41,27,0,16,19,0,0,0,0,0,0,0,0,0,0,18,31,18,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,21,0,0,0,3,15,20,29,33,2,20,1,3,31,37,52,58,51,26,44,50,54,74,67,49,83,96,77,54,77,96,103,117,154,163,141,88,78,80,56,83,73,66,73,69,70,77,84,87,79,55,37,48,67,74,62,43,35,32,39,41,41,59,59,36,11,11,33,46,34,12,2,0,0,0,2,26,30,12,0,0,0,0,0,0,21,27,15,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,5,20,8,0,5,35,28,0,56,65,49,42,0,56,59,87,125,129,104,74,68,61,72,77,57,19,0,30,34,30,13,18,27,16,27,13,15,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,19,6,13,20,0,4,14,13,30,31,22,4,1,43,54,56,74,85,68,33,32,36,28,20,35,34,30,22,47,54,37,46,29,37,36,12,25,28,18,8,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,21,40,48,34,72,76,58,38,23,6,0,0,0,0,0,0,0,6,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,9,0,17,8,0,0,0,3,17,32,21,28,31,19,0,12,18,0,0,26,51,55,13,61,83,77,41,0,11,20,23,17,9,0,0,14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,7,0,0,6,2,0,0,16,8,32,29,36,78,104,104,77,49,52,61,55,32,16,8,1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,1,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,2,4,1,0,0,0,0,0,0,0,0,0,7,24,14,0,0,1,0,26,33,15,27,33,43,78,73,49,21,0,19,54,63,48,21,17,12,10,3,0,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,1,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,11,9,1,20,10,18,33,52,42,38,50,52,50,56,66,109,128,115,74,63,68,14,41,46,41,42,54,51,29,9,15,19,2,0,0,0,0,0,0,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,4,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,20,12,15,26,26,11,35,45,44,47,37,4,33,31,0,7,0,41,62,65,56,46,37,86,119,123,91,17,45,62,52,23,56,51,32,36,0,49,58,44,31,32,38,27,17,27,23,11,21,22,10,0,0,2,13,17,16,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,5,10,6,19,26,7,13,20,41,60,64,45,24,32,29,10,9,12,0,0,5,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,18,12,0,17,26,22,25,7,38,49,43,51,58,53,27,26,57,65,53,8,0,14,21,5,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,19,28,43,48,52,59,49,19,8,38,58,61,69,76,93,85,56,43,19,28,32,47,52,33,4,3,0,0,0,0,0,0,0,0,0,6,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,2,10,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,8,0,0,3,13,23,0,5,16,16,19,21,14,26,39,49,44,65,97,108,89,51,74,59,0,47,45,0,31,38,17,0,24,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,34,32,2,33,45,71,85,79,67,67,88,124,129,107,86,63,65,61,45,71,75,63,10,42,35,0,20,23,24,13,0,0,0,2,7,0,0,0,6,37,52,37,1,11,2,10,14,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,5,0,0,0,0,0,0,0,0,0,17,36,59,70,60,43,42,36,18,11,43,60,73,58,11,28,37,49,38,107,126,116,83,66,69,68,68,64,66,64,46,41,45,24,18,17,10,0,0,0,4,0,0,0,10,18,21,12,7,18,5,32,51,62,58,37,14,19,33,29,21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,6,0,0,8,0,3,13,0,0,13,0,9,21,7,20,17,71,92,78,0,37,47,45,36,24,0,0,0,19,34,25,39,53,75,78,67,65,55,38,36,31,10,0,0,0,0,0,0,0,7,0,0,13,26,37,39,22,0,21,44,56,59,53,42,22,30,37,31,22,14,0,0,0,3,14,5,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,18,13,0,0,0,23,34,0,48,62,50,40,35,23,34,37,20,0,10,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,3,15,14,1,0,11,33,42,35,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,29,44,40,24,0,0,13,17,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,5,31,34,20,25,36,43,58,54,8,26,29,0,0,0,0,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,2,9,23,32,28,15,26,39,48,46,37,23,0,6,29,30,20,8,0,0,0,0,0,0,0,0,0,0,0,6,22,23,36,49,51,60,63,42,17,4,19,35,30,0,0,35,47,55,60,48,8,79,104,95,48,43,12,24,27,0,20,17,0,7,19,0,11,5,0,11,23,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,21,14,0,2,20,27,24,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,23,22,32,38,38,30,26,67,85,78,34,28,0,0,6,0,22,28,29,25,28,40,35,50,85,104,101,79,54,46,24,4,14,29,23,16,6,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,16,29,53,57,29,0,0,0,15,15,4,0,0,0,0,0,0,9,0,19,0,12,16,1,41,0,42,0,36,0,36,14,21,9,0,0,5,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2,0,0,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,2,20,24,7,30,31,14,30,31,26,23,17,2,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,6,3,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,9,0,0,0,0,0,0,9,2,0,0,0,0,0,4,13,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,22,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,30,22,2,0,0,3,15,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,6,4,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,5,13,15,13,6,0,0,0,5,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,13,16,11,7,7,9,7,7,6,4,0,0,0,0,0,0,0,0,1,3,2,7,10,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,5,0,0,0,0,0,0,0,0,3,5,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,13,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,1,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,2,4,14,19,18,18,16,13,11,4,0,0,0,0,0,0,4,7,3,0,0,0,0,0,0,0,0,0,0,0,1,6,5,0,0,0,0,0,5,10,10,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,5,0,0,3,17,22,16,1,0,5,13,11,1,0,0,0,0,0,12,17,10,5,9,15,18,18,18,16,17,18,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,9,0,0,0,0,0,0,0,0,0,0,0,0,4,5,1,0,0,0,0,0,0,0,3,12,10,5,5,6,10,17,22,21,10,0,0,0,0,0,0,7,12,14,14,8,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,13,0,0,0,0,0,0,0,0,2,6,0,0,0,0,0,0,0,6,8,1,0,0,0,0,0,0,2,7,4,0,0,0,7,6,0,11,17,10,0,0,0,0,0,0,0,0,0,0,0,7,13,12,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,10,4,0,0,0,0,0,0,0,0,0,7,20,26,22,11,0,0,7,0,0,0,0,3,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,15,10,0,0,0,7,13,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,8,12,6,0,0,0,0,0,11,20,21,20,19,15,1,0,0,0,0,0,0,0,0,0,1,7,10,7,0,0,0,0,0,0,0,0,0,0,0,0,0,1,5,4,0,0,0,2,2,1,0,0,0,0,5,6,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,14,21,18,10,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,8,10,5,0,0,0,0,0,1,3,0,0,0,0,0,3,9,1,0,2,7,15,21,19,7,0,0,2,3,5,9,11,12,12,9,3,1,0,0,0,0,3,5,0,0,0,0,0,0,0,0,0,0,0,0,5,12,10,5,0,0,0,0,0,0,0,4,7,3,0,0,0,0,0,0,0,0,0,0,0,3,7,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,7,9,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,5,2,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,4,9,7,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,10,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,16,15,0,0,6,11,0,0,0,4,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,7,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,11,9,0,0,0,0,6,12,12,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,8,6,0,0,0,3,1,0,0,0,4,0,0,0,0,0,0,0,0,0,2,5,3,0,0,0,4,8,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,6,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,5,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,5,5,2,0,0,0,0,5,7,6,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,6,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,42,61,52,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,6,0,0,0,0,0,0,0,0,0,3,5,0,0,0,1,5,0,0,0,0,0,0,0,0,0,5,3,7,17,20,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,8,0,0,0,0,0,7,13,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,3,0,24,38,20,0,0,0,0,0,0,0,0,0,0,0,0,0,6,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,39,44,19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,38,62,59,19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,22,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


# plt.plot(freq, ft.real**2 + ft.imag**2)
print(len(arr))
plt.plot(arr[0:1000])

plt.show()