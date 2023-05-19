import tkinter as tk
#++++++++++++++++++++++++++++++
def on_btn1_click():
  txt = entry.get()
  #global label
  #global btn1
  #global app
  label.configure(text=txt, bg="pink")
  btn1.configure(text="Já clicou aqui", bg="red")
  app.configure(bg="purple")

def on_btn2_click():
  label.configure(text="vish, eu avisei.", bg="brown")
  btn1.configure(text="Já clicou aqui", bg="cyan")
  btn2.configure(text="tchau", bg="navy")
  app.configure(bg="black")
#++++++++++++++++++++++++++++++
app = tk.Tk()
app.geometry("400x300")
app.configure(bg="lightblue")
#++++++++++++++++++++++++++++++
label = tk.Label(app, text="Rodrigo", bg="lightgreen", width=20, height=2)
label.pack(pady="10")

entry = tk.Entry(app, width=30)
entry.pack(pady=20)

btn1 = tk.Button(app, text="Clique aqui", command = on_btn1_click, bg="green", width=20, height=2)
btn1.pack(pady=10)

btn2 = tk.Button(app, text="NÃO CLIQUE AQUI!", command = on_btn2_click, bg="grey", width=20, height=2)
btn2.pack(pady=10)
#++++++++++++++++++++++++++++++
app.mainloop()
