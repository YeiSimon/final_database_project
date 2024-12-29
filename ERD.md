```mermaid
erDiagram
    patients ||--o{ appointments : "makes"
    doctors ||--o{ appointments : "handles"
    nurses ||--o{ appointments : "assists"
    nurses ||--o{ vital_signs : "records"
    appointments ||--o{ vital_signs : "has"
    appointments ||--o{ invoices : "generates"
    appointments ||--o{ referrals : "may have"
    appointments ||--o{ appointments : "follows up"

    patients {
        PK patient_id serial
        name varchar(100)
        phone varchar(20)
        email varchar(100)
        address text
        birth_date date
        medical_history text
        has_ic_card boolean
        ic_card_number varchar(20)
        created_at timestamp
        updated_at timestamp
    }

    doctors {
        PK doctor_id serial
        name varchar(100)
        specialization varchar(100)
        phone varchar(20)
        email varchar(100)
        department varchar(100)
        UK license_number varchar(50)
        created_at timestamp
        updated_at timestamp
    }

    nurses {
        PK nurse_id serial
        name varchar(100)
        phone varchar(20)
        email varchar(100)
        department varchar(100)
        UK license_number varchar(50)
        created_at timestamp
        updated_at timestamp
    }

    appointments {
        PK appointment_id serial
        FK patient_id integer
        FK doctor_id integer
        FK nurse_id integer
        appointment_time timestamp
        status enum
        completed_time timestamp
        diagnosis text
        appointment_type enum
        visit_type enum
        session enum
        is_emergency boolean
        FK follow_up_to integer
        created_at timestamp
        updated_at timestamp
    }

    vital_signs {
        PK vital_signs_id serial
        FK appointment_id integer
        FK nurse_id integer
        temperature decimal
        blood_pressure varchar
        pulse integer
        respiratory_rate integer
        measurement_time timestamp
        notes text
        created_at timestamp
        updated_at timestamp
    }

    invoices {
        PK invoice_id serial
        FK appointment_id integer
        registration_fee decimal
        medical_fee decimal
        total_amount decimal
        is_paid boolean
        payment_time timestamp
        payment_type enum
        created_at timestamp
        updated_at timestamp
    }

    referrals {
        PK referral_id serial
        FK appointment_id integer
        target_hospital varchar
        target_department varchar
        reason text
        referral_date timestamp
        status varchar
        notes text
        created_at timestamp
        updated_at timestamp
    }

```
