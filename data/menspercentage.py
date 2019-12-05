import csv
import matplotlib.pyplot as plt

golds = []
silvers = []
bronzes = []

categories = []

with open('data/mensmedals.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("this is first row in the spread sheet")
			categories.append(row)
			line_count += 1

		else:
			if row[7] == "Gold":
				print("won a gold medal")
				golds.append(row[7])
			elif row[7] == "Silver":
				print("won a silver medal")
				silvers.append(row[7])
			else:
				print("won a bronze medal")
				bronzes.append(row[7])

			print(line_count)
			line_count += 1


print(len(golds), "gold medals")
print(len(silvers), "silver medals")
print(len(bronzes), "bronze medals")

labels = ["Gold", "Silver", "Bronze"]
sizes = [len(golds), len(silvers), len(bronzes)]
colors = ['gold', 'silver', 'darkgoldenrod']


plt.pie(sizes, colors=colors, autopct='%.1f%%', shadow=True, startangle=140,)

plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Men's Medals percentage")
plt.xlabel("Medal Counts 1924-2014")
plt.show()
