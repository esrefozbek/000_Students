import pandas as pd
import matplotlib.pyplot as plt

# Örnek veri
df = pd.DataFrame({'x': [1, 2, 3], 'y': [1, 4, 9]})
df.plot(x='x', y='y')

# Grafik dosyaya kaydedilir
plt.savefig('grafik.png')