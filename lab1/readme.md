# Console Paint Application

## Description
This is a console-based Paint application written in Python, designed to work within a Linux terminal. The program allows users to create and manipulate geometric shapes on a virtual canvas. The application follows **Object-Oriented Programming (OOP)** principles and supports saving/loading canvases.

## Features
- Large canvas occupying the full terminal window
- Supports three types of shapes:
  - **Rectangle** (created by specifying the top-left corner, width, and height)
  - **Triangle** (created using three sides: `a, b, c`)
  - **Circle** (created using center coordinates and radius)
- Operations on shapes:
  - **Move** the shape
  - **Erase** a shape from the canvas
  - **Fill** a shape with a chosen character
- Undo/Redo functionality
- Save and load canvas from a file

## Installation
### Requirements
- Python 3.x
- Linux-based terminal (for proper rendering)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/console-paint.git
   cd console-paint
   ```
2. Run the application:
   ```sh
   python3 paint.py
   ```

## Usage
### Main Menu
```
exit - Exit (without saving)
add - Create a new shape
save - Save canvas to file
load - Load canvas from file
undo - Undo last action
redo - Redo last undone action
```

### Creating Shapes
When selecting **Create Shape**, choose the type:
- **Rectangle**: `x, y, width, height`
- **Triangle**: `a, b, c` (side lengths)
- **Circle**: `x, y, radius`

### Managing Shapes
```
move - Move shape
remove - Erase shape
```

### Saving & Loading
- **Save Canvas**: Enter filename (e.g., `canvas.json`).
- **Load Canvas**: Enter filename to restore a previously saved state.

### Undo & Redo
- **Undo (`5`)** the last action
- **Redo (`6`)** an undone action

## Notes
- All numeric inputs must be **integers**.
- Shapes are drawn using ASCII characters, so proportions may not be perfectly accurate.
- The canvas refreshes dynamically to display changes.

## License
no license )))

---
### Author
minigunpunk21
