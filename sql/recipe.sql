-- All information necessary to "cook" a recipe; denormalized for now.

DROP TABLE IF EXISTS recipe;

CREATE TABLE recipe (
    instructions TEXT,
    ingredients JSONB
);
