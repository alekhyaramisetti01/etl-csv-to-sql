import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("ETL Pipeline: CSV to PostgreSQL with Transformations & Queries", fontsize=10, fontweight="bold")

# Process Labels
steps = [
    "Extract Data\n(Source: dataset.csv)",
    "Transform Data\n(Remove Duplicates, Handle Missing Values)",
    "Load Data\n(Target: PostgreSQL)",
    "Execute Queries\n(analysis_queries.sql)",
    "Results & Analysis\n(Visualizations, Insights)"
]

# Text Elements
text_elements = [ax.text(5, 12 - i * 3, step, fontsize=9, ha='center', alpha=0) for i, step in enumerate(steps)]

# Circles to represent process stages
circles = [plt.Circle((5, 12 - i * 3), 0.6, color=['blue', 'orange', 'green', 'purple', 'red'][i], alpha=0) for i in range(len(steps))]

# Arrows for Flow Representation
arrows = [patches.FancyArrow(5, 11 - i * 3, 0, -2, width=0.1, color="black", alpha=0) for i in range(len(steps) - 1)]

# Add elements to plot
for circle in circles:
    ax.add_patch(circle)
for arrow in arrows:
    ax.add_patch(arrow)

# Animation function
def update_simplified(frame):
    index = frame // 10  # Show elements in steps
    if index < len(steps):
        text_elements[index].set_alpha(1)
        circles[index].set_alpha(1)
    if index > 0 and index - 1 < len(arrows):
        arrows[index - 1].set_alpha(1)
    return text_elements + circles + arrows

# Create animation
ani_simplified = animation.FuncAnimation(fig, update_simplified, frames=50, interval=300, repeat=False)

# Save animation as MP4 video
ani_simplified.save("etl_animation.mp4", writer="ffmpeg", fps=5)

print("✅ Animation saved as 'etl_animation.mp4'.")
