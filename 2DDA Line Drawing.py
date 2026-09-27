import matplotlib.pyplot as plt


def dda_line(x1, y1, x2, y2):

    pixels = []

    print("\n--- DDA Line Drawing Algorithm ---")
    print("Starting point:", (x1, y1))
    print("Ending point:", (x2, y2))

    # Calculate dx and dy
    dx = x2 - x1
    dy = y2 - y1

    print("\ndx =", dx)
    print("dy =", dy)

    # Calculate number of steps
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    print("Number of steps:", steps)

    # Calculate increments
    x_increment = dx / steps
    y_increment = dy / steps

    print("X increment:", x_increment)
    print("Y increment:", y_increment)

    # Starting coordinates
    x = x1
    y = y1

    print("\nGenerated Pixels:\n")

    # Generate pixels
    for i in range(steps + 1):

        round_x = round(x)
        round_y = round(y)

        pixels.append((round_x, round_y))

        print(
            "Step:", i,
            "x =", x,
            "y =", y,
            "pixels ->",
            (round_x, round_y)
        )

        # Update coordinates
        x = x + x_increment
        y = y + y_increment

    return pixels


# Input
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))


# Calling function
pixels = dda_line(x1, y1, x2, y2)


# Extract coordinates
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
    label="DDA Generated Pixels"
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


# Label each pixel
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
plt.title("DDA Line Drawing Algorithm")
plt.legend()

plt.show()