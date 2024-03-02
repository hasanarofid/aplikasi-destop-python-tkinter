import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Dashboard")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # Membuat frame utama
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Membuat menu samping
        self.sidebar = tk.Frame(self.main_frame, width=200, bg='gray')
        self.sidebar.pack(fill=tk.Y, side=tk.LEFT)

        # Membuat konten utama
        self.content = tk.Frame(self.main_frame, bg='white')
        self.content.pack(fill=tk.BOTH, expand=True)

        # Membuat tombol navigasi di menu samping
        self.home_button = ttk.Button(self.sidebar, text="Home", command=self.show_home)
        self.home_button.pack(pady=10)

        self.logout_button = ttk.Button(self.sidebar, text="Logout", command=self.logout)
        self.logout_button.pack(pady=10)

        # Menampilkan halaman login atau beranda tergantung pada status sesi
        self.show_login() if not self.check_session() else self.show_home()

    def show_home(self):
        # Menghapus konten sebelumnya
        for widget in self.content.winfo_children():
            widget.destroy()

        # Membuat konten halaman beranda
        label = ttk.Label(self.content, text="Welcome to Home Page", font=("Helvetica", 20))
        label.pack(pady=100)

    def show_login(self):
        # Menghapus konten sebelumnya
        for widget in self.content.winfo_children():
            widget.destroy()

        # Membuat konten halaman login
            from login import Login 
            login_page2= Login()
            login_page2.mainloop()
    def logout(self):
        if messagebox.askokcancel("Logout", "Apakah Anda yakin ingin logout?"):
            # Menutup jendela utama
            self.destroy()
            # Membuka halaman login
            from login import Login  # Import lokal di dalam fungsi logout
            login_page = Login()
            login_page.mainloop()

    def check_session(self):
        # Fungsi untuk memeriksa apakah sesi pengguna sudah login atau tidak
        # Di sini, fungsi ini akan selalu mengembalikan False untuk contoh sederhana
        # Anda dapat menambahkan logika sesi pengguna yang sesungguhnya di sini
        # return False
        logged_in = False
        if not logged_in:
            self.show_login()

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
