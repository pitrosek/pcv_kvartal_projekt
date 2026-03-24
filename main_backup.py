import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from PIL import Image, ImageTk
import os
import time
import json
from config.game_config import GAME_CONFIG, COLORS, FONTS, get_reveal_cost, get_letter_hint_cost


class GameState:
    """Správa stavu hry"""
    def __init__(self):
        self.points = GAME_CONFIG["starting_points"]
        self.grid_size = GAME_CONFIG["grid_size"]
        self.total_cells = self.grid_size ** 2
        self.revealed_cells = set()
        self.start_time = None
        self.game_active = True
        self.question = ""  # IT otázka
        self.correct_answer = ""  # Správná odpověď na otázku
        
    def reset(self):
        self.__init__()
        

class ImageProcessor:
    """Zpracování a dělení obrázku na mřížku"""
    def __init__(self, image_path, grid_size=4):
        self.image_path = image_path
        self.grid_size = grid_size
        self.tiles = []
        self.original_image = None
        self.load_and_process_image()
        
    def load_and_process_image(self):
        """Načtení a zpracování obrázku"""
        try:
            self.original_image = Image.open(self.image_path)
            # Změna velikosti na čtvercový obrázek
            size = 400
            self.original_image = self.original_image.resize((size, size), Image.Resampling.LANCZOS)
            self.tiles = self.divide_image()
        except Exception as e:
            raise Exception(f"Chyba při načítání obrázku: {e}")
    
    def divide_image(self):
        """Rozdělení obrázku na mřížku"""
        tiles = []
        tile_size = self.original_image.width // self.grid_size
        
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                left = col * tile_size
                top = row * tile_size
                right = left + tile_size
                bottom = top + tile_size
                
                tile = self.original_image.crop((left, top, right, bottom))
                tiles.append(tile)
        
        return tiles
    
    def get_tile(self, index):
        """Vrátí tile obrázku"""
        if 0 <= index < len(self.tiles):
            return self.tiles[index]
        return None
    
    def get_full_image_photo(self):
        """Vrátí celý obrázek jako PhotoImage"""
        return ImageTk.PhotoImage(self.original_image)


class QuizApplication:
    """Hlavní aplikace hry"""
    def __init__(self, root):
        self.root = root
        self.root.title("Pexeso - Soutěžní hra")
        self.root.geometry("1000x800")
        self.root.config(bg=COLORS["bg_main"])
        
        self.game_state = GameState()
        self.image_processor = None
        self.photo_tiles = {}
        self.questions_data = {}  # Načtené otázky z JSON
        self.current_question_data = None  # Aktuální otázka a odpověď
        
        # UI prvky
        self.timer_label = None
        self.points_label = None
        self.grid_buttons = []
        self.letter_labels = []
        self.letter_buttons = []
        self.answer_entry = None
        self.info_label = None
        self.last_move_label = None
        self.hint_info_label = None
        self.question_label = None  # Label pro otázku
        
        self.setup_ui()
        self.load_questions()
        self.load_image()
        self.update_timer()
        
    def setup_ui(self):
        """Vytvoření uživatelského rozhraní"""
        # Horní panel s información
        top_panel = tk.Frame(self.root, bg=COLORS["bg_light"], height=100)
        top_panel.pack(fill=tk.X, padx=10, pady=10)
        top_panel.pack_propagate(False)
        
        # Levá část top panelu
        left_top = tk.Frame(top_panel, bg=COLORS["bg_light"])
        left_top.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Body - velký nadpis
        self.points_label = tk.Label(
            left_top,
            text=f"Body: {self.game_state.points}",
            font=FONTS["large"],
            bg=COLORS["bg_light"],
            fg=COLORS["points_color"]
        )
        self.points_label.pack(side=tk.LEFT, padx=20)
        
        # Nápověda info
        self.hint_info_label = tk.Label(
            left_top,
            text="Nápověda",
            font=FONTS["medium"],
            bg=COLORS["bg_light"],
            fg=COLORS["fg_text"]
        )
        self.hint_info_label.pack(side=tk.LEFT, padx=40)
        
        # Poslední tah info
        self.last_move_label = tk.Label(
            left_top,
            text="Poslední tah: -",
            font=FONTS["medium"],
            bg=COLORS["bg_light"],
            fg=COLORS["fg_text"]
        )
        self.last_move_label.pack(side=tk.LEFT, padx=40)
        
        # Čas - vpravo
        self.timer_label = tk.Label(
            left_top,
            text="Čas: 10:00",
            font=FONTS["large"],
            bg=COLORS["bg_light"],
            fg=COLORS["error_color"]
        )
        self.timer_label.pack(side=tk.RIGHT, padx=20)
        
        # Střední frame - Obrázek + Mřížka
        middle_frame = tk.Frame(self.root, bg=COLORS["bg_main"])
        middle_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Mřížka tlačítek pro obrázek
        grid_frame = tk.Frame(middle_frame, bg=COLORS["bg_main"])
        grid_frame.pack(side=tk.LEFT, padx=10)
        
        self.grid_buttons = []
        for i in range(self.game_state.grid_size):
            row_buttons = []
            for j in range(self.game_state.grid_size):
                btn = tk.Button(
                    grid_frame,
                    width=12,
                    height=6,
                    font=FONTS["small"],
                    bg=COLORS["button_bg"],
                    fg=COLORS["fg_text"],
                    activebackground=COLORS["button_hover"],
                    relief=tk.RAISED,
                    bd=2
                )
                cell_index = i * self.game_state.grid_size + j
                btn.config(command=lambda idx=cell_index: self.reveal_cell(idx))
                btn.grid(row=i, column=j, padx=2, pady=2)
                row_buttons.append(btn)
            self.grid_buttons.append(row_buttons)
        
        # Pravý panel - Info
        right_frame = tk.Frame(middle_frame, bg=COLORS["bg_main"])
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)
        
        # Otázka
        tk.Label(
            right_frame,
            text="OTÁZKA:",
            font=FONTS["medium"],
            bg=COLORS["bg_main"],
            fg=COLORS["points_color"]
        ).pack(pady=(20, 5))
        
        # Label pro otázku
        self.question_label = tk.Label(
            right_frame,
            text="Čekám na otázku...",
            font=FONTS["medium"],
            bg=COLORS["bg_main"],
            fg=COLORS["fg_text"],
            justify=tk.LEFT,
            wraplength=280
        )
        self.question_label.pack(pady=20)
        
        # Info text
        self.info_label = tk.Label(
            right_frame,
            text="Vybírej políčka a odhaluj obrázek!\n\nKdyž si myslíš, že víš odpověď,\nvstup ji do pole níže.",
            font=FONTS["small"],
            bg=COLORS["bg_main"],
            fg=COLORS["fg_text"],
            justify=tk.LEFT,
            wraplength=280
        )
        self.info_label.pack(pady=10)
        
        # Dolní panel - Odpověď
        bottom_panel = tk.Frame(self.root, bg=COLORS["bg_light"])
        bottom_panel.pack(fill=tk.X, padx=10, pady=10)
        
        # Frame pro vstup odpovědi
        answer_frame = tk.Frame(bottom_panel, bg=COLORS["bg_light"])
        answer_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(
            answer_frame,
            text="Zadej odpověď na otázku:",
            font=FONTS["medium"],
            bg=COLORS["bg_light"],
            fg=COLORS["fg_text"]
        ).pack(side=tk.LEFT, padx=10)
        
        self.answer_entry = tk.Entry(
            answer_frame,
            font=FONTS["medium"],
            width=30,
            bg=COLORS["bg_light"],
            fg=COLORS["fg_text"],
            insertbackground=COLORS["fg_text"]
        )
        self.answer_entry.pack(side=tk.LEFT, padx=10)
        self.answer_entry.bind("<Return>", lambda e: self.submit_answer())
        
        submit_btn = tk.Button(
            answer_frame,
            text="Odeslat",
            font=FONTS["medium"],
            bg=COLORS["button_bg"],
            fg=COLORS["fg_text"],
            activebackground=COLORS["button_hover"],
            command=self.submit_answer,
            padx=20
        )
        submit_btn.pack(side=tk.LEFT, padx=10)
        
        # Tlačítko pro načtení nového obrázku
        load_btn = tk.Button(
            answer_frame,
            text="Načíst obrázek",
            font=FONTS["small"],
            bg=COLORS["button_bg"],
            fg=COLORS["fg_text"],
            activebackground=COLORS["button_hover"],
            command=self.load_image,
            padx=15
        )
        load_btn.pack(side=tk.RIGHT, padx=10)
    
    def load_questions(self):
        """Načtení otázek z JSON souboru"""
        try:
            with open("questions.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                # Indexování otázek podle jména obrázku
                self.questions_data = {q["image"]: q for q in data.get("questions", [])}
        except FileNotFoundError:
            messagebox.showwarning("Pozor", "Soubor questions.json nebyl nalezen!")
        except json.JSONDecodeError:
            messagebox.showerror("Chyba", "Chyba při čtení questions.json!")
    
    def load_image(self):
        """Načtení obrázku ze souboru"""
        if not os.path.exists("assets"):
            os.makedirs("assets")
        
        file_path = filedialog.askopenfilename(
            title="Vyber obrázek",
            initialdir="assets",
            filetypes=[("Obrázky", "*.png *.jpg *.jpeg *.bmp"), ("Všechny soubory", "*.*")]
        )
        
        if file_path:
            try:
                self.image_processor = ImageProcessor(file_path, self.game_state.grid_size)
                self.game_state.reset()
                
                # Získání otázky z JSON na základě názvu souboru
                image_name = os.path.basename(file_path)
                if image_name in self.questions_data:
                    self.current_question_data = self.questions_data[image_name]
                    self.game_state.question = self.current_question_data["question"]
                    self.game_state.correct_answer = self.current_question_data["answer"]
                    # Aktualizace otázky v UI
                    self.question_label.config(text=self.game_state.question)
                else:
                    # Fallback - ručně zadat otázku
                    dialog = tk.simpledialog.askstring(
                        "Otázka",
                        "Jaká je otázka k tomuto obrázku?"
                    )
                    if dialog:
                        answer_dialog = tk.simpledialog.askstring(
                            "Odpověď",
                            "Jaká je správná odpověď?"
                        )
                        if answer_dialog:
                            self.game_state.question = dialog
                            self.game_state.correct_answer = answer_dialog.upper()
                            self.question_label.config(text=self.game_state.question)
                
                self.update_ui()
                messagebox.showinfo("Úspěch", "Obrázek a otázka byly načteny. Hra začíná!")
            except Exception as e:
                messagebox.showerror("Chyba", str(e))
    
    def reveal_cell(self, index):
        """Odhalení políčka"""
        if not self.game_state.game_active or index in self.game_state.revealed_cells:
            return
        
        self.game_state.revealed_cells.add(index)
        
        # Výpočet ceny
        revealed_count = len(self.game_state.revealed_cells)
        cost = get_reveal_cost(revealed_count - 1)
        self.game_state.points += cost
        
        # Aktualizace info o posledním tahu
        self.last_move_label.config(text=f"Poslední tah: {cost} bodů")
        
        # Zobrazení obrázku
        self.update_ui()
        
        # Kontrola, zda je vše odhaleno
        if len(self.game_state.revealed_cells) == self.game_state.total_cells:
            self.show_full_image()
    
    def update_ui(self):
        """Aktualizace uživatelského rozhraní"""
        # Aktualizace bodů
        self.points_label.config(text=f"Body: {self.game_state.points}")
        
        # Aktualizace tlačítek
        for i in range(self.game_state.grid_size):
            for j in range(self.game_state.grid_size):
                cell_index = i * self.game_state.grid_size + j
                btn = self.grid_buttons[i][j]
                
                if cell_index in self.game_state.revealed_cells:
                    # Zobrazení části obrázku
                    if cell_index not in self.photo_tiles:
                        tile = self.image_processor.get_tile(cell_index)
                        self.photo_tiles[cell_index] = ImageTk.PhotoImage(tile)
                    
                    btn.config(
                        image=self.photo_tiles[cell_index],
                        text="",
                        state=tk.DISABLED,
                        bg=COLORS["bg_light"]
                    )
                    btn.image = self.photo_tiles[cell_index]
                else:
                    btn.config(
                        text="?",
                        state=tk.NORMAL,
                        image=""
                    )
    
    def submit_answer(self):
        """Odeslání odpovědi na otázku"""
        if not self.game_state.game_active:
            return
        
        answer = self.answer_entry.get().upper().strip()
        
        if not answer:
            messagebox.showwarning("Pozor", "Zadej odpověď!")
            return
        
        self.answer_entry.delete(0, tk.END)
        
        if answer == self.game_state.correct_answer:
            messagebox.showinfo(
                "Správně!",
                f"Správná odpověď: {self.game_state.correct_answer}\nZískané body: {self.game_state.points}"
            )
            self.game_state.game_active = False
        else:
            penalty = GAME_CONFIG["wrong_answer_penalty"]
            self.game_state.points -= penalty
            self.points_label.config(text=f"Body: {self.game_state.points}")
            messagebox.showerror(
                "Špatně",
                f"Nesprávná odpověď!\nZtráta {penalty} bodů\nZbývá: {self.game_state.points} bodů"
            )
    
    def show_full_image(self):
        """Zobrazení celého obrázku"""
        messagebox.showinfo(
            "Všechna políčka odhalena!",
            "Odhalil jsi celý obrázek.\nTeď jde o správné uhádnutí tajenky!"
        )
    
    def update_timer(self):
        """Aktualizace časovače"""
        if not self.game_state.game_active:
            return
        
        if self.game_state.start_time is None:
            self.game_state.start_time = time.time()
        
        elapsed = int(time.time() - self.game_state.start_time)
        remaining = GAME_CONFIG["game_time_seconds"] - elapsed
        
        if remaining <= 0:
            self.game_state.game_active = False
            messagebox.showinfo(
                "Čas vypršel!",
                f"Hra skončila!\nFinální skóre: {self.game_state.points} bodů"
            )
            return
        
        minutes = remaining // 60
        seconds = remaining % 60
        self.timer_label.config(text=f"Čas: {minutes:02d}:{seconds:02d}")
        
        # Aktualizace každou sekundu
        self.root.after(1000, self.update_timer)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApplication(root)
    root.mainloop()
