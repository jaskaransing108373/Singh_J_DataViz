import numpy as np
import matplotlib.pyplot as plt
 

height = [51, 21, 2, 38, 6, 41, 32]
bars = ['1924-48', '1952-68', '1972-88', '1992-2002', '2006', '2010', '2014']
y_pos = np.arange(len(bars))
 
# Create bars
plt.bar(y_pos, height)
 
# Create names on the x-axis
plt.xticks(y_pos, bars)
plt.ylabel("Number of Medals")
plt.xlabel("number of Years")
plt.title("Mens Gold medals - 1924-2014", pad=20)


plt.show()
