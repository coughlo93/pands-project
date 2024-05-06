## Iris Flower Dataset Overview

The Iris flower dataset is a well-known collection of data used in machine learning for classification tasks. It was first introduced by Ronald Fisher in 1936 and consists of measurements of flower parts from three Iris species:

* **Iris setosa**
* **Iris virginica**
* **Iris versicolor**

**Features:**

The dataset contains four features for each flower:

* **Sepal length (cm):** Length of the sepals (leaf-like structures)
* **Sepal width (cm):** Width of the sepals
* **Petal length (cm):** Length of the petals
* **Petal width (cm):** Width of the petals

**Target Variable:**

The target variable in this dataset is the Iris species (setosa, virginica, or versicolor). This makes it suitable for supervised learning tasks, particularly classification, where the goal is to predict the species of a new flower based on its measured features.

**Applications:**

The Iris dataset is commonly used for:

* **Introducing machine learning concepts:** Due to its simplicity and small size, the Iris dataset serves as a great example for beginners to understand classification algorithms and explore data analysis techniques.
* **Benchmarking algorithms:** The dataset allows comparing the performance of different classification algorithms on a well-defined task.
* **Demonstrating data visualization:** The four features can be effectively visualized using techniques like scatter plots and histograms to explore relationships between features and identify potential patterns for classification.

**Availability:**

The Iris dataset is readily available from various online [sources](https://github.com/mwaskom/seaborn-data/blob/master/iris.csv) in different formats.

**In Summary:**

The Iris dataset provides a valuable resource for learning and practicing machine learning classification tasks. Its compact size and clear structure make it ideal for beginners to understand the fundamentals of classification algorithms and data analysis in Python.

- Firstly I imported the the following libraries to aid my data analysis with this project. Pandas, NumPy & Matplotlib.

- I then loaded the data from a CSV file from the Seaborn repository on GitHub.

- Following on from this I then loaded & inspected the data & inspected the types of data to help identify potential issues or anomalies that may need to be addressed before further analysis.

- To analyse some of this data, I needed to get some variable plots, for this I chose petal length & petal width and I created plots on a scatter plot using NumPy & Matplotlib.

- I then needed to get the best fit line which can be got from the equation which I wass able to find from [statology.org](https://www.statology.org/line-of-best-fit-python/). I then plotted this line onto the scatter plot.

- I was then able to measure the corrolation using [numpy.corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html)

- Finally I decided to plot some histograms to analyse the petal lengths & petal widths in the dataset

**Packages Used:**

**Pandas** -  a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

**NumPy** - NumPy empowers you to perform complex numerical computations in Python with speed and ease.

**Matplotlib** - Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible.

# References

- [uci.edu Iris Dataset](https://archive.ics.uci.edu/dataset/53/iris)
 
- [Seaborn Iris Dataset](https://github.com/mwaskom/seaborn-data/blob/master/iris.csv)
 
- [Pydata](https://pandas.pydata.org/)
 
- [Numpy](https://numpy.org/)
 
- [Matplotlib](https://matplotlib.org/)

- [W3 Schools](https://www.w3schools.com/python/)

- [Python Cheat Sheet](https://acrobat.adobe.com/id/urn:aaid:sc:EU:f0f818bf-f5f5-469d-a9c9-9ef5370367e9?comment_id=29df74be-c9cb-4937-acb5-2c65a445a664)

- [Image source](http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html#correlations)

- [statology.org](https://www.statology.org/line-of-best-fit-python/)

- [numpy.corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html)
