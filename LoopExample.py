def create_array():
    """creates array"""
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    return planets

def main():
    """prints the array"""
    # planets=create_array()
    # for planet in planets:
     #   print(planet, end='\n')
    print_squares()
    print_square_with_list_comprehension()

def print_squares():
    """Print square of numbers from 1-10"""
    squares = []
    for number in range(10):
        squares.append(number**2)
    print(squares)

def print_square_with_list_comprehension():
    """Print squares of numbers from 1-10"""
    squares=[n**2 for n in range(10)]
    print (squares)

if __name__ == "__main__":
    main()