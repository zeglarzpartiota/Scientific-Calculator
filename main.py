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


class Calculator:
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_available = True
        self.operator = ''
        self.result = False
        self.second_op = False

    def enterNumber(self, number):
        first_number = entry.get()
        second_number = number
        if len(self.current) <= 18:
            if self.input_available:
                self.current = second_number
                self.input_available = False
            else:
                if second_number == '.':
                    if second_number in first_number:
                        return
                self.current = first_number + second_number
        display(self.current)

    def clear(self):
        display(self.current[0:-1])
        self.current = self.current[0:-1]
        if self.current == '':
            display('0')
            self.input_available = True

    def clearAllEntry(self):
        self.current = ''
        self.total = 0
        display('0')
        self.input_available = True
        self.result = False

    def counting(self):
        if self.operator == '*':
            return round(self.total * float(self.current), 15)
        elif self.operator == '/':
            return round(self.total / float(self.current), 15)
        elif self.operator == '+':
            return round(self.total + float(self.current), 15)
        elif self.operator == '-':
            return round(self.total - float(self.current), 15)
        else:
            return self.current

    def operation(self, op):
        self.operator = op
        if not self.result:
            self.total = float(self.current)
            self.current = ''
            self.result = True
            self.second_op = True
            display('0')
        else:  # elif just in case
            if not self.second_op:
                outcome = self.counting()
                self.total = outcome
                display(outcome)
                self.second_op = False
            else:
                pass
        self.input_available = True

    def equals(self):
        outcome = self.counting()
        display(outcome)
        self.current = str(outcome)
        self.total = 0
        self.input_available = True
        self.operator = ''
        self.result = False
        self.second_op = False

    # Functions

    def negation(self):
        self.current = float(self.current) * -1
        self.current = str(self.current)
        display(self.current)

    def pi(self):
        self.current = round(math.pi, 16)
        display(self.current)

    def log2(self):
        self.current = math.log2(float(self.current))
        display(self.current)

    def power(self):
        self.current = float(self.current) ** 2
        display(self.current)

    def root2(self):
        self.current = math.sqrt(float(self.current))
        display(self.current)

    def sine(self):
        self.current = math.sin(math.radians(float(self.current)))
        display(self.current)

    def cosine(self):
        self.current = math.cos(math.radians(float(self.current)))
        display(self.current)

    def tangent(self):
        self.current = math.tan(math.radians(float(self.current)))
        display(self.current)

    def hyperbolicSine(self):
        self.current = math.sinh(math.radians(float(self.current)))
        display(self.current)

    def hyperbolicCosine(self):
        self.current = math.cosh(math.radians(float(self.current)))
        display(self.current)

    def hyperbolicTangent(self):
        self.current = math.tanh(math.radians(float(self.current)))
        display(self.current)

    def arcSine(self):
        self.current = math.asin(float(self.current))
        display(self.current)

    def arcCosine(self):
        self.current = math.acos(float(self.current))
        display(self.current)

    def arcTangent(self):
        self.current = math.atan(float(self.current))
        display(self.current)

    def hyperbolicArcSine(self):
        self.current = math.asinh(float(self.current))
        display(self.current)

    def hyperbolicArcCosine(self):
        self.current = math.acosh(float(self.current))
        display(self.current)

    def hyperbolicArcTangent(self):
        self.current = math.atanh(float(self.current))
        display(self.current)


calculator = Calculator()

# ROW 1
buttonClear = Button(calc,
                     text='C',
                     width=6,
                     height=2,
                     border=0,
                     bg='#d4d4d2',
                     activebackground='#e6e6e5',
                     font=('Helvetica', 20, 'bold'),
                     command=lambda: calculator.clear()).grid(row=1, column=0, pady=1)
buttonAllClear = Button(calc,
                        text='CE',
                        width=6,
                        height=2,
                        border=0,
                        bg='#d4d4d2',
                        activebackground='#e6e6e5',
                        font=('Helvetica', 20, 'bold'),
                        command=lambda: calculator.clearAllEntry()).grid(row=1, column=1, pady=1)
buttonPi = Button(calc,
                  text='Pi',
                  width=6,
                  height=2,
                  border=0,
                  bg='#d4d4d2',
                  activebackground='#e6e6e5',
                  font=('Helvetica', 20, 'bold'),
                  command=lambda: calculator.pi()).grid(row=1, column=2, pady=1)
buttonDividing = Button(calc,
                        text='÷',
                        width=6,
                        height=2,
                        border=0,
                        bg='#ff9500',
                        activebackground='#ffb54d',
                        font=('Helvetica', 20, 'bold'),
                        command=lambda: calculator.operation('/')).grid(row=1, column=3, pady=1)
buttonLog2 = Button(calc,
                    text='log2',
                    width=6,
                    height=2,
                    border=0,
                    bg='#505050',
                    activebackground='#808080',
                    font=('Helvetica', 20, 'bold'),
                    command=lambda: calculator.log2()).grid(row=1, column=4, pady=1)
buttonLogX = Button(calc,
                    text='logx',
                    width=6,
                    height=2,
                    border=0,
                    bg='#505050',
                    activebackground='#808080',
                    font=('Helvetica', 20, 'bold')).grid(row=1, column=5, pady=1)  # TODO: command
buttonExponentiation2 = Button(calc,
                               text='x²',
                               width=6,
                               height=2,
                               border=0,
                               bg='#505050',
                               activebackground='#808080',
                               font=('Helvetica', 20, 'bold'),
                               command=lambda: calculator.power()).grid(row=1, column=6, pady=1)
buttonExponentiationX = Button(calc,
                               text='xⁿ',
                               width=6,
                               height=2,
                               border=0,
                               bg='#505050',
                               activebackground='#808080',
                               font=('Helvetica', 20, 'bold'),
                               command=lambda: calculator.powerX()).grid(row=1, column=7, pady=1)  # TODO: command

# ROW 2
buttonSeven = Button(calc,
                     text='7',
                     width=6,
                     height=2,
                     border=0,
                     bg='#505050',
                     activebackground='#808080',
                     font=('Helvetica', 20, 'bold'),
                     command=lambda: calculator.enterNumber('7')).grid(row=2, column=0, pady=1)
buttonEight = Button(calc,
                     text='8',
                     width=6,
                     height=2,
                     border=0,
                     bg='#505050',
                     activebackground='#808080',
                     font=('Helvetica', 20, 'bold'),
                     command=lambda: calculator.enterNumber('8')).grid(row=2, column=1, pady=1)
buttonNine = Button(calc,
                    text='9',
                    width=6,
                    height=2,
                    border=0,
                    bg='#505050',
                    activebackground='#808080',
                    font=('Helvetica', 20, 'bold'),
                    command=lambda: calculator.enterNumber('9')).grid(row=2, column=2, pady=1)
buttonMultiplication = Button(calc,
                              text='x',
                              width=6,
                              height=2,
                              border=0,
                              bg='#ff9500',
                              activebackground='#ffb54d',
                              font=('Helvetica', 20, 'bold'),
                              command=lambda: calculator.operation('*')).grid(row=2, column=3, pady=1)
buttonRoot2 = Button(calc,
                     text='√x',
                     width=6,
                     height=2,
                     border=0,
                     bg='#505050',
                     activebackground='#808080',
                     font=('Helvetica', 20, 'bold'),
                     command=lambda: calculator.root2()).grid(row=2, column=4, pady=1)
buttonSine = Button(calc,
                    text='sin',
                    width=6,
                    height=2,
                    border=0,
                    bg='#505050',
                    activebackground='#808080',
                    font=('Helvetica', 20, 'bold'),
                    command=lambda: calculator.sine()).grid(row=2, column=5, pady=1)
buttonCosine = Button(calc,
                      text='cos',
                      width=6,
                      height=2,
                      border=0,
                      bg='#505050',
                      activebackground='#808080',
                      font=('Helvetica', 20, 'bold'),
                      command=lambda: calculator.cosine()).grid(row=2, column=6, pady=1)
buttonTangent = Button(calc,
                       text='tan',
                       width=6,
                       height=2,
                       border=0,
                       bg='#505050',
                       activebackground='#808080',
                       font=('Helvetica', 20, 'bold'),
                       command=lambda: calculator.tangent()).grid(row=2, column=7, pady=1)

# ROW 3
buttonFour = Button(calc,
                    text='4',
                    width=6,
                    height=2,
                    border=0,
                    bg='#505050',
                    activebackground='#808080',
                    font=('Helvetica', 20, 'bold'),
                    command=lambda: calculator.enterNumber('4')).grid(row=3, column=0, pady=1)
buttonFive = Button(calc,
                    text='5',
                    width=6,
                    height=2,
                    border=0,
                    bg='#505050',
                    activebackground='#808080',
                    font=('Helvetica', 20, 'bold'),
                    command=lambda: calculator.enterNumber('5')).grid(row=3, column=1, pady=1)
buttonSix = Button(calc,
                   text='6',
                   width=6,
                   height=2,
                   border=0,
                   bg='#505050',
                   activebackground='#808080',
                   font=('Helvetica', 20, 'bold'),
                   command=lambda: calculator.enterNumber('6')).grid(row=3, column=2, pady=1)
buttonAddition = Button(calc,
                        text='+',
                        width=6,
                        height=2,
                        border=0,
                        bg='#ff9500',
                        activebackground='#ffb54d',
                        font=('Helvetica', 20, 'bold'),
                        command=lambda: calculator.operation('+')).grid(row=3, column=3, pady=1)
buttonRootX = Button(calc,
                     text='ⁿ√x',
                     width=6,
                     height=2,
                     border=0,
                     bg='#505050',
                     activebackground='#808080',
                     font=('Helvetica', 20, 'bold')).grid(row=3, column=4, pady=1)  # TODO: command
buttonHyperbolicSine = Button(calc,
                              text='sinh',
                              width=6,
                              height=2,
                              border=0,
                              bg='#505050',
                              activebackground='#808080',
                              font=('Helvetica', 20, 'bold'),
                              command=lambda: calculator.hyperbolicSine()).grid(row=3, column=5, pady=1)
buttonHyperbolicCosine = Button(calc,
                                text='cosh',
                                width=6,
                                height=2,
                                border=0,
                                bg='#505050',
                                activebackground='#808080',
                                font=('Helvetica', 20, 'bold'),
                                command=lambda: calculator.hyperbolicCosine()).grid(row=3, column=6, pady=1)
buttonHyperbolicTangent = Button(calc,
                                 text='tanh',
                                 width=6,
                                 height=2,
                                 border=0,
                                 bg='#505050',
                                 activebackground='#808080',
                                 font=('Helvetica', 20, 'bold'),
                                 command=lambda: calculator.hyperbolicTangent()).grid(row=3, column=7, pady=1)

# ROW 4
buttonOne = Button(calc,
                   text='1',
                   width=6,
                   height=2,
                   border=0,
                   bg='#505050',
                   activebackground='#808080',
                   font=('Helvetica', 20, 'bold'),
                   command=lambda: calculator.enterNumber('1')).grid(row=4, column=0, pady=1)
buttonTwo = Button(calc,
                   text='2',
                   width=6,
                   height=2,
                   border=0,
                   bg='#505050',
                   activebackground='#808080',
                   font=('Helvetica', 20, 'bold'),
                   command=lambda: calculator.enterNumber('2')).grid(row=4, column=1, pady=1)
buttonThree = Button(calc,
                     text='3',
                     width=6,
                     height=2,
                     border=0,
                     bg='#505050',
                     activebackground='#808080',
                     font=('Helvetica', 20, 'bold'),
                     command=lambda: calculator.enterNumber('3')).grid(row=4, column=2, pady=1)
buttonSubtraction = Button(calc,
                           text='-',
                           width=6,
                           height=2,
                           border=0,
                           bg='#ff9500',
                           activebackground='#ffb54d',
                           font=('Helvetica', 20, 'bold'),
                           command=lambda: calculator.operation('-')).grid(row=4, column=3, pady=1)
buttonArcSine = Button(calc,
                       text='asin',
                       width=6,
                       height=2,
                       border=0,
                       bg='#505050',
                       activebackground='#808080',
                       font=('Helvetica', 20, 'bold'),
                       command=lambda: calculator.arcSine()).grid(row=4, column=5, pady=1)
buttonArcCosine = Button(calc,
                         text='acos',
                         width=6,
                         height=2,
                         border=0,
                         bg='#505050',
                         activebackground='#808080',
                         font=('Helvetica', 20, 'bold'),
                         command=lambda: calculator.arcCosine()).grid(row=4, column=6, pady=1)
buttonArcTangent = Button(calc,
                          text='atan',
                          width=6,
                          height=2,
                          border=0,
                          bg='#505050',
                          activebackground='#808080',
                          font=('Helvetica', 20, 'bold'),
                          command=lambda: calculator.arcTangent()).grid(row=4, column=7, pady=1)

# ROW 5
buttonNegation = Button(calc,
                        text='+/-',
                        width=6,
                        height=2,
                        border=0,
                        bg='#505050',
                        activebackground='#808080',
                        font=('Helvetica', 20, 'bold'),
                        command=lambda: calculator.negation()).grid(row=5, column=0, pady=1)
buttonZero = Button(calc,
                    text='0',
                    width=6,
                    height=2,
                    border=0,
                    bg='#505050',
                    activebackground='#808080',
                    font=('Helvetica', 20, 'bold'),
                    command=lambda: calculator.enterNumber('0')).grid(row=5, column=1, pady=1)
buttonDot = Button(calc,
                   text='.',
                   width=6,
                   height=2,
                   border=0,
                   bg='#505050',
                   activebackground='#808080',
                   font=('Helvetica', 20, 'bold'),
                   command=lambda: calculator.enterNumber('.')).grid(row=5, column=2, pady=1)
buttonEquals = Button(calc,
                      text='=',
                      width=6,
                      height=2,
                      border=0,
                      bg='#ff9500',
                      activebackground='#ffb54d',
                      font=('Helvetica', 20, 'bold'),
                      command=lambda: calculator.equals()).grid(row=5, column=3, pady=1)
buttonHyperbolicArcSine = Button(calc,
                                 text='asinh',
                                 width=6,
                                 height=2,
                                 border=0,
                                 bg='#505050',
                                 activebackground='#808080',
                                 font=('Helvetica', 20, 'bold'),
                                 command=lambda: calculator.hyperbolicArcSine()).grid(row=5, column=5, pady=1)
buttonHyperbolicArcCosine = Button(calc,
                                   text='acosh',
                                   width=6,
                                   height=2,
                                   border=0,
                                   bg='#505050',
                                   activebackground='#808080',
                                   font=('Helvetica', 20, 'bold'),
                                   command=lambda: calculator.hyperbolicArcCosine()).grid(row=5, column=6, pady=1)
buttonHyperbolicArcTangent = Button(calc,
                                    text='atanh',
                                    width=6,
                                    height=2,
                                    border=0,
                                    bg='#505050',
                                    activebackground='#808080',
                                    font=('Helvetica', 20, 'bold'),
                                    command=lambda: calculator.hyperbolicArcTangent()).grid(row=5, column=7, pady=1)

entry.grid(row=0, column=0, columnspan=8, pady=1)
root.mainloop()
