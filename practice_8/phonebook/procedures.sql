CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many_users(
    names text[],
    phones text[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i int;
BEGIN
    FOR i IN 1..array_length(names,1) LOOP
        
        IF phones[i] ~ '^[0-9]+$' THEN
            INSERT INTO contacts(name, phone)
            VALUES (names[i], phones[i]);
        ELSE
            RAISE NOTICE 'Incorrect data: %, %', names[i], phones[i];
        END IF;

    END LOOP;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_contact(p_value TEXT)
LANGUAGE plpgsql
AS $$
BEGIN

    IF p_value ~ '^[0-9]+$' THEN
        DELETE FROM contacts
        WHERE phone = p_value;
    ELSE
        DELETE FROM contacts
        WHERE name = p_value;
    END IF;

    IF NOT FOUND THEN
        RAISE NOTICE 'Contact not found';
    END IF;

END;
$$;