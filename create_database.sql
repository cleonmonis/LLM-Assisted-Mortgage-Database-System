CREATE TABLE agencies (
    agency_id SERIAL PRIMARY KEY,
    agency_name TEXT NOT NULL,
    agency_abbr TEXT NOT NULL,
    agency_code INTEGER NOT NULL
);

CREATE TABLE geographic_data (
    geo_id SERIAL PRIMARY KEY,
    msamd_name TEXT,
    msamd TEXT,
    state_name TEXT NOT NULL,
    state_abbr TEXT NOT NULL,
    state_code TEXT NOT NULL,
    county_name TEXT NOT NULL,
    county_code TEXT NOT NULL,
    census_tract_number TEXT NOT NULL,
    population NUMERIC,
    minority_population NUMERIC,
    hud_median_family_income NUMERIC,
    tract_to_msamd_income NUMERIC,
    number_of_owner_occupied_units NUMERIC,
    number_of_1_to_4_family_units NUMERIC
);

CREATE TABLE applicants (
    applicant_id SERIAL PRIMARY KEY,
    applicant_ethnicity_name TEXT,
    applicant_ethnicity INTEGER,
    co_applicant_ethnicity_name TEXT,
    co_applicant_ethnicity INTEGER,
    applicant_race_name_1 TEXT,
    applicant_race_1 INTEGER,
    co_applicant_race_name_1 TEXT,
    co_applicant_race_1 INTEGER,
    applicant_sex_name TEXT,
    applicant_sex INTEGER,
    co_applicant_sex_name TEXT,
    co_applicant_sex INTEGER,
    applicant_income_000s NUMERIC
);

CREATE TABLE loan_details (
    loan_id SERIAL PRIMARY KEY,
    loan_type_name TEXT,
    loan_type INTEGER,
    property_type_name TEXT,
    property_type INTEGER,
    loan_purpose_name TEXT,
    loan_purpose INTEGER,
    owner_occupancy_name TEXT,
    owner_occupancy INTEGER,
    loan_amount_000s NUMERIC,
    preapproval_name TEXT,
    preapproval INTEGER,
    action_taken_name TEXT,
    action_taken INTEGER,
    purchaser_type_name TEXT,
    purchaser_type INTEGER,
    denial_reason_name_1 TEXT,
    denial_reason_1 INTEGER,
    denial_reason_name_2 TEXT,
    denial_reason_2 INTEGER,
    denial_reason_name_3 TEXT,
    denial_reason_3 INTEGER,
    rate_spread TEXT,
    hoepa_status_name TEXT,
    hoepa_status INTEGER,
    lien_status_name TEXT,
    lien_status INTEGER
);

CREATE TABLE applications (
    application_id SERIAL PRIMARY KEY,
    agency_id INTEGER REFERENCES agencies(agency_id),
    geo_id INTEGER REFERENCES geographic_data(geo_id),
    applicant_id INTEGER REFERENCES applicants(applicant_id),
    loan_id INTEGER REFERENCES loan_details(loan_id),
    as_of_year INTEGER,
    respondent_id TEXT,
    edit_status_name TEXT,
    edit_status INTEGER,
    sequence_number TEXT,
    application_date_indicator TEXT
);

INSERT INTO agencies (agency_name, agency_abbr, agency_code) VALUES
('Office of the Comptroller of the Currency', 'OCC', 1),
('Federal Reserve System', 'FRS', 2),
('Federal Deposit Insurance Corporation', 'FDIC', 3),
('National Credit Union Administration', 'NCUA', 5),
('Department of Housing and Urban Development', 'HUD', 7),
('Consumer Financial Protection Bureau', 'CFPB', 9);

INSERT INTO geographic_data (state_name, state_abbr, state_code, county_name, county_code, census_tract_number) VALUES
('New Jersey', 'NJ', '34', 'Bergen County', '003', '0001.00'),
('New Jersey', 'NJ', '34', 'Essex County', '013', '0002.00'),
('New Jersey', 'NJ', '34', 'Middlesex County', '023', '0003.00');

INSERT INTO applicants (applicant_ethnicity, applicant_ethnicity_name, applicant_income_000s) VALUES
(2, 'Not Hispanic or Latino', 75),
(1, 'Hispanic or Latino', 60),
(2, 'Not Hispanic or Latino', 120);

INSERT INTO loan_details (loan_type, loan_type_name, owner_occupancy, owner_occupancy_name, loan_amount_000s, action_taken, action_taken_name) VALUES
(1, 'Conventional', 1, 'Owner-occupied as a principal dwelling', 250, 1, 'Loan originated'),
(2, 'FHA-insured', 1, 'Owner-occupied as a principal dwelling', 180, 3, 'Application denied by financial institution'),
(1, 'Conventional', 2, 'Not owner-occupied', 300, 1, 'Loan originated');

INSERT INTO applications (agency_id, geo_id, applicant_id, loan_id, as_of_year) VALUES
(1, 1, 1, 1, 2017),
(2, 2, 2, 2, 2017),
(3, 3, 3, 3, 2017);