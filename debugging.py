def createg(stepfunction):
	g = np.ones(N)
	ptr = 0
	for i in range(N):
		if ptr == k-1:
			g[i] = stepfunction[ptr][1]
		elif h_plot[i, 0] < stepfunction[ptr+1][0]:
			g[i] = stepfunction[ptr][1]
		else:
			ptr += 1
			g[i] = stepfunction[ptr][1]

	return g


# Read Ayush File
f = open(ayush_output, 'r')
lines = f.readlines()
print(lines)
ayush_stepfn = []
for i in range(k):
	ayush_stepfn.append(list(map(float, lines[i+1][:-1].split()[:2])))

print(ayush_stepfn)

h_plot = np.asarray(h)
print(h_plot.shape)


def createg(stepfunction):
	g = np.ones(N)
	ptr = 0
	for i in range(N):
		if ptr == k-1:
			g[i] = stepfunction[ptr][1]
		elif h_plot[i, 0] < stepfunction[ptr+1][0]:
			g[i] = stepfunction[ptr][1]
		else:
			ptr += 1
			g[i] = stepfunction[ptr][1]

	return g

g_sans = createg(final_stepfn)
g_ayush = createg(ayush_stepfn)

print("Sansiddh Min of Max - " + str(np.max(np.absolute(g_sans - h_plot[:, 1]))))
print("Ayush Min of Max - " + str(np.max(np.absolute(g_ayush - h_plot[:, 1]))))

plt.figure()
plt.plot(h_plot[:, 0], h_plot[:, 1], 'ko')

for idx in range(len(final_stepfn)):
	if idx < (len(final_stepfn) - 1):
		print(final_stepfn[idx][1])
		plt.plot([final_stepfn[idx][0], final_stepfn[idx+1][0]], final_stepfn[idx][1]*np.ones(2), 'b-')
		plt.plot(final_stepfn[idx+1][0]*np.ones(2), [final_stepfn[idx][1], final_stepfn[idx+1][1]], 'b-')
	else:
		plt.plot([final_stepfn[idx][0], h_plot[h_plot.shape[0]-1, 0]], final_stepfn[idx][1]*np.ones(2), 'b-')

for idx in range(len(ayush_stepfn)):
	if idx < (len(ayush_stepfn) - 1):
		print(ayush_stepfn[idx][1])
		plt.plot([ayush_stepfn[idx][0], ayush_stepfn[idx+1][0]], ayush_stepfn[idx][1]*np.ones(2), 'r-')
		plt.plot(ayush_stepfn[idx+1][0]*np.ones(2), [ayush_stepfn[idx][1], ayush_stepfn[idx+1][1]], 'r-')
	else:
		plt.plot([ayush_stepfn[idx][0], h_plot[h_plot.shape[0]-1, 0]], ayush_stepfn[idx][1]*np.ones(2), 'r-')

plt.show()


[[7.0, 499.0], [1414.0, 520.0], [1532.0, 499.0]]

def createg_ayush(i):
	idx1 = np.where(h_plot[:, 0] == 1414)[0][0]
	idx2 = np.where(h_plot[:, 0] == 1532)[0][0]
	
	if i < idx1:
		return 499
	elif i < idx2:
		return 520
	else:
		return 499

g_ayush = np.ones(1000)
for i in range(1000):
	g_ayush[i] = createg_ayush(i)


[(7, 499.0), (1529, 500.5), (3534, 495.0)]
def createg_sans(i):
	idx1 = np.where(h_plot[:, 0] == 1529)[0][0]
	idx2 = np.where(h_plot[:, 0] == 3534)[0][0]

	if i < idx1:
		return 499
	elif i < idx2:
		return 500.5
	else:
		return 495

g_sans = np.ones(1000)
for i in range(1000):
	g_sans[i] = createg_sans(i)
