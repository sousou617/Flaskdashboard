import matplotlib.pyplot as plt
import numpy as np

raw_data = pd.read_csv('report_requests.csv')
data = raw_data[:10]['Name', 'Median time']

names = data.iloc[:, 0]
time = data.iloc[:, 1]
indx = np.arange(len(data))

plt.figure(figsize=(10,7))

graphMath = plt.bar(x=indx, height=names, width=0.35)

plt.xlabel('names')
plt.ylabel('time')

names = ['\n'.join(wrap(name, 15)) for name in names]
plt.xticks(indx, names)
plt.yticks(np.arange(0, 2400, 2400/len(indx)))
plt.title('Median Response Time')

# plt.show()


