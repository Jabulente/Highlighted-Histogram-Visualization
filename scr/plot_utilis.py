import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns
import numpy as np


if __name__ == "__main__":
    np.random.seed(1)
    sample_data = np.random.normal(loc=0.5, scale=0.3, size=500)
    print(sample_data)

    fig, ax = plt.subplots(figsize=(9,8), dpi=100)
    sns.despine(ax=ax, left=True, right=True, bottom=False, top=True)
    n, bins, patches = plt.hist(
        sample_data, bins=25,
        facecolor='w',
        edgecolor='k',
        linewidth=0.5,
        alpha=0.7
    )
    
    n = n.astype('int')
    for i in range(len(patches)): 
        patches[i].set_facecolor(plt.cm.viridis(n[i] / max(n)))

    patches[10].set_fc('red')
    patches[10].set_alpha(1)
    
    plt.title("Distribution of Electrical Conductivity (dS/m)")
    ax.grid(linestyle='--', alpha=0.1, color='black')
    ax.set_xlabel('Electrical Conductivity (dS/m)')
    ax.set_ylabel('Frequency/Counts')
    
    text = "If you are interested in this, let’s connect."
    _params = dict(xy=(0.45, 43), xytext=(1, 25), fontsize=10, arrowprops={'width':0.4,'headwidth':7,'color':'#333333'})
    plt.annotate(text, **_params)
    
    plt.tight_layout(rect=[0, 0, 1, 0.97])
    text = f"Data Source: Electrical Conductivity (dS/m) (2025) | Created by: Jabulente | Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}"
    fig.text(0.5, -0.02, text, ha='center', va='center', fontsize=8, color='black')
    
    plt.show()
