import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import subprocess

class ImageWindow:
    def __init__(self, master, image_path):
        self.master = master
        self.master.title("Image Viewer")

        self.image_path = image_path

        # Load image using PIL
        try:
            self.image = Image.open(self.image_path)
            self.tk_image = ImageTk.PhotoImage(self.image)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open image: {e}")
            self.master.destroy()
            return

        # Display the image
        self.image_label = tk.Label(master, image=self.tk_image)
        self.image_label.pack(padx=10, pady=10)

        # Save and Print buttons
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)

        self.save_button = tk.Button(self.button_frame, text="Save As...", command=self.save_image)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.print_button = tk.Button(self.button_frame, text="Print", command=self.print_image)
        self.print_button.pack(side=tk.LEFT, padx=5)

    def save_image(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg *.jpeg"), ("All files", "*.*")]
        )
        if file_path:
            try:
                self.image.save(file_path)
                messagebox.showinfo("Success", f"Image saved to {file_path}")
            except Exception as e:
                messagebox.showerror("Save Error", f"Could not save image: {e}")

    def print_image(self):
        try:
            # Use lp command to send the image to the default printer
            subprocess.run(["lp", self.image_path], check=True)
            messagebox.showinfo("Print", "Image sent to printer.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Print Error", f"Failed to print image:\n{e}")
        except Exception as e:
            messagebox.showerror("Print Error", f"Unexpected error:\n{e}")
