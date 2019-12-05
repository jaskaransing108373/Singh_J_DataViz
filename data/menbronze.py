import matplotlib.pyplot as plt

years = [1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2000, 2002, 2006, 2010, 2014]

medals = [0, 0, 5.0, 0, 0, 0, 1, 1, 17, 1, 0, 18, 0, 1, 1, 1, 1, 1, 4, 2, 0, 2, 1, 5, 4]

plt.plot(years, medals, color=(255/255, 100/255, 100/255), linewidth=6.0)

plt.ylabel("Number of Bronze Medals")
plt.xlabel("number of Year")
plt.title("mens bronze medals - 1924-2014", pad=20)


plt.show()