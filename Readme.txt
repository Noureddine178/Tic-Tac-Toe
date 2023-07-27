* Introduction:
Hello everyone! Today, I am thrilled to share my very first coding project with you all. As a beginner in the world of coding, I have embarked on an exciting journey to learn and explore the vast realm of programming.
My first project is a simple yet fun game called "Rock-Paper-Scissors," and I've built it using Python and the PyQt5 library to create a graphical user interface (GUI)

* Approach: 
Being a beginner, I wanted to start with a relatively straightforward project that allowed me to apply some of the basic concepts I've learned.
To make the game interactive and visually appealing, I decided to use the PyQt5 library to create a simple GUI.

* Key Components of the Code:
     Importing Libraries:

I began by importing the necessary libraries, such as random for generating the computer's choice and PyQt5 for creating the GUI.
The judge Function:

      The judge Function:

To determine the winner of each round, I defined the judge function. It compares the player's choice with the computer's choice using a dictionary that maps each option to its losing counterpart.
The play Function:

       The play Function:

The core of the game is encapsulated in the play function. Here, I get the player's choice from the GUI input and ensure it's a valid option (rock, paper, or scissors).
If the input is valid, I randomly generate the computer's choice and call the judge function to decide the round's winner.
The outcome of the round is then displayed in a message box using PyQt5.

        Graphical User Interface (GUI):

The GUI is created using a .ui file (rpz.ui) and loaded into the application using loadUi.
I designed a simple layout with a button for the player to click and an area to display the result of each round.

