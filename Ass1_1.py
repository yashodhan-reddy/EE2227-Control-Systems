from scipy import signal
import matplotlib.pyplot as plt

system = signal.lti([1,2], [3,4]) # Transfer function's numerator cofficients in first array and denominator coefficients in second array 
r = range(0, 10000)  
w, mag, phase = signal.bode(system, w=r)
plt.figure()
plt.grid(True, which="both")
plt.semilogx(w, mag)    # Bode magnitude plot
plt.ylabel("[dB]")
plt.xlabel("[rad/s]")
plt.figure()
plt.grid(True, which="both")
plt.semilogx(w, phase)  # Bode phase plot
plt.ylabel("[degrees]")
plt.xlabel("[rad/s]")
plt.show()
