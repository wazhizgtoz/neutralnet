
CREATE TRIGGER TRG_ATIVAR_EQ AFTER INSERT ON service_orders
FOR EACH ROW


BEGIN

    IF NEW.type = 'Instalacao' AND NEW.status_appointment like 'Concl%do com sucesso'THEN

        BEGIN
            UPDATE customer SET status_eq = 1 WHERE subscriber_id = NEW.subscriber_id;
        END;

        ELSE            
            IF (NEW.type = 'Retirada' AND NEW.status_appointment like 'Concl%do com sucesso') THEN
                BEGIN
                    UPDATE customer SET status_eq = 0 WHERE subscriber_id = NEW.subscriber_id;
                END;
            END IF;

                   
            IF (NEW.type = 'Instalacao' AND NEW.status_appointment like 'Cancelado') THEN
                BEGIN
                    UPDATE customer SET status_eq = 2 WHERE subscriber_id = NEW.subscriber_id;
                END;
            END IF;            
        
    END IF;
END; 
