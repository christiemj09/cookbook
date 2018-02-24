-- Add a recipe to the database.

CREATE OR REPLACE FUNCTION public.add_recipe(recipe TEXT, ingredients JSONB)
RETURNS VOID
AS $$
BEGIN

-- Function body goes here

END
$$ LANGUAGE plpgsql;