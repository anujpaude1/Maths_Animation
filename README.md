# Maths Animation

This repository contains code for creating mathematical animations using the Manim library. The animations include visualizations of geometric shapes, integration concepts, and more.

## Requirements

To run the code in this repository, you need to have the following packages installed:

- `manim==0.15.2`
- `numpy==1.21.0`

You can install the required packages using the following command:

```sh
pip install -r requirements.txt
```

## File Descriptions

### `integration.py`

This file contains classes and methods to create animations related to integration concepts. Key classes include:

- `GetAreaExample(Scene)`: Demonstrates the area of a shaded region using integration.
- `pp(ZoomedScene)`: Creates a zoomed-in view of the integration process with Riemann rectangles.

### `cube.py`

This file contains the `Try(ThreeDScene)` class, which creates 3D animations of geometric shapes, including cubes and their diagonals. It also includes angle calculations and visualizations.

### `rolles_theorem.py`

This file contains the `Try(Scene)` class, which demonstrates Rolle's Theorem using a graph with labeled axes and points.

### `requirements.txt`

Lists the required Python packages to run the animations.

### `temp.py`

An empty file that imports the Manim library.

### `.gitignore`

Specifies files and directories to be ignored by Git, including `__pycache__`, `tempCodeRunnerFile.py`, and `media`.

## Running the Animations

To run an animation, use the following command:

```sh
manim -pql <filename.py> <ClassName>
```

For example, to run the `GetAreaExample` animation from `integration.py`, use:

```sh
manim -pql integration.py GetAreaExample
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Manim](https://www.manim.community/) - The mathematical animation engine used in this project.
- [NumPy](https://numpy.org/) - The fundamental package for scientific computing with Python.
