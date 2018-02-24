CREATE OR REPLACE FUNCTION public.workon(venv TEXT)
RETURNS VOID
AS $$
"""
Run a script invocation from its recipe.
"""

# Function body goes here

$$ LANGUAGE plpythonu;