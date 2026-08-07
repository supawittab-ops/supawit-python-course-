def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

def calculate_triangle_area(base, height):
    """Calculates and displays triangle area"""
    area = (base * height) / 2
    print(f"Triangle with base {base} and height {height}")
    print(f"Area = ({base} × {height}) / 2 = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)