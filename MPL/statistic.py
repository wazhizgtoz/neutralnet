import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [2,4,6,8,10]

plt.bar(x,y, label='Barras', color='green')

plt.xlabel('mes')
plt.ylabel('volume')
plt.legend('descrição')
plt.title('Quantidade Vendida')

plt.show()
