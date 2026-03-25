import tkinter as tk
janela = tk.Tk()
janela.title("Calculadora")
entrada = tk.Entry(janela, width=25)
entrada.grid(row=0, column=0, columnspan=4)
def add_num(num):
    entrada.insert(tk.END, num)
def resultado():
    conta = entrada.get()
    try:
        resp = eval(conta)
        entrada.delete(0, tk.END)
        entrada.insert(0, resp)
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "erro")
def limpar():
    entrada.delete(0, tk.END)

tk.Button(janela, text="7", command=lambda: add_num("7")).grid(row=1, column=0)
tk.Button(janela, text="8", command=lambda: add_num("8")).grid(row=1, column=1)
tk.Button(janela, text="9", command=lambda: add_num("9")).grid(row=1, column=2)
tk.Button(janela, text="/", command=lambda: add_num("/")).grid(row=1, column=3)

tk.Button(janela, text="4", command=lambda: add_num("4")).grid(row=2, column=0)
tk.Button(janela, text="5", command=lambda: add_num("5")).grid(row=2, column=1)
tk.Button(janela, text="6", command=lambda: add_num("6")).grid(row=2, column=2)
tk.Button(janela, text="*", command=lambda: add_num("*")).grid(row=2, column=3)

tk.Button(janela, text="1", command=lambda: add_num("1")).grid(row=3, column=0)
tk.Button(janela, text="2", command=lambda: add_num("2")).grid(row=3, column=1)
tk.Button(janela, text="3", command=lambda: add_num("3")).grid(row=3, column=2)
tk.Button(janela, text="-", command=lambda: add_num("-")).grid(row=3, column=3)

tk.Button(janela, text="0", command=lambda: add_num("0")).grid(row=4, column=0)
tk.Button(janela, text=".", command=lambda: add_num(".")).grid(row=4, column=1)
tk.Button(janela, text="+", command=lambda: add_num("+")).grid(row=4, column=2)

tk.Button(janela, text="=", command=resultado).grid(row=4, column=3)
tk.Button(janela, text="C", command=limpar).grid(row=5, column=0, columnspan=4)

janela.mainloop() 
