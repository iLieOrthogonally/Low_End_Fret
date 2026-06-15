import tkinter as tk
from tkinter import ttk

# CONSTANTS

# The 12 standard notes in an octave indicated with sharps and not flats, but this is adjusted later
MUSIC_NOTES = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']

# Scale and chord formulas (steps from the root note)
FORMULAS = {
    'Major': [0, 2, 4, 5, 7, 9, 11],
    'Minor': [0, 2, 3, 5, 7, 8, 10],
    'Major Triad': [0, 4, 7],
    'Minor Triad': [0, 3, 7],
    'Major Pentatonic': [0, 2, 4, 7, 9],
    'Minor Pentatonic': [0, 3, 5, 7, 10]
}

# Standard 4-string bass starting notes using absolute semitones (C0 = 0, C1 = 12, C2 = 24, etc). 
# Lowest note on a Bass Guitar is E1 (4 semitones away from C1: 16)
BASS_STRINGS = {
    'E': 16,
    'A': 21,
    'D': 26,
    'G': 31
}

# Simple Unified Colors
ROOT_COLOR = "red2"         # Bright Red for the Root Note
SCALE_NOTE_COLOR = "green4"   # Darker Green for all other notes in the scale

# FUNCTIONS 

def calculate_scale_notes(root, formula_name):
    """Finds the names of the notes that are in the chosen scale/chord."""
    root_index = MUSIC_NOTES.index(root)
    intervals = FORMULAS[formula_name]
    
    scale_notes = []
    for interval in intervals:
        note_index = (root_index + interval) % 12
        scale_notes.append(MUSIC_NOTES[note_index])
        
    return scale_notes


# Drawing the rectangles and fretboard

def draw_fretboard():
    """Creates the GUI window, buttons for user input, and draws the bass fretboard."""
    window = tk.Tk()
    window.title("Bass Fretboard Visualizer")

    # Create a Control Frame panel for the dropdown menus
    control_frame = tk.Frame(window, bg="#1e1e1e")
    control_frame.pack(fill="x", pady=5)
    
    # Setup Root Note Dropdown Menu
    tk.Label(control_frame, text="Root Note:", fg="white", bg="#1e1e1e", font=("Arial", 10, "bold")).pack(side="left", padx=(20, 5))
    root_dropdown = ttk.Combobox(control_frame, values=MUSIC_NOTES, width=7, state="readonly")
    root_dropdown.set("C")  # Default starting note
    root_dropdown.pack(side="left", padx=5)
    
    # Setup Scale/Triad Dropdown Menu
    tk.Label(control_frame, text="Scale/Triad:", fg="white", bg="#1e1e1e", font=("Arial", 10, "bold")).pack(side="left", padx=(20, 5))
    formula_dropdown = ttk.Combobox(control_frame, values=list(FORMULAS.keys()), width=16, state="readonly")
    formula_dropdown.set("Major")  # Default starting formula
    formula_dropdown.pack(side="left", padx=5)
    
    # Create the canvas big enough to show 13 different positions for each of the 4 strings
    # The 13 different positions are the open string plus 12 frets
    width = 940
    height = 520
    canvas = tk.Canvas(window, width=width, height=height, bg="#1e1e1e")
    canvas.pack()
    
    # Create a background color to differentiate fretboard from open strings
    canvas.create_rectangle(80, 90, 880, 330, fill="saddle brown", outline="#2d1a12", width=3)
    
    # Draw the 12 frets and add the fret numbers below them
    fret_spacing = 800 / 12
    for i in range(13):
        x = 80 + (i * fret_spacing)
        # Fret lines should go all the way down the neck of the bass
        canvas.create_line(x, 90, x, 330, fill="blanched almond", width=2)
        
        if i > 0:
            fret_x = x - (fret_spacing / 2)
            canvas.create_text(fret_x, 400, text=str(i), fill="blanched almond", font=("Arial", 12, "bold", "underline"))

    # The order we want to draw strings on the screen (highest string on top)
    string_order = ['G', 'D', 'A', 'E']
    string_spacing = 240 / 3
    
    for index, string_name in enumerate(string_order):
        # Calculate Y location for the strings
        y = 90 + (index * string_spacing)
        
        # Draw the string lines in silver
        canvas.create_line(70, y, 890, y, fill="#cfd8dc", width=2 + (index * 0.5))

        # Label the open string letter on the left side
        canvas.create_text(45, y, text=string_name, fill="white", font=("Arial", 12, "bold"))

    # Label the Open String
    canvas.create_text(45, 400, text="Open", fill="blanched almond", font=("Arial", 11, "underline"))
        
    # Label the different circles for root vs note in scale
    legend_text = "● Red Circle = Root Note    ● Green Circle = Notes in Scale"
    canvas.create_text(470, 455, text=legend_text, fill="#b0bec5", font=("Arial", 9))

    # Label the different fretboard locations
    legend_text = "*Underlined numbers indicate the Open String and 12 Frets"
    canvas.create_text(470, 475, text=legend_text, fill="#b0bec5", font=("Arial", 9))
        


 # Allow for new selections by user
    def clear_fretboard(event=None):
        """Wipes and rewrites all dynamic note circles."""
        # Clear previous notes
        canvas.delete("dynamic_notes")
        
        # Use the selections from the interactive buttons
        root_note = root_dropdown.get()
        formula_name = formula_dropdown.get()
        scale_notes = calculate_scale_notes(root_note, formula_name)
        
        # Redraw the dynamic main title text
        title_text = "Showing Fretboard Positions for " + root_note + " " + formula_name.upper()
        canvas.create_text(470, 35, text=title_text, fill="white", font=("Arial", 14, "bold"), tags="dynamic_notes")

        # Change legend depending on whether user chooses a scale or triad
        if formula_name in ("Major Triad", "Minor Triad"):
            legend_text_triad = "*Grey numbers underneath circled notes show location in triad"
            canvas.create_text(470, 495, text=legend_text_triad, fill="#b0bec5", font=("Arial", 9, "bold"), tags="dynamic_notes")
        else:
            legend_text_scale = "*Grey numbers underneath circled notes show location in scale"
            canvas.create_text(470, 495, text=legend_text_scale, fill="#b0bec5", font=("Arial", 9, "bold"), tags="dynamic_notes")


        # Draw notes mapping loops
        for index, string_name in enumerate(string_order):
            y = 90 + (index * string_spacing)
            open_note = BASS_STRINGS[string_name]
            
            for fret in range(13):
                abs_pitch = open_note + fret
                note_name = MUSIC_NOTES[abs_pitch % 12]
                
                if note_name in scale_notes:
                    if fret == 0:
                        marker_x = 45
                    else:
                        marker_x = 80 + (fret * fret_spacing) - (fret_spacing / 2)
                    
                    if note_name == root_note:
                        marker_color = ROOT_COLOR
                        border_thickness = 3
                        border_color = "white"
                    else:
                        marker_color = SCALE_NOTE_COLOR
                        border_thickness = 1
                        border_color = "#1e1e1e"
                    
                    # Draw circular note indicators with dynamic tracking labels
                    canvas.create_oval(marker_x - 18, y - 18, marker_x + 18, y + 18, 
                                       fill=marker_color, outline=border_color, width=border_thickness, tags="dynamic_notes")
                    
                    canvas.create_text(marker_x, y, text=note_name, fill="white", font=("Arial", 9, "bold"), tags="dynamic_notes")
                    
                    scale_degree = scale_notes.index(note_name) + 1
                    canvas.create_text(marker_x, y + 28, text=str(scale_degree), fill="#b0bec5", font=("Arial", 9, "bold"), tags="dynamic_notes")


    # Bindings to clear_fretboard to match your interior naming scheme
    root_dropdown.bind("<<ComboboxSelected>>", clear_fretboard)
    formula_dropdown.bind("<<ComboboxSelected>>", clear_fretboard)
    
    clear_fretboard()  # Populate default view when app opens
    window.mainloop()


# --- MAIN CODE ---

if __name__ == "__main__":
    print("Opening Interactive Bass Guitar Fretboard Visualizer...")
    draw_fretboard()
