# 📊 Matplotlib — Data Visualization with Python

A structured, hands-on journey to mastering **Matplotlib**, Python's core visualization library.
This repository contains practical examples, experiments, and exercises focused on building clear and meaningful data visualizations.

---

## 🎯 Learning Objective

The goal of this repository is to develop a strong foundation in **data visualization with Python** and learn how to transform datasets into meaningful visual insights.

Matplotlib is being learned as part of my broader **Data Science / AI & ML learning journey**.

---

## 🛠️ Technologies

* **Python**
* **Matplotlib**
* **VS Code**
* **Jupyter Notebook** *(when required)*

---

## 📚 Topics Covered

### Basic Plotting

* `plt.plot()`
* `plt.show()`
* `plt.figure()`
* `figsize`

### Chart Customization

* `plt.title()`
* `plt.xlabel()`
* `plt.ylabel()`
* `plt.grid()`
* `plt.xticks()`
* `plt.yticks()`

### Line Customization

* `linewidth`
* `markersize`
* Line styling
* Multiple lines

### Legends

* `label`
* `plt.legend()`

### Bar Charts

* `plt.bar()`
* Bar colors
* Category-based visualization
* Comparing values using bars

### Axis Control

* `plt.xlim()`
* `plt.ylim()`
* Controlling the visible axis range
* Understanding categorical vs numerical axes

---

## 📈 Current Progress

| Topic                  | Status      |
| ---------------------- | ----------- |
| Basic Plotting         | ✅ Completed |
| Titles & Labels        | ✅ Completed |
| Grid                   | ✅ Completed |
| X/Y Ticks              | ✅ Completed |
| Figure Size            | ✅ Completed |
| Line Customization     | ✅ Completed |
| Multiple Lines         | ✅ Completed |
| Legends                | ✅ Completed |
| Bar Charts             | ✅ Completed |
| X-axis Limits          | ✅ Completed |
| Y-axis Limits          | ✅ Completed |
| Subplots               | 🔄 Next     |
| Pie Charts             | ⏳ Upcoming  |
| Scatter Plots          | ⏳ Upcoming  |
| Histograms             | ⏳ Upcoming  |
| Advanced Customization | ⏳ Upcoming  |
| Mini Projects          | ⏳ Upcoming  |

---

## 💻 Example

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]

sales = [12000, 15000, 13500, 18000, 21000, 19500, 23000, 26000]

plt.figure(figsize=(10, 6))

plt.title("2026 Sales")
plt.xlabel("Month")
plt.ylabel("Monthly Sales")

plt.bar(months, sales, label="Sales")

plt.legend()

plt.xlim(1, 6)
plt.ylim(0, 30000)

plt.show()
```

---

## 🧠 Learning Approach

Instead of only following tutorials, I practice each concept by:

1. Learning the function
2. Writing the code independently
3. Testing it with different datasets
4. Identifying and fixing errors
5. Understanding how each parameter affects the visualization
6. Applying the concept in practical examples

The focus is on **understanding the logic behind visualization**, not simply memorizing syntax.

---

## 🗂️ Repository Structure

```text
Matplotlib/
│
├── Basics/
├── Line_Plots/
├── Bar_Charts/
├── Axis_Customization/
├── Subplots/
├── Pie_Charts/
├── Scatter_Plots/
├── Histograms/
├── Projects/
└── README.md
```

*The folder structure will evolve as new concepts are added.*

---

## 🗺️ Roadmap

### Phase 1 — Fundamentals

* [x] Basic plots
* [x] Titles and labels
* [x] Grid
* [x] Figure size
* [x] Ticks

### Phase 2 — Customization

* [x] Line customization
* [x] Legends
* [x] Multiple plots
* [x] Axis limits

### Phase 3 — Chart Types

* [x] Bar charts
* [ ] Pie charts
* [ ] Scatter plots
* [ ] Histograms
* [ ] Box plots

### Phase 4 — Advanced Visualization

* [ ] Subplots
* [ ] Advanced styling
* [ ] Annotations
* [ ] Figure saving
* [ ] Advanced axis customization

### Phase 5 — Projects

* [ ] Sales analysis
* [ ] Expense analysis
* [ ] Temperature analysis
* [ ] Business dashboard
* [ ] Data analysis projects

---

## 🚀 Long-Term Goal

Build strong visualization skills that can be applied to:

* Data Analysis
* Exploratory Data Analysis (EDA)
* Machine Learning
* AI/ML Projects
* Business Analytics
* Data Science

---

## 📌 Status

**Currently learning:** Matplotlib fundamentals and chart customization

**Next:** `subplot()` and multiple charts in a single figure.

---

### 👨‍💻 Author

**Kiran L.M**

Aspiring **AI/ML Engineer** | Python Developer | Data Science Enthusiast
