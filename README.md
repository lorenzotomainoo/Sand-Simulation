# Sand-Simulation

## Overview
Sand-Simulation is a 2D cellular automaton built in Python using the Pygame library. The project models granular physics, specifically simulating the behavior of falling sand. Particles interact with one another within a grid system, cascading downward and stacking according to basic rules of gravity and displacement. 

## Features
* **Cellular Automaton Engine:** Implements a bottom-up grid update algorithm to accurately simulate particle collisions, gravity, and displacement.
* **Interactive Rendering:** Users can draw sand structures in real-time using mouse input.
* **Dynamic Color Generation:** Particles are generated with slight color variations to provide a textured, realistic visual representation.
* **Multiple Material States:** Includes a secondary color generation mode, allowing for visual distinction between particle types (toggled via SPACEBAR).

## Prerequisites
To run this project locally, you must have the following installed on your system:
* Python 3.x
* Pygame (version 2.0.0 or higher)

## Installation

1. **Clone the repository:**
   Open your terminal or command prompt and run:
   ```
   git clone [https://github.com/your-username/Sand-Simulation.git](https://github.com/your-username/Sand-Simulation.git)

    Navigate to the project directory:

    cd Sand-Simulation

    Install the required dependencies:
    It is recommended to use a virtual environment. Install the Pygame library using pip:

    pip install pygame

Usage

To execute the simulation, run the main Python script from your terminal:

python main.py

Controls

    Left Mouse Button (Hold): Draw sand particles continuously at the cursor's location.

    Spacebar: Toggle between the default color scheme (sand) and the secondary color scheme.

Project Structure

    main.py: Contains the primary execution loop, display initialization, and event handling.

    library.py: Contains the core logic for the cellular automaton, including matrix initialization, state updates, and rendering functions.

License

This project is open-source and available under the MIT License.
