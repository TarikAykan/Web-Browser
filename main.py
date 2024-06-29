import tkinter as tk
import tkinter.messagebox as msgbox
import webbrowser as wb

class WebBrowserApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Web Tarayıcısı")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text ="URL:")
        self.label.pack(pady = 10)

        self.url_entry = tk.Entry(self.root, width= 50)
        self.url_entry.pack(pady = 5)

        self.go_button = tk.Button(self.root, text ="Git", command = self.open_url)
        self.go_button.pack(pady=10)

    def open_url(self):
        url = self.url_entry.get()
        if url:
            try:
                wb.open(url)
            except Exception as e:
                msgbox.showerror("Hata",f"Bağlantı açılırken bir hata oluştu: \n{str(e)}")
        else:
            msgbox.showwarning("Uyarı","Lütfen bir url girin")

if __name__ == "__main__":
    root = tk.Tk()
    app = WebBrowserApp(root)
    root.mainloop()
