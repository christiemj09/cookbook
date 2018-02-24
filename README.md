# Introduction

Save script invocations in a database and allow them to be run from queries.

# Ideas

Maybe some cute metaphors for the mental model:

* `instructions`: A format string that can be turned into an executable line of Bash.
* `ingredients`: Values that populate instructions.
* `recipe`: A pairing of instructions and ingredients. Specifies a script invocation.
* `meal`: A script pipeline composed of a series of recipes.
* `dish`: Blocks of recipes that are grouped together for ease of reference.

# Challenges

* Can simplify some of the machinery to be a Python code execution engine. How best to isolate the two sets of functionality?
* Can this be made portable across databases? Probably not if you use PL/Python, but what if you use SQLAlchemy? Target MySQL and SQLite if so.
* Would be nice to have a UI instead of manual entry. Django? Or use `atomize`...