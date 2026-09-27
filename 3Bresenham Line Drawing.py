import matplotlib.pyplot as plt


def bresenham_line(x1, y1, x2, y2):

    pixels = []

    print("\n--- Bresenham Line Drawing Algorithm ---")
    print("Starting point:", (x1, y1))
    print("Ending point:", (x2, y2))

    # Calculate dx and dy
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    print("\ndx =", dx)
    print("dy =", dy)

    # Determine x direction
    if x1 < x2:
        sx = 1
    else:
        sx = -1

    # Determine y direction
    if y1 < y2:
        sy = 1
    else:
        sy = -1

    # Initial error
    error = dx - dy

    print("Initial Error:", error)
    print("\nGenerated Pixels:\n")

    step = 0

    while True:

        # Store pixel
        pixels.append((x1, y1))

        print(
            "Step:", step,
            "x =", x1,
            "y =", y1,
            "Error =", error,
            "pixels ->",
            (x1, y1)
        )

        # Stop condition
        if x1 == x2 and y1 == y2:
            break

        # Double error
        e2 = 2 * error

        # Update X
        if e2 > -dy:

            error = error - dy
            x1 = x1 + sx

        # Update Y
        if e2 < dx:

            error = error + dx
            y1 = y1 + sy

        step += 1

    return pixels


# Input
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))


# Calling function
pixels = bresenham_line(x1, y1, x2, y2)


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
    label="Bresenham Pixels"
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
plt.title("Bresenham Line Drawing Algorithm")
plt.legend()

plt.show()