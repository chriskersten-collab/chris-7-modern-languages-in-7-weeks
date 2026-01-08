/*
try running it with:
\i path/to/yourfile.sql
\i P:\Documents\PythonLessons\week5\Week_5_Day_3_SQL_Modeling_and_Constraints\extra_credit_unique.sql
*/


-- Cleanup and sanity check:
SELECT * FROM contacts;
SELECT * FROM applications;
DROP TABLE contacts CASCADE;
DROP TABLE applications CASCADE;

CREATE TABLE contacts (
    company_id SERIAL PRIMARY KEY,
    company_name TEXT NOT NULL UNIQUE,
    recruiter_email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE applications (
    application_id SERIAL PRIMARY KEY,
    company_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    applications_sent INTEGER NOT NULL CHECK (applications_sent > 0),
    response BOOLEAN DEFAULT FALSE,
    applied_at DATE NOT NULL,
    UNIQUE (company_id, role),

    CONSTRAINT fk_company
        FOREIGN KEY (company_id)
        REFERENCES contacts(company_id)
        ON DELETE CASCADE
);
