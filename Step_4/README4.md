# Create and show a bar chart using matplotlib.

In this lesson you will learn how to draw a countplot plot using the seaborn and matplotlib.pyplot modules

Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible.

You will use the seaborn `countplot` and the `.show()` method for this course to draw your unique plot.

## Seaborn know how:
- remember the category attribute we have given to some fields in the last step?
- those categories are used when we want to plot something on an axis in a given order
- let's say that we want to plot the number of games per [Xbox, PS4] platform by the genre of the games and we want the genres
to be also ordered alphabetically, what we can do is to create special categories for the given fields where we specify the order
of plotting and then we create the plot
- `sns.countplot(x="field", hue="category", data=df, native_scale=True)` creates a plot with the given specification:
    - on the x axis we have the **unique items** of the **"field"**
    - every item on the x axis has a number of bars that represents the number of all the items included in 
    the **hue = "category"**(it is not the same concept as the category attribute, "category" in this case is a field name from the DataFrame)
- you can specify the order of the items and the order of the bars for an item by using the category attribute we have explained above
that changes the DataFrame object(df)

## Matplotlib.pyplot know ow:
- after defining the count plot we can draw it using the `.plot()` method

## Task:
- draw a count plot with some specification provided in the task4.py script

## Checker:
- in order to check your code run the checker4.py script

Hint: Try to understand the reason of this implementation and why the things are defined as we presented.
