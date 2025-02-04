import customtkinter as ctk
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont 
import ctypes

#cores ---------------------------------------------------------------------
corRosa = "#ed85b8"
corRosaclaro = "#eb98c1"
corPreta = "#282b2e"
corBranca = "#faebf8"
corBrancoescuro = "#f7d5f3"

# janela -------------------------------------------------------------------

janela = Tk()
janela.title("Calculadora Kitty")
janela.geometry("320x450")
janela.config(bg=corPreta)


frame_tela = ctk.CTkFrame(janela, width=320, height=110, fg_color=corBranca)
frame_tela.grid(row=0, column=0)

frame_corpo = ctk.CTkFrame(janela, width=320, height=450, fg_color=corPreta)
frame_corpo.grid(row=1, column=0)

#travar janela -----------------------------------------
janela.resizable(False, False)
# icone janela ------------------------------------------
janela.iconbitmap("hellokittyico.ico")

#fontes --------------------------------------------------------------------

try:

    fonte_Starborn16 = ("Starborn", 16, "normal")

    fonte_Starborn32 = ("Starborn", 24, "normal")
    
    fonte_HelloKitty = ("Hello Kitty", 45, "normal")

except Exception as e:
    print(f"Erro ao carregar a fonte: {e}")
    fonte_Starborn16 = fonte_HelloKitty = ("Arial", 20)

# criando função -----------------------------------------------------------

todos_valores = ''

valor_texto = StringVar()

def entrar_valores(event):
    global todos_valores

    todos_valores = todos_valores + str(event)

    valor_texto.set(todos_valores)
 
# calcular -----------------------------------------------------------

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

# função clear/limpar ------------------------------------------------------

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

#label ---------------------------------------------------------------------



app_label = Label(frame_tela, textvariable=valor_texto, width=12, height=3, padx=5, relief=FLAT, anchor="e", justify=RIGHT, font=fonte_Starborn32, fg=corPreta, bg=corBranca)
app_label.place(x=0, y=0)

# Hello Kitty --------------------------------------------------------------

label = tk.Label(frame_corpo, text="X", font=fonte_HelloKitty, fg=corBranca, bg=corPreta)
label.place(x=125, y=-5)

#botoes linha 1 ------------------------------------------------------------

b_C = ctk.CTkButton(frame_corpo, text="C", font=fonte_Starborn16, width=150, height=50, fg_color=corRosa, text_color=corPreta, hover_color=corRosaclaro, corner_radius=5, command= limpar_tela)
b_C.place(x=5, y= 55)

b_porcentagem = ctk.CTkButton(frame_corpo, text="%", font=fonte_Starborn16, width=70, height=50, fg_color=corRosa, text_color=corPreta, hover_color=corRosaclaro, corner_radius=5, command= lambda: entrar_valores('%'))
b_porcentagem.place(x=165, y= 55)

b_divisao = ctk.CTkButton(frame_corpo, text="/", font=fonte_Starborn16, width=70, height=50, fg_color=corRosa, text_color=corPreta, hover_color=corRosaclaro, corner_radius=5, command= lambda: entrar_valores('/'))
b_divisao.place(x=245, y=55)

#vbotoes linha 2 -------------------------------------------------

b_7 = ctk.CTkButton(frame_corpo, text="7", font=fonte_Starborn16, width=70, height=50, fg_color=corBranca, text_color=corPreta, hover_color=corBrancoescuro, corner_radius=5, command= lambda: entrar_valores('7'))
b_7.place(x=5, y= 110)

b_8 = ctk.CTkButton(frame_corpo, text="8", font=fonte_Starborn16, width=70, height=50, fg_color=corBranca, text_color=corPreta, hover_color=corBrancoescuro, corner_radius=5, command= lambda: entrar_valores('8'))
b_8.place(x=85, y= 110)

b_9 = ctk.CTkButton(frame_corpo, text="9", font=fonte_Starborn16, width=70, height=50, fg_color=corBranca, text_color=corPreta, hover_color=corBrancoescuro, corner_radius=5, command= lambda: entrar_valores('9'))
b_9.place(x=165, y= 110)

b_multiplica = ctk.CTkButton(frame_corpo, text="*", font=fonte_Starborn16, width=70, height=50, fg_color=corRosa, text_color=corPreta, hover_color=corRosaclaro, corner_radius=5, command= lambda: entrar_valores('*'))
b_multiplica.place(x=245, y= 110)

#linha 3 ---------------------------------------------------------

b_4 = ctk.CTkButton(frame_corpo, text="4", font=fonte_Starborn16, width=70, height=50, fg_color=corBranca, text_color=corPreta, hover_color=corBrancoescuro, corner_radius=5, command= lambda: entrar_valores('4'))
b_4.place(x=5, y= 165)

b_5 = ctk.CTkButton(frame_corpo, text="5", font=fonte_Starborn16, width=70, height=50, fg_color=corBranca, text_color=corPreta, hover_color=corBrancoescuro, corner_radius=5, command= lambda: entrar_valores('5'))
b_5.place(x=85, y= 165)

b_6 = ctk.CTkButton(frame_corpo, text="6", font=fonte_Starborn16, width=70, height=50, fg_color=corBranca, text_color=corPreta, hover_color=corBrancoescuro, corner_radius=5, command= lambda: entrar_valores('6'))
b_6.place(x=165, y= 165)

b_menos = ctk.CTkButton(frame_corpo, text="-", font=fonte_Starborn16, width=70, height=50, fg_color=corRosa, text_color=corPreta, hover_color=corRosaclaro, corner_radius=5, command= lambda: entrar_valores('-'))
b_menos.place(x=245, y= 165)

#linha 4 ---------------------------------------------------------

b_1 = ctk.CTkButton(frame_corpo, text="1", font=fonte_Starborn16, width=70, height=50, fg_color=corBranca, text_color=corPreta, hover_color=corBrancoescuro, corner_radius=5, command= lambda: entrar_valores('1'))
b_1.place(x=5, y= 220)

b_2 = ctk.CTkButton(frame_corpo, text="2", font=fonte_Starborn16, width=70, height=50, fg_color=corBranca, text_color=corPreta, hover_color=corBrancoescuro, corner_radius=5, command= lambda: entrar_valores('2'))
b_2.place(x=85, y= 220)

b_3 = ctk.CTkButton(frame_corpo, text="3", font=fonte_Starborn16, width=70, height=50, fg_color=corBranca, text_color=corPreta, hover_color=corBrancoescuro, corner_radius=5, command= lambda: entrar_valores('3'))
b_3.place(x=165, y= 220)

b_mais = ctk.CTkButton(frame_corpo, text="+", font=fonte_Starborn16, width=70, height=50, fg_color=corRosa, text_color=corPreta, hover_color=corRosaclaro, corner_radius=5, command= lambda: entrar_valores('+'))
b_mais.place(x=245, y= 220)
 
#linha 5 ---------------------------------------------------------

b_zero = ctk.CTkButton(frame_corpo, text="0", font=fonte_Starborn16, width=70, height=50, fg_color=corBranca, text_color=corPreta, hover_color=corBrancoescuro, corner_radius=5, command= lambda: entrar_valores('0'))
b_zero.place(x=5, y= 275)

b_ponto = ctk.CTkButton(frame_corpo, text=".", font=fonte_Starborn16, width=70, height=50, fg_color=corRosa, text_color=corPreta, hover_color=corRosaclaro, corner_radius=5, command= lambda: entrar_valores('.'))
b_ponto.place(x=85, y= 275)

b_igual = ctk.CTkButton(frame_corpo, text="=", font=fonte_Starborn16, width=150, height=50, fg_color=corRosa, text_color=corPreta, hover_color=corRosaclaro, corner_radius=5, command= calcular)
b_igual.place(x=165, y= 275)

# calcular -----------------------------------------------------------



janela.mainloop()