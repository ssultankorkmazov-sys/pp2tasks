CREATE OR REPLACE FUNCTION find_text_by_pattern(target_text text)
RETURNS SETOF contacts
AS $$
BEGIN
    RETURN QUERY 
    SELECT * FROM contacts
    WHERE contacts.name ILIKE '%' || target_text || '%'
       OR contacts.phone ILIKE '%' || target_text || '%';

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Name or phone with this pattern % not found', target_text;
    END IF;

END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION pagination(limit_value int, offset_value int)
RETURNS SETOF contacts
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM contacts 
    LIMIT limit_value
    OFFSET offset_value;

END;
$$ LANGUAGE plpgsql;