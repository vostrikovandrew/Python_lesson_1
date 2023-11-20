def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


a = 3
b = 1 / 2
n = 3
x = 1.

print('a =', a, type(a))
print('b =', b, type(a))
print('x =', x, type(a))

w = b ** n * np.cos(a ** n * np.pi * x)
print(w)

s = sum(b ** n * np.cos(a ** n * np.pi * x) for n in range(0, 10))
print(s)

sw = 'b ** n * np.cos(a ** n * np.pi * x)'
print('sw =', sw, type(sw))
s50 = sum(eval(sw) for n in range(0, 50))
print(s50)
s100 = sum(eval(sw) for n in range(0, 100))
print(s100)

dx = 0.0001
x = np.arange(-2, 2 + dx, dx)
print('x =', x, type(x))

plt.plot(x, sum(eval(sw) for n in range(0, 50)))
plt.show()
