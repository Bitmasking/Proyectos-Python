from tkinter import *
import parser

pantalla = Tk()
pantalla.title("Calculadora")
pantalla
display = Entry(pantalla)

idx = 0


def tipear(n):
    global idx
    display.insert(idx, n)
    idx += 1


def tipear_op(op):
    global idx
    opsz = len(op)
    display.insert(idx, op)
    idx += opsz


def limpiar():
    global idx
    display.delete(0, END)


def borrar():
    texto = display.get()
    if len(texto):
        res = texto[:-1]
        limpiar()
        display.insert(0, res)
    else:
        limpiar()
        display.insert(0, "ERROR")


def resultado():
    res = display.get()
    try:
        ans = parser.expr(res).compile()
        imp = eval(ans)
        limpiar()
        display.insert(0, imp)
    except Exception:
        limpiar()
        display.insert(0, "ERROR")


# Input de Datos
display.grid(row=1, columnspan=6, sticky=W+E)
# Botones
Button(pantalla, text="1", command=lambda: tipear(1)).grid(
    row=2, column=0, sticky=W+E)
Button(pantalla, text="2", command=lambda: tipear(2)).grid(
    row=2, column=1, sticky=W+E)
Button(pantalla, text="3", command=lambda: tipear(3)).grid(
    row=2, column=2, sticky=W+E)
Button(pantalla, text="4", command=lambda: tipear(4)).grid(
    row=3, column=0, sticky=W+E)
Button(pantalla, text="5", command=lambda: tipear(5)).grid(
    row=3, column=1, sticky=W+E)
Button(pantalla, text="6", command=lambda: tipear(6)).grid(
    row=3, column=2, sticky=W+E)
Button(pantalla, text="7", command=lambda: tipear(7)).grid(
    row=4, column=0, sticky=W+E)
Button(pantalla, text="8", command=lambda: tipear(8)).grid(
    row=4, column=1, sticky=W+E)
Button(pantalla, text="9", command=lambda: tipear(9)).grid(
    row=4, column=2, sticky=W+E)

# Operadores
Button(pantalla, text="AC", command=lambda: limpiar()).grid(
    row=5, column=0, sticky=W+E)
Button(pantalla, text="0", command=lambda: tipear(0)).grid(
    row=5, column=1, sticky=W+E)
Button(pantalla, text="%", command=lambda: tipear_op("%")).grid(
    row=5, column=2, sticky=W+E)

Button(pantalla, text="+", command=lambda: tipear_op("+")
       ).grid(row=2, column=3, sticky=W+E)
Button(pantalla, text="-", command=lambda: tipear_op("-")
       ).grid(row=3, column=3, sticky=W+E)
Button(pantalla, text="*", command=lambda: tipear_op("*")
       ).grid(row=4, column=3, sticky=W+E)
Button(pantalla, text="/", command=lambda: tipear_op("/")
       ).grid(row=5, column=3, sticky=W+E)

Button(pantalla, text="ᐸ", command=lambda: borrar()).grid(
    row=2, column=4, sticky=W+E, columnspan=2)
Button(pantalla, text="exp", command=lambda: tipear_op(
    "**")).grid(row=3, column=4, sticky=W+E)
Button(pantalla, text="^2", command=lambda: tipear_op(
    "**2")).grid(row=3, column=5, sticky=W+E)
Button(pantalla, text="(", command=lambda: tipear_op(
    "(")).grid(row=4, column=4, sticky=W+E)
Button(pantalla, text=")", command=lambda: tipear_op(
    ")")).grid(row=4, column=5, sticky=W+E)
Button(pantalla, text="=", command=lambda: resultado()).grid(
    row=5, column=4, sticky=W+E, columnspan=2)


pantalla.mainloop()
