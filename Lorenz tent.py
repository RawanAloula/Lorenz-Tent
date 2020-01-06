

from scipy.signal import find_peaks

x = X[:,2]    #get z  (this depends on the structutr of your data)

#extract location of peaks 
peaks, _ = find_peaks(x, height=0)    


# Plot peaks 
plt.plot(x)
plt.plot(peaks, x[peaks], "ro")
plt.show()


# Plot Tent
zn = x[peaks[:-1]]
zn1 = x[peaks[1:]]

plt.scatter(zn,zn1, c= 'r')
plt.xlabel('Z_n')
plt.ylabel('Z_(n+1)')
plt.plot(zn,zn,'k-')