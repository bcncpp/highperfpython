from fractal.julia import calc_pure_python


def main():
    # Calculate the Julia set using a pure Python solution with
    # reasonable defaults for a laptop
    calc_pure_python(desired_width=1000, max_iterations=300)


if __name__ == "__main__":
    main()
