# Konfigurace hry

# Herní parametry
GAME_CONFIG = {
    "starting_points": 120,  # Počáteční body
    "grid_size": 4,  # 4x4 grid
    "game_time_seconds": 600,  # 10 minut (600 sekund)
    "wrong_answer_penalty": 20,  # Trest za špatnou odpověď
}

# Cena za odhalení políček
def get_reveal_cost(cell_number):
    """
    Vrací cenu za odhalení políčka
    Prvního políčka je zdarma (0 bodů), ostatní podle čísla
    """
    if cell_number == 0:
        return 0
    return -(cell_number - 1)

# Cena za odhalení písmene
def get_letter_hint_cost(letter_number):
    """
    Vrací cenu za odhalení písmene tajenky
    """
    if letter_number == 0:
        return 0
    return -(letter_number - 1)

# Barvový motiv
COLORS = {
    "bg_main": "#2C3E50",
    "bg_light": "#34495E",
    "fg_text": "#ECF0F1",
    "button_bg": "#3498DB",
    "button_hover": "#2980B9",
    "points_color": "#F39C12",
    "error_color": "#E74C3C",
    "success_color": "#27AE60",
}

# Fonty
FONTS = {
    "title": ("Arial", 28, "bold"),
    "large": ("Arial", 20, "bold"),
    "medium": ("Arial", 14, "normal"),
    "small": ("Arial", 10, "normal"),
}
