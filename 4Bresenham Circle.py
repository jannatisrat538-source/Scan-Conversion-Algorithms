import matplotlib.pyplot as plt


def bresenham_circle(xc, yc, r):

    pixels = []

    print("\n--- Bresenham Circle Algorithm ---")
    print("Center:", (xc, yc))
    print("Radius:", r)

    # Initial values
    x = 0
    y = r

    # Initial decision parameter
    p = 3 - 2 * r

    print("\nInitial x =", x)
    print("Initial y =", y)
    print("Initial decision parameter =", p)

    step = 0

    while x <= y:

        print("\nStep:", step)
        print("x =", x, "y =", y)
        print("Decision parameter =", p)

        # 8 symmetric points
        points = [

            (xc + x, yc + y),
            (xc - x, yc + y),

            (xc + x, yc - y),
            (xc - x, yc - y),

            (xc + y, yc + x),
            (xc - y, yc + x),

            (xc + y, yc - x),
            (xc - y, yc - x)

        ]

        # Store and print pixels
        for point in points:

            pixels.append(point)

            print(
                "pixels ->",
                point
            )

        # Update decision parameter
        if p < 0:

            print("Decision: p < 0")

            p = p + 4 * x + 6

        else:

            print("Decision: p >= 0")

            p = p + 4 * (x - y) + 10

            y = y - 1

        x = x + 1

        step += 1

    return pixels


# Input
xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))
r = int(input("Enter radius: "))


# Calling function
pixels = bresenham_circle(xc, yc, r)


# Extract coordinates
x_pixels = [p[0] for p in pixels]
y_pixels = [p[1] for p in pixels]


# Plotting
plt.figure(figsize=(8, 8))


# Generated circle pixels
plt.scatter(
    x_pixels,
    y_pixels,
    s=100,
    marker="s",
    color="red",
    label="Generated Circle Pixels"
)


# Center point
plt.scatter(
    [xc],
    [yc],
    s=150,
    marker="o",
    color="green",
    label="Center"
)


# Label each pixel
for x, y in pixels:

    plt.annotate(
        f"({x}, {y})",
        (x, y),
        xytext=(6, 6),
        textcoords="offset points",
        fontsize=8
    )


# Axis settings
plt.xticks(
    range(
        xc - r - 2,
        xc + r + 3
    )
)

plt.yticks(
    range(
        yc - r - 2,
        yc + r + 3
    )
)


plt.grid(True)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title("Bresenham Circle Drawing Algorithm")

plt.axis("equal")
plt.legend()

plt.show()