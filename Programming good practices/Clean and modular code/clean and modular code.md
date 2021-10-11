# Clean and modular code guidelines. 

## Writing clean code: Meaningful names

### Use meaningful names.

* For booleans prefix the name of the the variable with names like **is_ or has_**. Example **is_minor** = True 
* Use **verbs** for functions and **nouns** for variables 
* Be descriptive and imply type: For booleans, you can prefix with is_ or has_ to make it clear it is a condition. You can also use parts of speech to imply types, like using verbs for functions and nouns for variables.
* Be consistent but clearly differentiate: age_list and age is easier to differentiate than ages and age.
* Avoid abbreviations and single letters: You can determine when to make these exceptions based on the audience for your code. If you work with other data scientists, certain variables may be common knowledge. While if you work with full stack engineers, it might be necessary to provide more descriptive names in these cases as well. (Exceptions include counters and common math variables.)
* Long names aren't the same as descriptive names: You should be descriptive, but only with relevant information. For example, good function names describe what they do well without including details about implementation or highly specific uses. **Example** : def count_different_elements()
  
* Try testing how effective your names are by asking a fellow programmer to guess the purpose of a function or variable based on its name, without looking at your code. Coming up with meaningful names often requires effort to get right.

# Writing clean code: Nice whitespace

## Use whitespace properly.

* Organize your code with consistent indentation: the standard is to use four spaces for each indent. You can make this a default in your text editor.
* Separate sections with blank lines to keep your code well organized and readable.
* Try to limit your lines to around 79 characters, which is the guideline given in the PEP 8 style guide. In many good text editors, there is a setting to display a subtle line that indicates where the 79 character limit is.
* For more guidelines, check out the code layout section of PEP 8 in the following notes.

[Python guidelines](https://www.python.org/dev/peps/pep-0008/?#code-lay-out)


# Wriring modular code.



## Tip: DRY (Don't Repeat Yourself)
Don't repeat yourself! Modularization allows you to reuse parts of your code. Generalize and consolidate repeated code in functions or loops.

## Tip: Abstract out logic to improve readability
Abstracting out code into a function not only makes it less repetitive, but also improves readability with descriptive function names. Although your code can become more readable when you abstract out logic into functions, it is possible to over-engineer this and have way too many modules, so use your judgement.

## Tip: Minimize the number of entities (functions, classes, modules, etc.)
There are trade-offs to having function calls instead of inline logic. If you have broken up your code into an unnecessary amount of functions and modules, you'll have to jump around everywhere if you want to view the implementation details for something that may be too small to be worth it. Creating more modules doesn't necessarily result in effective modularization.

## Tip: Functions should do one thing
Each function you write should be focused on doing one thing. If a function is doing multiple things, it becomes more difficult to generalize and reuse. Generally, if there's an "and" in your function name, consider refactoring.

## Tip: Arbitrary variable names can be more effective in certain functions
Arbitrary variable names in general functions can actually make the code more readable.

## Tip: Try to use fewer than three arguments per function
Try to use no more than three arguments when possible. This is not a hard rule and there are times when it is more appropriate to use many parameters. But in many cases, it's more effective to use fewer arguments. Remember we are modularizing to simplify our code and make it more efficient. If your function has a lot of parameters, you may want to rethink how you are splitting this up.

# Documentation

## Inline comments:

* Inline comments are text following hash symbols throughout your code. They are used to explain parts of your code, and really help future contributors understand your work.
* Comments often document the major steps of complex code. Readers may not have to understand the code to follow what it does if the comments explain it. However, others would argue that this is using comments to justify bad code, and that if code requires comments to follow, it is a sign refactoring is needed.
* Comments are valuable for explaining where code cannot. For example, the history behind why a certain method was implemented a specific way. Sometimes an unconventional or seemingly arbitrary approach may be applied because of some obscure external variable causing side effects. These things are difficult to explain with code

## Docstrings **(functions)**:

Docstring, or documentation strings, are valuable pieces of documentation that explain the functionality of any function or module in your code. Ideally, each of your functions should always have a docstring.

Docstrings are surrounded by triple quotes. The first line of the docstring is a brief explanation of the function's purpose.

* One-line docstring
```python
def population_density(population, land_area):
    """Calculate the population density of an area."""
    return population / land_area
```   
If you think that the function is complicated enough to warrant a longer description, you can add a more thorough paragraph after the one-line summary.

* Multi-line docstring
```python
def population_density(population, land_area):
    """Calculate the population density of an area.

    Args:
    population: (int). The population of the area
    land_area: (int or float). This function is unit-agnostic, if you pass in values in terms of square km or square miles the function will return a density in those units.

    Returns:
    population_density: population/land_area. The population density of a 
    particular area.
    """
    return population / land_area
``` 

* The next element of a docstring is an explanation of the function's arguments. Here, you list the arguments, state their purpose, and state what types the arguments should be. Finally, it is common to provide some description of the output of the function. Every piece of the docstring is optional; however, doc strings are a part of good coding practice.