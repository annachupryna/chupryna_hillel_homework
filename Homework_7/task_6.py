# Task 6


def rotate_arrows(arrows):
    num_of_arrows = set()
    for arrow in arrows:
        num_of_arrows.add(arrows.count(arrow))
    return len(arrows) - max(num_of_arrows)
