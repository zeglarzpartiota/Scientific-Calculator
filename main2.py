from tkinter import *
import math

root = Tk()
root.title('Scientific Calculator')
root.geometry('881x523')
root.config(bg='#1d1c1d')
root.resizable(width=False, height=False)
icon = PhotoImage(file='icon.png')
root.iconphoto(True, icon)

calc = Frame(root,
             bg='#1d1c1d',
             width=885,
             height=525)
calc.pack()

t = StringVar()

entry = Entry(calc,
              textvariable=t,
              width=20,
              font=('Helvetica', 60),
              bg='#1d1c1d',
              fg='white',
              justify=RIGHT,
              border=False)

entry.insert(0, '0')


def display(value):
    entry.delete(0, END)
    entry.insert(0, value)


def current_operation(sign: str, o_value):
    if sign == '^':
        return float(o_value[0]) ** float(o_value[1])
    elif sign == '√':
        # much more efficient than using math's power module ~ 6
        return float(o_value[1]) ** (1.0 / float(o_value[0]))
    else:
        return math.log(float(o_value[1]), (float(o_value[0])))


class Calculator:
    def __init__(self):
        self.total_value = 0
        self.current_value = ''
        self.input_available = True
        self.operator = ''
        self.result = False
        self.is_end = False
        self.sign = ''

    def enterNumber(self, number):
        first_number = entry.get()
        second_number = number
        if len(self.current_value) <= 19:
            if self.input_available:
                self.current_value = second_number
                self.input_available = False
            else:
                if second_number == '.':
                    if second_number in first_number:
                        return
                        # TODO: split current to be able to check whether there is a dot in second part of any_x
                self.current_value = first_number + second_number
        display(self.current_value)

    def clear(self):
        display(self.current_value[0:-1])
        self.current_value = self.current_value[0:-1]
        if self.current_value == '':
            display('0')
            self.input_available = True

    def clearAllEntry(self):
        self.current_value = ''
        self.total_value = 0
        display('0')
        self.input_available = True
        self.result = False

    def counting(self):
        if self.operator == '*':
            return round(self.total_value * float(self.current_value), 15)
        elif self.operator == '/':
            return round(self.total_value / float(self.current_value), 15)
        elif self.operator == '+':
            return round(self.total_value + float(self.current_value), 15)
        elif self.operator == '-':
            return round(self.total_value - float(self.current_value), 15)
        else:
            return self.current_value

    def operation(self, op):
        if not self.result:
            self.total_value = float(self.current_value)
            self.current_value = ''
            self.result = True
            display('0')
        elif self.result:
            outcome = self.counting()
            self.total_value = outcome
            display(outcome)
        self.input_available = True
        self.operator = op

    def equals(self):
        if not self.is_end:
            outcome = self.counting()
            display(outcome)
            self.current_value = str(outcome)
            self.total_value = 0
            self.input_available = True
            self.operator = ''
            self.result = False
        else:
            self.result_of_any_x(self.sign)

    def result_of_any_x(self, sign):
        operation = entry.get()
        operation_values = operation.split(sign)
        result_of_operation = current_operation(sign=sign, o_value=operation_values)
        display(result_of_operation)
        self.current_value = result_of_operation
        self.is_end = False
        self.sign = ''

    # Functions

    def any_x(self, sign):
        self.is_end = True
        self.sign = sign
        display(entry.get() + sign)

    def negation(self):
        self.current_value = float(self.current_value) * -1
        self.current_value = str(self.current_value)
        display(self.current_value)

    def pi(self):
        self.current_value = round(math.pi, 16)
        display(self.current_value)

    def sine(self):
        self.current_value = math.sin(math.radians(float(self.current_value)))
        display(self.current_value)

    def cosine(self):
        self.current_value = math.cos(math.radians(float(self.current_value)))
        display(self.current_value)

    def tangent(self):
        self.current_value = math.tan(math.radians(float(self.current_value)))
        display(self.current_value)

    def hyperbolicSine(self):
        self.current_value = math.sinh(math.radians(float(self.current_value)))
        display(self.current_value)

    def hyperbolicCosine(self):
        self.current_value = math.cosh(math.radians(float(self.current_value)))
        display(self.current_value)

    def hyperbolicTangent(self):
        self.current_value = math.tanh(math.radians(float(self.current_value)))
        display(self.current_value)


calculator = Calculator()


# ROW 1
buttonClear = Button(
    calc,
    text='C',
    width=6,
    height=2,
    border=0,
    bg='#d4d4d2',
    activebackground='#e6e6e5',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.clear()
).grid(row=1, column=0, pady=1)

buttonAllClear = Button(
    calc,
    text='CE',
    width=6,
    height=2,
    border=0,
    bg='#d4d4d2',
    activebackground='#e6e6e5',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.clearAllEntry()
).grid(row=1, column=1, pady=1)

buttonPi = Button(
    calc,
    text='Pi',
    width=6,
    height=2,
    border=0,
    bg='#d4d4d2',
    activebackground='#e6e6e5',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.pi()
).grid(row=1, column=2, pady=1)

buttonDividing = Button(
    calc,
    text='÷',
    width=6,
    height=2,
    border=0,
    bg='#ff9500',
    activebackground='#ffb54d',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.operation('/')
).grid(row=1, column=3, pady=1)

buttonLog2 = Button(
    calc,
    text='log2',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold')
).grid(row=1, column=4, pady=1)

buttonLogX = Button(
    calc,
    text='logx',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.any_x(sign='log')
).grid(row=1, column=5, pady=1)

buttonExponentiation2 = Button(
    calc,
    text='x²',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold')
).grid(row=1, column=6, pady=1)

buttonExponentiationX = Button(
    calc,
    text='xⁿ',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.any_x(sign='^')
).grid(row=1, column=7, pady=1)

# ROW 2
buttonSeven = Button(
    calc,
    text='7',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.enterNumber('7')
).grid(row=2, column=0, pady=1)
buttonEight = Button(
    calc,
    text='8',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.enterNumber('8')
).grid(row=2, column=1, pady=1)

buttonNine = Button(
    calc,
    text='9',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.enterNumber('9')
).grid(row=2, column=2, pady=1)

buttonMultiplication = Button(
    calc,
    text='x',
    width=6,
    height=2,
    border=0,
    bg='#ff9500',
    activebackground='#ffb54d',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.operation('*')
).grid(row=2, column=3, pady=1)

buttonRoot2 = Button(
    calc,
    text='√x',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold')
).grid(row=2, column=4, pady=1)

buttonSine = Button(
    calc,
    text='sin',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.sine()
).grid(row=2, column=5, pady=1)

buttonCosine = Button(
    calc,
    text='cos',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.cosine()
).grid(row=2, column=6, pady=1)

buttonTangent = Button(
    calc,
    text='tan',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold')
).grid(row=2, column=7, pady=1)

# ROW 3
buttonFour = Button(
    calc,
    text='4',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.enterNumber('4')
).grid(row=3, column=0, pady=1)

buttonFive = Button(
    calc,
    text='5',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.enterNumber('5')
).grid(row=3, column=1, pady=1)

buttonSix = Button(
    calc,
    text='6',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.enterNumber('6')
).grid(row=3, column=2, pady=1)

buttonAddition = Button(
    calc,
    text='+',
    width=6,
    height=2,
    border=0,
    bg='#ff9500',
    activebackground='#ffb54d',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.operation('+')
).grid(row=3, column=3, pady=1)

buttonRootX = Button(
    calc,
    text='ⁿ√x',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.any_x(sign='√')
).grid(row=3, column=4, pady=1)

buttonHyperbolicSine = Button(
    calc,
    text='sinh',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.hyperbolicSine()
).grid(row=3, column=5, pady=1)

buttonHyperbolicCosine = Button(
    calc,
    text='cosh',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.hyperbolicCosine()
).grid(row=3, column=6, pady=1)

buttonHyperbolicTangent = Button(
    calc,
    text='tanh',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.hyperbolicTangent()
).grid(row=3, column=7, pady=1)

# ROW 4
buttonOne = Button(
    calc,
    text='1',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.enterNumber('1')
).grid(row=4, column=0, pady=1)

buttonTwo = Button(
    calc,
    text='2',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.enterNumber('2')
).grid(row=4, column=1, pady=1)

buttonThree = Button(
    calc,
    text='3',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.enterNumber('3')
).grid(row=4, column=2, pady=1)

buttonSubtraction = Button(
    calc,
    text='-',
    width=6,
    height=2,
    border=0,
    bg='#ff9500',
    activebackground='#ffb54d',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.operation('-')
).grid(row=4, column=3, pady=1)

# ROW 5
buttonNegation = Button(
    calc,
    text='+/-',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.negation()
).grid(row=5, column=0, pady=1)

buttonZero = Button(
    calc,
    text='0',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.enterNumber('0')
).grid(row=5, column=1, pady=1)

buttonDot = Button(
    calc,
    text='.',
    width=6,
    height=2,
    border=0,
    bg='#505050',
    activebackground='#808080',
    command=lambda: calculator.enterNumber('.'),
    font=('Helvetica', 20, 'bold')
).grid(row=5, column=2, pady=1)

buttonEquals = Button(
    calc,
    text='=',
    width=6,
    height=2,
    border=0,
    bg='#ff9500',
    activebackground='#ffb54d',
    font=('Helvetica', 20, 'bold'),
    command=lambda: calculator.equals()
).grid(row=5, column=3, pady=1)

entry.grid(row=0, column=0, columnspan=8, pady=1)
root.mainloop()
