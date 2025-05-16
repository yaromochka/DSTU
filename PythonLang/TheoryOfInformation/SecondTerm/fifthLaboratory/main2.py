import tkinter as tk
from tkinter import ttk, messagebox
from PythonLang.TheoryOfInformation.SecondTerm.fifthLaboratory.enums.ChannelType import ChannelType
from PythonLang.TheoryOfInformation.SecondTerm.fifthLaboratory.CommunicationChannel import CommunicationChannel


class ChannelGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Communication Channel")

        self.channel_type = tk.StringVar(value=ChannelType.DSK.name)
        self.text_input = tk.StringVar()
        self.num_adders_input = tk.IntVar()
        self.adders_entries = []
        self.channel = None

        self.setup_widgets()

    def setup_widgets(self):
        ttk.Label(self.root, text="Тип канала:").grid(row=0, column=0, sticky="w")
        ttk.Combobox(self.root, textvariable=self.channel_type, values=[t.name for t in ChannelType]).grid(row=0, column=1)

        ttk.Label(self.root, text="Количество сумматоров:").grid(row=1, column=0, sticky="w")
        ttk.Entry(self.root, textvariable=self.num_adders_input).grid(row=1, column=1)
        ttk.Button(self.root, text="Подтвердить", command=self.create_adders_inputs).grid(row=1, column=2)

        self.adders_frame = ttk.Frame(self.root)
        self.adders_frame.grid(row=2, column=0, columnspan=3, sticky="ew")

        ttk.Label(self.root, text="Введите текст:").grid(row=3, column=0, sticky="w")
        ttk.Entry(self.root, textvariable=self.text_input, width=50).grid(row=3, column=1, columnspan=2, sticky="ew")

        ttk.Button(self.root, text="Выполнить", command=self.run_channel).grid(row=4, column=0, columnspan=3)

        self.output = tk.Text(self.root, height=20, width=80)
        self.output.grid(row=5, column=0, columnspan=3)

    def create_adders_inputs(self):
        for widget in self.adders_frame.winfo_children():
            widget.destroy()
        self.adders_entries.clear()
        for i in range(self.num_adders_input.get()):
            entry = ttk.Entry(self.adders_frame)
            entry.grid(row=i, column=0, sticky="ew")
            self.adders_entries.append(entry)

    def run_channel(self):
        try:
            adders = [list(map(int, entry.get().split(','))) for entry in self.adders_entries]
            text = self.text_input.get()

            self.channel = CommunicationChannel(ChannelType[self.channel_type.get()])
            self.channel.set_text(text)
            self.channel.set_adders(adders)
            self.channel.encode()
            self.channel.add_mistakes()

            encoded = self.channel.encoded_data
            new_encoded = self.channel.new_encoded_data
            errors = self.channel.count_p_errors()

            self.output.delete(1.0, tk.END)
            self.output.insert(tk.END, "Закодированные данные до искажений:\n")
            for line in encoded:
                self.output.insert(tk.END, f"{line}\n")
            self.output.insert(tk.END, "\nПосле искажений:\n")
            for line in new_encoded:
                self.output.insert(tk.END, f"{line}\n")

            self.output.insert(tk.END, "\n---\n")
            if ChannelType[self.channel_type.get()] in (ChannelType.DSK, ChannelType.Z):
                self.output.insert(tk.END, f"Вероятность ошибок: {errors[0]:.4f}\n")
                self.output.insert(tk.END, f"Пропускная способность: {errors[1]:.4f}\n")
            else:
                self.output.insert(tk.END, f"Вероятность ошибок: {errors[0]:.4f}\n")
                self.output.insert(tk.END, f"Вероятность стираний: {errors[1]:.4f}\n")
                self.output.insert(tk.END, f"Пропускная способность: {errors[2]:.4f}\n")

        except Exception as e:
            messagebox.showerror("Ошибка", str(e))


if __name__ == '__main__':
    root = tk.Tk()
    app = ChannelGUI(root)
    root.mainloop()