# 📊 Matplotlib Learning

This repository contains my learning and practice work with **Matplotlib**, a Python library used for data visualization.

## 🚀 What is Matplotlib?

Matplotlib is a Python library used to create visualizations such as:

* 📈 Line Charts
* 📊 Bar Charts
* 🥧 Pie Charts
* 📊 Histograms
* 🎯 Scatter Plots

It helps convert data into visual charts that are easier to understand and analyze.

---

## 📚 Topics Covered

### 1. Basic Plotting

* `plt.plot()`
* `plt.figure()`
* `plt.show()`

### 2. Chart Customization

* `plt.title()`
* `plt.xlabel()`
* `plt.ylabel()`
* `plt.grid()`
* `plt.legend()`
* `figsize`
* `color`
* `linewidth`
* `markersize`
* `linestyle`
* `marker`

### 3. Axis Customization

* `plt.xticks()`
* `plt.yticks()`
* `plt.xlim()`
* `plt.ylim()`

### 4. Bar Chart

Learned how to compare categorical data using:

```python
plt.bar()
```

Also practiced:

* Colors
* Edge colors
* Labels
* Legends
* Grid
* Titles

### 5. Pie Chart

Learned how to represent parts of a whole using:

```python
plt.pie()
```

Practiced:

* `labels`
* `autopct`
* `colors`

Example:

```python
plt.pie(
    amount,
    labels=categories,
    autopct="%1.1f%%"
)
```

### 6. Histogram

Learned how to visualize the distribution of numerical data using:

```python
plt.hist()
```

Practiced:

* `bins`
* `color`
* `edgecolor`
* Titles
* Axis labels

Example:

```python
plt.hist(
    heights,
    bins=10,
    color="orange",
    edgecolor="black"
)
```

### 7. Scatter Plot

Learned how to visualize the relationship between two numerical variables using:

```python
plt.scatter()
```

Practiced:

* Multiple datasets
* Colors
* Markers
* Labels
* Legends
* Grid

Example:

```python
plt.scatter(
    hours,
    marks,
    color="blue",
    marker="*",
    label="Class A"
)
```

---

## 🧠 What I Have Learned

I can now:

* Create different types of charts
* Compare categorical data
* Visualize numerical distributions
* Observe relationships between variables
* Customize charts
* Add titles and axis labels
* Add legends and grids
* Customize colors and markers
* Compare multiple datasets in a scatter plot

---

## 🛠️ Technologies Used

* Python 🐍
* Matplotlib 📊

Install Matplotlib:

```bash
pip install matplotlib
```

---

## 📂 Repository Structure

```text
Matplotlib/
│
├── Basic_Plots/
├── Line_Charts/
├── Bar_Charts/
├── Pie_Charts/
├── Histograms/
├── Scatter_Plots/
└── README.md
```

---

## 🎯 Next Topics

* Subplots
* Multiple plots in one figure
* Advanced customization
* Working with real-world datasets
* Data visualization projects

---

## 📈 Learning Progress

**Matplotlib Basics → Completed ✅**

**Current focus:** Building stronger visualization skills through practice and projects.

---

## 👨‍💻 About

This repository documents my journey of learning **Python Data Visualization with Matplotlib** as part of my preparation for **AI/ML**.

> Learn → Practice → Build → Improve 🚀
