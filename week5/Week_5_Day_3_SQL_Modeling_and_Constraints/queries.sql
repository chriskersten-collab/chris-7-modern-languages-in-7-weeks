/*
try running it with:
\i path/to/yourfile.sql
\i P:\Documents\PythonLessons\week5\Week_5_Day_3_SQL_Modeling_and_Constraints\queries.sql
That didn't work, permission denied.

Try the shell command:
psql -U username -d databasename -f /path/to/yourfile.sql

*/


-- Cleanup and sanity check:
SELECT * FROM contacts;
-- DROP TABLE IF EXISTS contacts; 
/*
(didn't work, because contacts is linked with another table. "
ERROR:  cannot drop table contacts because other objects depend on it
DETAIL:  constraint fk_company on table applications depends on table contacts
HINT:  Use DROP ... CASCADE to drop the dependent objects too.
") */
DROP TABLE contacts CASCADE;
DROP TABLE applications CASCADE;

--Example 1 — Create contacts Table
CREATE TABLE contacts (
    company_id SERIAL PRIMARY KEY,
    company_name TEXT NOT NULL UNIQUE,
    recruiter_email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
/*
Why this design?
SERIAL → auto-increment ID
UNIQUE company names
Timestamps are automatic
*/

--Example 2 — Create applications Table
CREATE TABLE applications (
    application_id SERIAL PRIMARY KEY,
    company_id INTEGER NOT NULL,
    role TEXT NOT NULL,
    applications_sent INTEGER NOT NULL CHECK (applications_sent > 0),
    response BOOLEAN DEFAULT FALSE,
    applied_at DATE NOT NULL,

    CONSTRAINT fk_company
        FOREIGN KEY (company_id)
        REFERENCES contacts(company_id)
        ON DELETE CASCADE
);
/*
What’s enforced?
No application without a company
No zero or negative applications
Deleting a contact deletes related applications
*/

-- Example 3 — Valid Inserts
INSERT INTO contacts (company_name, recruiter_email)
VALUES ('OpenAI', 'jobs@openai.com');
INSERT INTO applications (company_id, role, applications_sent, applied_at)
VALUES (1, 'Data Scientist', 3, CURRENT_DATE);
/*
✔ Valid
✔ Clean
✔ Safe
*/

/*
❌ Example 4 — Invalid Inserts (and Why)

INSERT INTO applications (company_id, role, applications_sent, applied_at)
VALUES (999, 'Engineer', 1, CURRENT_DATE);
❌ Fails — foreign key violation
➡ Company must exist first

INSERT INTO applications (company_id, role, applications_sent, applied_at)
VALUES (1, 'Engineer', 0, CURRENT_DATE);
❌ Fails — CHECK constraint
➡ Invalid business rule
*/

/*
🧪 Exercises (Submit All)
Exercise 1 — Model Tables
Write SQL to create:
contacts
applications
Include:
Primary keys
Foreign key
At least one CHECK
*/

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

    CONSTRAINT fk_company
        FOREIGN KEY (company_id)
        REFERENCES contacts(company_id)
        ON DELETE CASCADE
);

/*
Exercise 2 — Insert Valid Data

Insert:
2 contacts
3 applications (linked correctly)
*/
INSERT INTO contacts (company_name, recruiter_email)
VALUES ('OpenAI', 'jobs@openai.com');
INSERT INTO applications (company_id, role, applications_sent, applied_at)
VALUES (1, 'Data Scientist', 3, CURRENT_DATE);
INSERT INTO contacts (company_name, recruiter_email)
VALUES ('Alphabet', 'jobs@alphabet.com');
INSERT INTO applications (company_id, role, applications_sent, applied_at)
VALUES (2, 'Data Alphabetizer', 2, CURRENT_DATE);
INSERT INTO applications (company_id, role, applications_sent, applied_at)
VALUES (2, 'Database Wizzard', 3, CURRENT_DATE);
SELECT * FROM contacts;
SELECT * FROM applications;

/* Exercise 3 — Constraint Violation
Intentionally:
Insert an application with applications_sent = 0
*/
INSERT INTO applications (company_id, role, applications_sent, applied_at)
VALUES (1, 'Data Facricator', 0, CURRENT_DATE);

-- Observe the error
ERROR:  new row for relation "applications" violates check constraint "applications_applications_sent_check"
DETAIL:  Failing row contains (4, 1, Data Facricator, 0, f, 2026-01-08).

-- Write a 1-sentence explanation
There is a constraint: "applications_sent INTEGER NOT NULL CHECK (applications_sent > 0)," 
so if applications_sent = 0 , the INSERT is rejected with an ERROR.

/* Exercise 4 — Query with JOIN
Write a query that shows:
company_name
role
response
SELECT ...
FROM ...
JOIN ... */
SELECT contacts.company_name, applications.role
FROM contacts
INNER JOIN applications ON applications.company_id = contacts.company_id;

/* Exercise 5 — Comparison (Written)
1–2 sentences:
Why are database constraints safer than validating data only in application code?
(Add as a SQL comment.) */
/*
Database constraints are considered safer than validating data only in application code 
primarily because they enforce rules at the data storage level, 
ensuring data integrity regardless of how data is inserted or modified.
*/

/*
Go Further (Optional — Strong Signal)

Try one:

🔹 Add a UNIQUE composite constraint
UNIQUE (company_id, role)

🔹 Add an ENUM (Postgres)
CREATE TYPE response_status AS ENUM ('pending', 'rejected', 'accepted');

🔹 Explain ON DELETE CASCADE vs RESTRICT (comment)
*/

-- Add a UNIQUE composite constraint
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
    UNIQUE (company_id, role), -- Add a UNIQUE composite constraint

    CONSTRAINT fk_company
        FOREIGN KEY (company_id)
        REFERENCES contacts(company_id)
        ON DELETE CASCADE
);

-- 🔹 Add an ENUM (Postgres)
CREATE TYPE response_status AS ENUM ('pending', 'rejected', 'accepted');

/*
🔹 Explain ON DELETE CASCADE vs RESTRICT (comment)
ON DELETE CASCADE automatically deletes all related records in the child table 
when a record in the parent table is deleted, ensuring referential integrity without orphaned records.
In contrast, ON DELETE RESTRICT prevents the deletion of a record in the parent table 
if there are related records in the child table.
*/

/*
Feedback:
Avoid:

CREATE TABLE applications ( ... UNIQUE (company_id, role) );


✅ Prefer:

ALTER TABLE applications
ADD CONSTRAINT unique_company_role
UNIQUE (company_id, role);


This is important professionally — recreating tables would destroy data.

3️⃣ ENUM created but not used

You defined:

CREATE TYPE response_status AS ENUM ('pending', 'rejected', 'accepted');


…but applications.response is still BOOLEAN.

If you want to use the ENUM, do this instead:

ALTER TABLE applications
ALTER COLUMN response
TYPE response_status
USING CASE
    WHEN response = true THEN 'accepted'::response_status
    ELSE 'pending'::response_status
END;


Or define it directly during table creation:

response response_status DEFAULT 'pending'

*/