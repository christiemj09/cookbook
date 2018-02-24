-- Initialize a table holding information on virtual environments.

CREATE OR REPLACE FUNCTION public.init_virtualenv()
RETURNS VOID
AS $$
BEGIN

CREATE TABLE IF NOT EXISTS virtualenv (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    path TEXT
);

END
$$ LANGUAGE plpgsql;