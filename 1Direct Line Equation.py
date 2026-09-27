import matplotlib.pyplot as plt


def direct_line(x1, y1, x2, y2):

    pixels = []

    print("\n--- Direct Line Equation Method ---")
    print("Starting point:", (x1, y1))
    print("Ending point:", (x2, y2))

    dx = x2 - x1
    dy = y2 - y1

    # Vertical line
    if dx == 0:

        print("Case: Vertical line.")
        print("Slope is undefined.\n")

        start_y = min(y1, y2)
        end_y = max(y1, y2)

        for y in range(start_y, end_y + 1):

            pixels.append((x1, y))

            print(
                "x =", x1,
                "y =", y,
                "pixels ->", (x1, y)
            )

    else:

        # Calculate slope
        m = dy / dx

        # Calculate y-intercept
        b = y1 - m * x1

        print("Slope:", m)
        print("Y-intercept:", b)

        # Shallow line
        if abs(m) <= 1:

            print("Case: Shallow line.\n")

            start_x = min(x1, x2)
            end_x = max(x1, x2)

            for x in range(start_x, end_x + 1):

                y = m * x + b
                round_y = round(y)

                pixels.append((x, round_y))

                print(
                    "x =", x,
                    "y =", y,
                    "pixels ->", (x, round_y)
                )

        # Steep line
        else:

            print("Case: Steep line.\n")

            start_y = min(y1, y2)
            end_y = max(y1, y2)

            for y in range(start_y, end_y + 1):

                x = (y - b) / m
                round_x = round(x)

                pixels.append((round_x, y))

                print(
                    "y =", y,
                    "x =", x,
                    "pixels ->", (round_x, y)
                )

    return pixels


# Input
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))


# Calling function
pixels = direct_line(x1, y1, x2, y2)


# Extract pixel coordinates
x_pixels = [p[0] for p in pixels]
y_pixels = [p[1] for p in pixels]


# Plotting
plt.figure(figsize=(8, 6))


# Ideal mathematical line
plt.plot(
    [x1, x2],
    [y1, y2],
    label="Ideal Mathematical Line"
)


# Generated pixels
plt.scatter(
    x_pixels,
    y_pixels,
    s=100,
    marker="s",
    color="red",
    label="Generated Pixels"
)


# End points
plt.scatter(
    [x1, x2],
    [y1, y2],
    s=150,
    marker="o",
    color="green",
    label="End Points"
)


# Label pixels
for x, y in pixels:

    plt.annotate(
        f"({x}, {y})",
        (x, y),
        xytext=(8, 8),
        textcoords="offset points",
        fontsize=10
    )


# Axis settings
plt.xticks(
    range(
        min(x1, x2) - 1,
        max(x1, x2) + 2
    )
)

plt.yticks(
    range(
        min(y1, y2) - 1,
        max(y1, y2) + 2
    )
)


plt.grid(True)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Direct Line Equation Algorithm")
plt.legend()

plt.show()