-- Format strings that can be populated with ingredients.

DROP TABLE IF EXISTS instructions;

CREATE TABLE instructions (
    id SERIAL PRIMARY KEY,
    text TEXT
);
