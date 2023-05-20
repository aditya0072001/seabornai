# seabornai

[![Downloads](https://pepy.tech/badge/seabornai/month)](https://pepy.tech/project/seabornai)

seabornai is a Python library that leverages the OpenAI ChatGPT API to generate Seaborn graphs based on supplied data and prompts/questions.

**Disclaimer:** Usage of this library requires an OpenAI API key and subscription, as well as the Seaborn library installed.

## Installation

You can install seabornai using pip:

```
pip install seabornai
```

## Usage

```python
from seabornai import generate_graph, set_openai_api_key

# Set your OpenAI API key
api_key = input("Please enter your OpenAI API key: ")
set_openai_api_key(api_key)

# Example usage
data = {"x_column": [1, 2, 3], "y_column": [4, 5, 6]}
prompt = "What is the relationship between x_column and y_column?"

# Generate a Seaborn graph
generate_graph(data, prompt)
```

## Features

- Generate Seaborn graphs based on supplied data and prompts/questions.
- Customize graph style, size, labels, titles, legends, and colors.
- Choose from various types of plots, such as bar plots, scatter plots, line plots, or box plots.
- Perform statistical analysis by adding regression lines, confidence intervals, or hypothesis testing.
- Save the generated graph to a file in different formats (e.g., PNG, PDF, SVG).

## Examples

Here are some examples of using seabornai to generate Seaborn graphs:

### Example 1: Scatter Plot

```python
data = {"x_column": [1, 2, 3, 4], "y_column": [2, 4, 6, 8]}
prompt = "What is the relationship between x_column and y_column?"

generate_graph(data, prompt, style="darkgrid", size=(8, 6))
```

### Example 2: Bar Plot

```python
data = {"category": ["A", "B", "C"], "value": [10, 20, 30]}
prompt = "How does the value vary across different categories?"

generate_graph(data, prompt, style="whitegrid", size=(6, 4))
```

## Download and Popularity

The seabornai package has been downloaded approximately X times per month. Thank you for your support!

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
