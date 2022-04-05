### Learning Objectives
* Data visualization and some of the best practices when creating plots and visuals.
* The history and architecture of Matplotlib, and how to do basic plotting with Matplotlib.
* Generating different visualization tools using Matplotlib such as line plots, area plots, histograms, bar charts, box plots, and pie charts.
* Seaborn, another data visualization library in Python, and how to use it to create attractive statistical graphics.
* Folium, and how to use to create maps and visualize geospatial data.

### Section Includes
1. Introduction to Visualization Tools
2. Basic Visualization Tools
3. Specialized Visualization Tools
4. Extra Visualization Tools
5. Creating Maps and Visualizing Geospatial Data

---

### Introduction
**Why Build Visuals?**
* For exploratory data analysis
* Communicate data clearly
* Shared unbiased representation of data
* Use data to suport recommendations to stakeholders

**Less is More**
* Effective
* Attractive
* Impactive

**`Matplotlib`**
* John Hunter (1968 - 2012); developed as ECoG Visualization Tool
* Analogous to matlab scripting Interface
* Architecture
    * Scripting layer
        * Comprised mainly `pyplot`, a scripting interface that is lighter than the `Artist` layer
    * Artist layer
        * Artist is the one who knows how to use the rederer to draw on the canvas
        * Primitive and Composite Artist Objects
        * Each Artist may contain other composite artists or primitive artists
    * Backend layer
        * FigureCanvas: `matplotlib.backend_bases.FigureCanvas`
        * Renderer: `matplotlib.backend_bases.Renderer`
        * Event: `matplotlib.backend_bases.Event`

```Python
# Getting Started
# Normal Distribution Demonstration
import matplotlib.pyplot as plt
import numpy as np

randnum = np.random.randn(10000)
plt.hist(randnum, 100)
plt.title(r'Normal distribution with $\mu=0, \sigma=1$')
plt.savefig('matplotlib_histogram.png)
plt.show()
```

---