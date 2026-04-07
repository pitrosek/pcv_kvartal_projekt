import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from PIL import Image, ImageTk
import os
import time
import json
from config.game_config import GAME_CONFIG, COLORS, FONTS

# Konstanta pro body za politčko
CELL_BASE_POINTS = 8
CELL_SECOND_ATTEMPT_PERCENT = 0.2  # 20% při druhém a další pokusu


class GameState:
    """Správa stavu hry"""
    def __init__(self):
        self.points = GAME_CONFIG["starting_points"]
        self.grid_size = GAME_CONFIG["grid_size"]
        self.total_cells = self.grid_size ** 2
        self.revealed_cells = set()  # Odhalená politčka
        self.cell_attempts = {}  # Počet pokusů na politčko {index: attempts}
        self.start_time = None
        self.game_active = True
        
    def reset(self):
        self.__init__()
    
    def get_cell_points(self, cell_index):
        """Vrací body za politčko podle počtu pokusů"""
        attempts = self.cell_attempts.get(cell_index, 0)
        if attempts == 1:  # První pokus → 100%
            return CELL_BASE_POINTS
        else:  # Druhý a další pokus → 20%
            return int(CELL_BASE_POINTS * CELL_SECOND_ATTEMPT_PERCENT)


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


class QuizApplication:
    """Hlavní aplikace hry"""
    def __init__(self, root):
        self.root = root
        self.root.title("Pexeso - IT Soutěžní Hra")
        self.root.geometry("900x800")
        self.root.config(bg=COLORS["bg_main"])
        
        self.game_state = GameState()
        self.image_processor = None
        self.photo_tiles = {}
        self.questions = []  # Všechny otázky
        self.dialog_open = False  # Flag, aby se zabránil více dialogům
        self.current_image_index = 0  # Index aktuálního obrázku
        
        # UI prvky
        self.timer_label = None
        self.points_label = None
        self.grid_buttons = []
        self.guess_button = None  # Tlačítko na hádam finálního obrázku
        self.guess_frame = None
        self.answer_entry = None
        
        self.setup_ui()
        self.load_questions()
        self.load_first_image()  # Načti první obrázek automaticky
        self.update_timer()
        
    def setup_ui(self):
        """Vytvoření uživatelského rozhraní"""
        # Horní panel
        top_panel = tk.Frame(self.root, bg=COLORS["bg_light"], height=80)
        top_panel.pack(fill=tk.X, padx=10, pady=10)
        top_panel.pack_propagate(False)
        
        # Body - vlevo
        self.points_label = tk.Label(
            top_panel,
            text=f"Body: {self.game_state.points}",
            font=FONTS["large"],
            bg=COLORS["bg_light"],
            fg=COLORS["points_color"]
        )
        self.points_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        # Čas - vpravo
        self.timer_label = tk.Label(
            top_panel,
            text="Čas: 10:00",
            font=FONTS["large"],
            bg=COLORS["bg_light"],
            fg=COLORS["error_color"]
        )
        self.timer_label.pack(side=tk.RIGHT, padx=20, pady=10)
        
        # Info - uprostřed
        info_label = tk.Label(
            top_panel,
            text="Klikni na políčko → odpověz na otázku → vyhraji body!",
            font=FONTS["medium"],
            bg=COLORS["bg_light"],
            fg=COLORS["fg_text"]
        )
        info_label.pack(side=tk.LEFT, expand=True)
        
        # Střední frame - Mřížka obrázku
        middle_frame = tk.Frame(self.root, bg=COLORS["bg_main"])
        middle_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Mřížka tlačítek pro obrázek
        grid_frame = tk.Frame(middle_frame, bg=COLORS["bg_main"])
        grid_frame.pack(expand=True)
        
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
                btn.config(command=lambda idx=cell_index: self.on_cell_click(idx))
                btn.grid(row=i, column=j, padx=3, pady=3)
                row_buttons.append(btn)
            self.grid_buttons.append(row_buttons)
        
        # Frame pro guess tlačítko - pod mřížkou
        self.guess_frame = tk.Frame(middle_frame, bg=COLORS["bg_main"])
        self.guess_frame.pack(pady=10)
        
        self.guess_button = tk.Button(
            self.guess_frame,
            text="Hádat celý obrázek",
            font=FONTS["medium"],
            bg=COLORS["button_bg"],
            fg=COLORS["fg_text"],
            activebackground=COLORS["button_hover"],
            command=self.show_guess_image_dialog_final
        )
        self.guess_button.pack(padx=10, pady=10)
        
        # Dolní panel - Tlačítka
        bottom_panel = tk.Frame(self.root, bg=COLORS["bg_light"])
        bottom_panel.pack(fill=tk.X, padx=10, pady=10)
        
        load_btn = tk.Button(
            bottom_panel,
            text="Další Obrázek",
            font=FONTS["medium"],
            bg=COLORS["button_bg"],
            fg=COLORS["fg_text"],
            activebackground=COLORS["button_hover"],
            command=self.load_next_image
        )
        load_btn.pack(side=tk.LEFT, padx=10, pady=10)
    
    def load_questions(self):
        """Načtení otázek z JSON souboru"""
        try:
            with open("questions.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                all_questions = data.get("questions", [])
                if len(all_questions) < 16:
                    messagebox.showwarning("Pozor", f"V questions.json je jen {len(all_questions)} otázek, potřeba alespoň 64!")
        except FileNotFoundError:
            messagebox.showerror("Chyba", "Soubor questions.json nebyl nalezen!")
        except json.JSONDecodeError:
            messagebox.showerror("Chyba", "Chyba při čtení questions.json!")
    
    def update_questions_for_image(self):
        """Aktualizace otázek pro aktuální obrázek"""
        try:
            with open("questions.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                all_questions = data.get("questions", [])
                # Filtruj otázky pro aktuální obrázek podle image_id
                self.questions = [q for q in all_questions if q.get("image_id") == self.current_image_index]
                if len(self.questions) < 16:
                    messagebox.showwarning("Pozor", f"Pro obrázek {self.current_image_index + 1} je jen {len(self.questions)} otázek, potřeba 16!")
        except Exception as e:
            messagebox.showerror("Chyba", f"Chyba při načítání otázek: {e}")
    
    def load_first_image(self):
        """Načtení prvního obrázku ze seznamu"""
        self.current_image_index = 0
        self.update_questions_for_image()
        self.load_current_image()
    
    def load_next_image(self):
        """Načtení dalšího obrázku ze seznamu"""
        images = GAME_CONFIG.get("images", [])
        if self.current_image_index < len(images) - 1:
            self.current_image_index += 1
            self.update_questions_for_image()
            self.load_current_image()
        else:
            messagebox.showinfo("Info", "To byl poslední obrázek!")
    
    def load_current_image(self):
        """Načtení aktuálního obrázku z cesty v konfigu"""
        images = GAME_CONFIG.get("images", [])
        if self.current_image_index < len(images):
            file_path = images[self.current_image_index]
            if os.path.exists(file_path):
                try:
                    self.image_processor = ImageProcessor(file_path, self.game_state.grid_size)
                    self.game_state.reset()
                    self.photo_tiles = {}
                    self.update_ui()
                    messagebox.showinfo(
                        "Úspěch",
                        f"Obrázek {self.current_image_index + 1}/{len(images)} načten!\n\n"
                        "Klikej na políčka a odpovídej na IT otázky.\n"
                        "Správně odpověz NA OTÁZKU a HAD CO VIDÍŠ NA OBRÁZKU.\n"
                        "Prvního správná odpověď = 100% bodů\n"
                        "Druhou správná odpověď = 20% bodů"
                    )
                except Exception as e:
                    messagebox.showerror("Chyba", f"Chyba při načítání obrázku: {e}")
            else:
                messagebox.showerror("Chyba", f"Obrázek nenalezen: {file_path}")
        else:
            messagebox.showerror("Chyba", "Žádný obrázek k dispozici!")
    
    def on_cell_click(self, cell_index):
        """Při kliknutí na políčko"""
        # Kontrola, zda je políčko již odhaleno
        if cell_index in self.game_state.revealed_cells:
            return
        
        # Kontrola, zda je hra aktivní
        if not self.game_state.game_active:
            return
        
        # Kontrola, aby se dialog neotevíral vícekrát
        if self.dialog_open:
            return
        
        # Zavolej dialog s otázkou
        self.show_question_dialog(cell_index)
    
    def show_question_dialog(self, cell_index):
        """Zobrazí dialog s otázkou"""
        self.dialog_open = True
        
        # Zjisti otázku
        if cell_index < len(self.questions):
            question_data = self.questions[cell_index]
            question = question_data.get("question", "Neznámá otázka")
            correct_answer = question_data.get("answer", "").upper()
        else:
            messagebox.showerror("Chyba", "Otázka pro toto políčko nebyla nalezena!")
            self.dialog_open = False
            return
        
        # Inicializuj pokus
        if cell_index not in self.game_state.cell_attempts:
            self.game_state.cell_attempts[cell_index] = 0
        
        # Dialog pro odpověď
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Otázka na políčko {cell_index + 1}")
        dialog.geometry("500x300")
        dialog.config(bg=COLORS["bg_light"])
        dialog.resizable(False, False)
        
        # Otázka
        tk.Label(
            dialog,
            text=question,
            font=FONTS["medium"],
            bg=COLORS["bg_light"],
            fg=COLORS["fg_text"],
            wraplength=450,
            justify=tk.CENTER
        ).pack(pady=20, padx=10)
        
        # Počet znaků v odpovědi
        char_count_label = tk.Label(
            dialog,
            text=f"📋 Počet znaků: {len(correct_answer)}",
            font=FONTS["small"],
            bg=COLORS["bg_light"],
            fg=COLORS["points_color"]
        )
        char_count_label.pack(pady=5)
        
        # Input field pro otázku
        entry_question = tk.Entry(
            dialog,
            font=FONTS["medium"],
            width=40
        )
        entry_question.pack(pady=15)
        entry_question.focus()
        
        # Čítač pokusů
        attempt_label = tk.Label(
            dialog,
            text="",
            font=FONTS["small"],
            bg=COLORS["bg_light"],
            fg=COLORS["points_color"]
        )
        attempt_label.pack(pady=5)
        
        # Funkcí pro kontrolu odpovědi
        def check_answer():
            user_answer_question = entry_question.get().upper().strip()
            
            if not user_answer_question:
                messagebox.showwarning("Pozor", "Zadej odpověď!")
                return
            
            self.game_state.cell_attempts[cell_index] += 1
            attempts = self.game_state.cell_attempts[cell_index]
            
            # Kontrola odpovědi na otázku
            question_correct = user_answer_question == correct_answer
            
            if question_correct:
                # SPRÁVNÁ ODPOVĚĎ
                points = self.game_state.get_cell_points(cell_index)
                self.game_state.points += points
                self.game_state.revealed_cells.add(cell_index)
                
                # Zpráva
                attempt_text = "1. pokus" if attempts == 1 else f"{attempts}. pokus"
                percent = "100%" if attempts == 1 else "20%"
                msg = (
                    f"✓ Správně!\n\n"
                    f"Odpověď: {correct_answer}\n\n"
                    f"{attempt_text} → +{points} bodů ({percent})\n"
                    f"Celkem: {self.game_state.points} bodů"
                )
                
                # Aktualizuj UI IHNED
                self.update_ui()
                
                # Zavři dialog
                dialog.destroy()
                self.dialog_open = False
                
                # Pak zobraz zprávu
                messagebox.showinfo("Správně! ✓", msg)
                
                # Kontrola, zda jsou všechna política odhalena
                if len(self.game_state.revealed_cells) == self.game_state.total_cells:
                    messagebox.showinfo(
                        "Gratuluji!",
                        f"Odhalil jsi celý obrázek!\n\nFinální skóre: {self.game_state.points} bodů"
                    )
                    self.game_state.game_active = False
            else:
                # ŠPATNÁ ODPOVĚĎ
                penalty = 20
                self.game_state.points -= penalty
                
                # Aktualizuj body v hlavním okně
                self.points_label.config(text=f"Body: {self.game_state.points}")
                
                # Feedback
                attempt_label.config(
                    text=f"Pokus číslo {attempts} → Špatně! -20 bodů\nSpráva odpověď: {correct_answer}\nZbývá: {self.game_state.points} bodů\n\nZkus to znovu...",
                    fg=COLORS["error_color"]
                )
                entry_question.delete(0, tk.END)
                entry_question.focus()
        
        # Tlačítko Odeslat
        tk.Button(
            dialog,
            text="Odeslat",
            font=FONTS["medium"],
            bg=COLORS["button_bg"],
            fg=COLORS["fg_text"],
            command=check_answer,
            padx=30
        ).pack(pady=15)
        
        # Pokud je Enter, odešli odpověď
        entry_question.bind("<Return>", lambda e: check_answer())
        
        # Při zavření okna
        def on_close():
            dialog.destroy()
            self.dialog_open = False
        
        dialog.protocol("WM_DELETE_WINDOW", on_close)
        dialog.transient(self.root)
    
    def show_guess_image_dialog_final(self):
        """Zobrazí dialog na hádam finálního obrázku"""
        self.dialog_open = True
        
        # Zjisti správnou odpověď pro aktuální obrázek
        all_answers = ["BILL GATES", "MARK ZUCKERBERG", "CHATGPT", "GRAFICKA KARTA"]
        correct_answer = all_answers[self.current_image_index] if self.current_image_index < len(all_answers) else ""
        
        # Dialog pro hádam
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Hádat obrázek #{self.current_image_index + 1}")
        dialog.geometry("500x450")
        dialog.config(bg=COLORS["bg_light"])
        dialog.resizable(False, False)
        
        # Label
        tk.Label(
            dialog,
            text="Co vidíš na obrázku?\n(Vidíš jen odhalená políčka)",
            font=FONTS["medium"],
            bg=COLORS["bg_light"],
            fg=COLORS["fg_text"]
        ).pack(pady=15)
        
        # Frame na náhled - jen odhalená políčka
        image_frame = tk.Frame(dialog, bg=COLORS["bg_main"], relief=tk.SUNKEN, bd=2)
        image_frame.pack(pady=10)
        
        # Vykresli jen odhalená políčka
        tiles_frame = tk.Frame(image_frame, bg=COLORS["bg_main"])
        tiles_frame.pack(padx=5, pady=5)
        
        if self.image_processor:
            for i in range(self.game_state.grid_size):
                for j in range(self.game_state.grid_size):
                    cell_index = i * self.game_state.grid_size + j
                    
                    if cell_index in self.game_state.revealed_cells:
                        # Zobraz odhalené politčko
                        tile = self.image_processor.get_tile(cell_index)
                        if tile:
                            resized_tile = tile.resize((70, 70), Image.Resampling.LANCZOS)
                            photo = ImageTk.PhotoImage(resized_tile)
                            label = tk.Label(tiles_frame, image=photo, bg=COLORS["bg_main"])
                            label.image = photo
                            label.grid(row=i, column=j, padx=2, pady=2)
                    else:
                        # Prázdné místo za neodhalené politčko
                        empty_label = tk.Label(
                            tiles_frame,
                            text="?",
                            width=8,
                            height=3,
                            bg=COLORS["button_bg"],
                            fg=COLORS["fg_text"],
                            font=FONTS["small"]
                        )
                        empty_label.grid(row=i, column=j, padx=2, pady=2)
        
        # Label s počtem odhalených
        revealed_count = len(self.game_state.revealed_cells)
        total_count = self.game_state.total_cells
        info_label = tk.Label(
            dialog,
            text=f"Odhaleno {revealed_count}/{total_count} politček",
            font=FONTS["small"],
            bg=COLORS["bg_light"],
            fg=COLORS["points_color"]
        )
        info_label.pack(pady=5)
        
        # Input field
        entry = tk.Entry(
            dialog,
            font=FONTS["medium"],
            width=40
        )
        entry.pack(pady=15)
        entry.focus()
        
        # Feedback label
        feedback_label = tk.Label(
            dialog,
            text="",
            font=FONTS["small"],
            bg=COLORS["bg_light"],
            fg=COLORS["points_color"]
        )
        feedback_label.pack(pady=5)
        
        # Funkcí pro kontrolu odpovědi
        def check_final_guess():
            user_answer = entry.get().upper().strip()
            
            if not user_answer:
                messagebox.showwarning("Pozor", "Zadej odpověď!")
                return
            
            # Kontrola s částečnou shodou
            if user_answer in correct_answer or correct_answer in user_answer:
                # SPRÁVNÉ HÁDAM
                msg = (
                    f"✓ Správně!\n\n"
                    f"Obrázek: {correct_answer}\n\n"
                    f"Gratuluji za správné hádání!"
                )
                
                # Zavři dialog
                dialog.destroy()
                self.dialog_open = False
                
                # Zpráva
                messagebox.showinfo("Správně! ✓", msg)
                
                # Přesun na další obrázek
                self.load_next_image()
            else:
                # ŠPATNÉ HÁDAM
                feedback_label.config(
                    text=f"Nesprávně! Zkus znovu...",
                    fg=COLORS["error_color"]
                )
                entry.delete(0, tk.END)
                entry.focus()
        
        # Tlačítko Hádat
        tk.Button(
            dialog,
            text="Hádat",
            font=FONTS["medium"],
            bg=COLORS["button_bg"],
            fg=COLORS["fg_text"],
            command=check_final_guess,
            padx=30
        ).pack(pady=10)
        
        # Enter
        entry.bind("<Return>", lambda e: check_final_guess())
        
        # Při zavření okna
        def on_close():
            dialog.destroy()
            self.dialog_open = False
        
        dialog.protocol("WM_DELETE_WINDOW", on_close)
        dialog.transient(self.root)
    
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
                    if self.image_processor:
                        tile = self.image_processor.get_tile(cell_index)
                        if tile:
                            resized_tile = tile.resize((140, 140), Image.Resampling.LANCZOS)
                            photo = ImageTk.PhotoImage(resized_tile)
                            self.photo_tiles[cell_index] = photo
                            
                            btn.config(
                                image=photo,
                                text="",
                                state=tk.DISABLED,
                                bg=COLORS["bg_light"],
                                relief=tk.SUNKEN,
                                width=0,
                                height=0
                            )
                            btn.image = photo
                else:
                    btn.config(
                        text="?",
                        state=tk.NORMAL,
                        image="",
                        relief=tk.RAISED,
                        width=12,
                        height=6
                    )
        
        # Tlačítko "Hádat" je vždy aktivní
        self.guess_button.config(state=tk.NORMAL)
        
        # Vynutí refresh UI
        self.root.update_idletasks()
    
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
                f"Hra skončila!\n\nFinální skóre: {self.game_state.points} bodů"
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
