import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Contraseñas")
        self.root.geometry("500x400")  
        
        self.label_length = tk.Label(root, text="Longitud de la Contraseña:")
        self.label_length.pack(pady=10)
        
        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=10)
        
        self.generate_button = tk.Button(root, text="Generar Contraseña", command=self.generate_password)
        self.generate_button.pack(pady=20)
        
        self.password_label = tk.Label(root, text="Contraseña Generada:")
        self.password_label.pack(pady=10)
        
        self.password_entry = tk.Entry(root, show='')
        self.password_entry.pack(pady=10)
        
        
        self.developer_label = tk.Label(root, text="Developed with ❤️ by Carlos Calleja Saez", font=("Arial", 10))
        self.developer_label.pack(side=tk.BOTTOM, pady=10)
        
    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(password_length))
            self.password_entry.delete(0, tk.END)  
            self.password_entry.insert(0, password)
        except ValueError:
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, "Introduce un número válido")


root = tk.Tk()
app = PasswordGenerator(root)
root.mainloop()
