# Low_End_Fret
Bass Guitar Fretboard Visualizer

This is a Python code that generates an interactive GUI to visualize which notes fit within selected scales/triads. 
Users can choose from any starting note and an accompanying scale or triad.

There are either the Major Scale, Minor Scale, Major Pentatonic, Minor Pentatonic, Major Triad, or Minor Triad. 
It maps notes from open strings up to the 12th fret for standard 4-string bass tuning (E, A, D, G), color-coding root notes and tracking interval scale degrees.

Building this application allowed me to solidify the principles taught throughout the Code In Place course:
  - Decomposition & Logic: Data calculations (music theory math) had to be broken down into smaller steps.
  - Loops: Creating a loop for the musical notes, as they repeat across the fretboard.
  - Graphical Canvas Coordination: Ensuring shapes and text aligned as expected within graphic window dimensions.
  - Receiving User Input: Interactive drop-down menus and refreshing the graphics to respond to real-time user selections.




Installation & Setup

Prerequisites: Make sure you have Python 3 installed on your local machine. This script utilizes Python's built-in tkinter framework.

Running the App: 
Copy or download the source code file.
Open your terminal or command prompt in the project directory.
Execute the program file: python bass_visualizer.py

Alternatively, the code in the source file can be copied and pasted into an IDE of your choice. With this option, ensure that the IDE you choose is capable of generating a GUI interface. 


How the Program Works:
Dropdown Control Panel: Use the panel menus in the top right corner of the window to seamlessly select a Root Note and a target Scale/Triad.
The Grid Matrix: Notes are calculated accurately using absolute mathematical semitone values relative to standard base string pitches:
  - G String: Base index 31
  - D String: Base index 26
  - A String: Base index 21
  - E String: Base index 16


Future Iterations of this Project:
I will likely expand upon this project by giving the user a choice between picking a 4-string Bass Guitar or a 6-string Guitar. 
I chose a 4-string Bass Guitar as my starting point, as each string is exactly 5 semitones away from each other. This makes the math easy to loop and replicate. 
The main barrier to doing a visualization for a 6-string Guitar is that the 2nd highest string (B) does not follow the same pattern, so it is not exactly 5 semitones away from the preceding string.

  

Acknowledgments
A huge thank you to the Code in Place professors, section leaders, and peers! This project represents many hours of strengthening our problem-solving skills, debugging strategies, and coding foundations. 
