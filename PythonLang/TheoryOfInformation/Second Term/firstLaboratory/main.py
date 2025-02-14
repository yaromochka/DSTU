import tkinter as tk
from calculator import calculate

def calc() -> None:
    expr: str = expr_entry.get()
    mod: int = int(mod_entry.get())
    result = calculate(expr, mod)
    result_label.config(text=f"Результат: {result}")

# --- Графический интерфейс ---
root = tk.Tk()
root.title("Калькулятор выражений в поле")

tk.Label(root, text="Выражение:").grid(row=0, column=0, padx=5, pady=5)
expr_entry = tk.Entry(root, width=30)
expr_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Модуль:").grid(row=1, column=0, padx=5, pady=5)
mod_entry = tk.Entry(root, width=10)
mod_entry.grid(row=1, column=1, padx=5, pady=5)

calc_button = tk.Button(root, text="Вычислить", command=calc)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Результат:")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()
