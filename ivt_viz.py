import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)
k = 0.5

plt.figure(figsize=(8, 5))
plt.plot(x, y, 'b-', linewidth=2, label='f(x) = sin(x)')
plt.axhline(y=k, color='r', linestyle='--', label=f'k = {k}')

crossings = x[np.where(np.diff(np.sign(y - k)))[0]]
plt.plot(crossings, [k]*len(crossings), 'go', markersize=10, label='IVT points')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Intermediate Value Theorem')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('ivt.png', dpi=100)
plt.show()
