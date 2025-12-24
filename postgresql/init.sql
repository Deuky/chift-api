CREATE TABLE res_partner_audit (
    id SERIAL PRIMARY KEY,
    partner_id INT,
    action TEXT NOT NULL,
    data JSONB,
    action_at TIMESTAMP DEFAULT now()
);

CREATE OR REPLACE FUNCTION partner_audit_trigger()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO res_partner_audit (partner_id, action, data)
        VALUES (NEW.id, TG_OP, to_jsonb(NEW));
        RETURN NEW;

    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO res_partner_audit (partner_id, action, data)
        VALUES (NEW.id, TG_OP, to_jsonb(NEW));
        RETURN NEW;

    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO res_partner_audit (partner_id, action, data)
        VALUES (OLD.id, TG_OP, to_jsonb(OLD));
        RETURN OLD;
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER res_partner_audit
AFTER INSERT OR UPDATE OR DELETE
ON users
FOR EACH ROW
EXECUTE FUNCTION users_audit_trigger();