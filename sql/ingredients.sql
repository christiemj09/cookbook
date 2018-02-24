-- Store sets of ingredients for recipes.

DROP TABLE IF EXISTS ingredients;

CREATE TABLE ingredients (
    id SERIAL PRIMARY KEY,
    doc JSONB
);
