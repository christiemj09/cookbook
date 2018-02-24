CREATE OR REPLACE FUNCTION public.workon(venv TEXT)
RETURNS VOID
AS $$
"""
Activate a virtual environment.
"""

# From https://gist.github.com/dmckeone/69334e2d8b27f586414a
import os
activate_this = os.path.join(venv, 'bin', 'activate_this.py')
exec(open(activate_this).read(), dict(__file__=activate_this))

$$ LANGUAGE plpythonu;
