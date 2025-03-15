-- Database: hospital

-- DROP DATABASE IF EXISTS hospital;

CREATE DATABASE hospital
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'es-ES'
    LC_CTYPE = 'es-ES'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
CREATE TABLE devices (
    id SERIAL PRIMARY KEY,
    device_name VARCHAR(255) NOT NULL
);


CREATE TABLE medical_results (
    id SERIAL PRIMARY KEY,
    external_id VARCHAR(255) UNIQUE NOT NULL,
    device_id INTEGER REFERENCES devices(id) ON DELETE CASCADE,
    average_before FLOAT NOT NULL,
    average_after FLOAT NOT NULL,
    data_size INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear la función para actualizar updated_at automáticamente
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- Crear el trigger que actualiza updated_at en cada UPDATE

CREATE TRIGGER update_medical_results_updated_at
BEFORE UPDATE ON medical_results
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

