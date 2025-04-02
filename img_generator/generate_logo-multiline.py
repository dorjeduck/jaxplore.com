import sys
from PIL import Image, ImageDraw
import argparse

# Check for correct usage
if len(sys.argv) < 2:
    print("Usage: python generate_logo-multiline.py <text>")
    sys.exit(1)

# Fixed image width and spacing
# Parse command line arguments
parser = argparse.ArgumentParser(description="Generate a logo from text.")
parser.add_argument("text", help="Text to generate the logo from")
parser.add_argument("--width", type=int, default=1000, help="Width of the image")
parser.add_argument("--spacing", type=int, default=5, help="Spacing between squares")
parser.add_argument(
    "--always_blue_first",
    action="store_true",
    help="Always use blue color for the first square",
)
args = parser.parse_args()

# Assign parsed arguments to variables
img_width = args.width
spacing = args.spacing
ALWAYS_BLUE_FIRST = args.always_blue_first


# Split text into lines
text = sys.argv[1].upper()  # Convert input text to uppercase
lines = text.split("_")
max_line_length = max(len(line) for line in lines)

# Space between lines multiplier
line_spacing_multiplier = 3

# Calculate square size and image height dynamically
square_size = (img_width - 6 * (max_line_length + 1) * spacing) // (3 * max_line_length)
img_height = len(lines) * (5 * (square_size + spacing) - spacing) + (len(lines) - 1) * (
    line_spacing_multiplier * spacing
)

# Create an image with a transparent background
image = Image.new("RGBA", (img_width, img_height), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Colors for the squares
colors = [(68, 118, 222, 255), (19, 135, 123, 255), (195, 83, 214, 255)]


# Grid definitions for each letter (5x3 grid)
def get_letter_grid(letter):
    grids = {
        "A": [
            (0, 1),
            (1, 0),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
            (3, 0),
            (3, 2),
            (4, 0),
            (4, 2),
        ],
        "B": [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
            (3, 0),
            (3, 2),
            (4, 0),
            (4, 1),
            (4, 2),
        ],
        "C": [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2)],
        "D": [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 2),
            (2, 0),
            (2, 2),
            (3, 0),
            (3, 2),
            (4, 0),
            (4, 1),
            (4, 2),
        ],
        "E": [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (2, 0),
            (2, 1),
            (3, 0),
            (4, 0),
            (4, 1),
            (4, 2),
        ],
        "F": [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (2, 1), (3, 0), (4, 0)],
        "G": [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (2, 0),
            (3, 0),
            (3, 2),
            (4, 0),
            (4, 1),
            (4, 2),
        ],
        "H": [
            (0, 0),
            (0, 2),
            (1, 0),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
            (3, 0),
            (3, 2),
            (4, 0),
            (4, 2),
        ],
        "I": [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)],
        "J": [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (4, 1), (4, 0), (3, 0)],
        "K": [
            (0, 0),
            (0, 2),
            (1, 0),
            (1, 2),
            (2, 0),
            (2, 1),
            (3, 0),
            (3, 2),
            (4, 0),
            (4, 2),
        ],
        "L": [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2)],
        "M": [
            (0, 0),
            (0, 2),
            (1, 0),
            (1, 1),
            (1, 2),
            (2, 0),
            (2, 2),
            (3, 0),
            (3, 2),
            (4, 0),
            (4, 2),
        ],
        "N": [
            (0, 1),
            (1, 0),
            (1, 2),
            (2, 0),
            (2, 2),
            (3, 0),
            (3, 2),
            (4, 0),
            (4, 2),
        ],
        "O": [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 2),
            (2, 0),
            (2, 2),
            (3, 0),
            (3, 2),
            (4, 0),
            (4, 1),
            (4, 2),
        ],
        "P": [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
            (3, 0),
            (4, 0),
        ],
        "Q": [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
            (3, 2),
            (4, 2),
        ],
        "R": [
            (0, 0),
            (0, 1),
            (1, 0),
            (1, 2),
            (2, 0),
            (2, 1),
            (3, 0),
            (3, 2),
            (4, 0),
            (4, 2),
        ],
        "S": [
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 1),
            (2, 1),
            (2, 2),
            (3, 0),
            (3, 2),
            (4, 0),
            (4, 1),
        ],
        "T": [(0, 0), (0, 1), (0, 2), (1, 1), (2, 1), (3, 1), (4, 1)],
        "U": [
            (0, 0),
            (0, 2),
            (1, 0),
            (1, 2),
            (2, 0),
            (2, 2),
            (3, 0),
            (3, 2),
            (4, 0),
            (4, 1),
            (4, 2),
        ],
        "V": [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2), (3, 0), (3, 2), (4, 1)],
        "W": [
            (0, 0),
            (0, 2),
            (1, 0),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
            (3, 0),
            (3, 2),
            (4, 0),
            (4, 2),
        ],
        "X": [
            (0, 0),
            (1, 0),
            (2, 1),
            (3, 0),
            (4, 0),
            (4, 2),
            (3, 2),
            (1, 2),
            (0, 2),
        ],
        "Y": [(0, 0), (0, 2), (1, 0), (1, 2), (2, 1), (3, 1), (4, 1)],
        "Z": [(0, 0), (0, 1), (0, 2), (1, 2), (2, 1), (3, 0), (4, 0), (4, 1), (4, 2)],
        "-": [(2, 0), (2, 1), (2, 2)],
    }
    return grids.get(letter.upper(), [])


# Start drawing text as squares
x_offset = 10  # Initial horizontal offset
y_offset = (
    img_height
    - (
        len(lines) * (5 * (square_size + spacing) - spacing)
        + (len(lines) - 1) * (line_spacing_multiplier * spacing)
    )
) // 2  # Vertical centering

n = 0
for i, line in enumerate(lines):
    
    line_width = len(line) * (3 * square_size + 4 * spacing) - spacing
    x_offset = (img_width - line_width) // 2  # Horizontal centering for each line
    for j, letter in enumerate(line):
        
        grid = get_letter_grid(letter)
        for y, x in grid:
            color = (
                colors[j % len(colors)]
                if ALWAYS_BLUE_FIRST
                else colors[n % len(colors)]
            )
            
            x1 = x_offset + x * (square_size + spacing)
            y1 = y_offset + y * (square_size + spacing)
            x2 = x1 + square_size
            y2 = y1 + square_size
            draw.rectangle([x1, y1, x2, y2], fill=color)
        
        x_offset += 3 * square_size + 4 * spacing
        n += 1  # Add spacing between letters
    y_offset += (
        5 * (square_size + spacing) + line_spacing_multiplier * spacing
    )  # Move to next line with additional spacing

# Save the image
image.save(text.lower() + ".png", "PNG")
