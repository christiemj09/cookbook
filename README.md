# Introduction

Save script invocations in a database and allow them to be run from queries.

# Ideas

Maybe some cute metaphors for the mental model:

* `recipe`: A format string that can be turned into an executable line of Bash (have to worry about injection)
* `ingredient`: A value that populates a recipe.
* `meal`: A script pipeline composed of a series of recipes.
* `dish`: Blocks of recipes that are grouped together for ease of reference.

# Challenges

* How to handle shell injection? Don't need to if recipes are signed or verified in some way? Ban comments or semicolons? Or just don't need to worry about it at all since you're not accepting any outside input for recipes?
* Can simplify some of the machinery to be a Python code execution engine. How best to isolate the two sets of functionality?
* Can this be made portable across databases? Probably not if you use PL/Python, but what if you use SQLAlchemy? Target MySQL and SQLite if so.
