import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_use_case_diagram():
    _, ax = plt.subplots(figsize=(8, 6))

    # Draw actors
    ax.text(0.1, 0.8, 'User', fontsize=12, ha='center')
    ax.text(0.9, 0.8, 'Admin', fontsize=12, ha='center')

    # Draw use cases
    use_cases = [
        (0.3, 0.6, 'Search for Books'),
        (0.3, 0.5, 'Borrow Books'),
        (0.3, 0.4, 'Return Books'),
        (0.3, 0.3, 'View Borrowed Books'),
        (0.3, 0.2, 'Receive Notifications'),
        (0.7, 0.5, 'Add Books'),
        (0.7, 0.4, 'Delete Books'),
        (0.7, 0.3, 'View All Books')
    ]

    for x, y, label in use_cases:
        ax.add_patch(patches.Ellipse((x, y), width=0.2, height=0.1, edgecolor='black', facecolor='lightgray'))
        ax.text(x, y, label, ha='center', va='center')

    # Draw lines between actors and use cases
    user_lines = [
        ((0.1, 0.8), (0.3, 0.55)),  # Search for Books
        ((0.1, 0.8), (0.3, 0.45)),  # Borrow Books
        ((0.1, 0.8), (0.3, 0.35)),  # Return Books
        ((0.1, 0.8), (0.3, 0.25)),  # View Borrowed Books
        ((0.1, 0.8), (0.3, 0.15))   # Receive Notifications
    ]
    
    admin_lines = [
        ((0.9, 0.8), (0.7, 0.45)),  # Add Books
        ((0.9, 0.8), (0.7, 0.35)),  # Delete Books
        ((0.9, 0.8), (0.7, 0.25))   # View All Books
    ]

    for line in user_lines:
        ax.plot(*zip(*line), color='black', linestyle='--')

    for line in admin_lines:
        ax.plot(*zip(*line), color='black', linestyle='--')

    # Set limits and hide axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Save the diagram
    plt.title('Use Case Diagram', fontsize=14)
    plt.savefig('use_case_diagram.png', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    draw_use_case_diagram()
