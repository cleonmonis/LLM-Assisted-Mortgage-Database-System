CREATE TABLE loan_details (
    loan_id INTEGER PRIMARY KEY,
    loan_type INTEGER,
    loan_type_name TEXT,
    
    property_type INTEGER,
    property_type_name TEXT,
    
    loan_purpose INTEGER,
    loan_purpose_name TEXT,
    owner_occupancy INTEGER,
    owner_occupancy_name TEXT,
    
    loan_amount_000s NUMERIC, 
    preapproval INTEGER,
    preapproval_name TEXT,
    action_taken INTEGER,
    action_taken_name TEXT,
    
    purchaser_type INTEGER,
    purchaser_type_name TEXT,
    
    denial_reason_1 INTEGER,
    denial_reason_name_1 TEXT,
    denial_reason_2 INTEGER,
    denial_reason_name_2 TEXT,
    denial_reason_3 INTEGER,
    denial_reason_name_3 TEXT,
    
    rate_spread TEXT,
    hoepa_status INTEGER,
    hoepa_status_name TEXT,
    lien_status INTEGER,
    lien_status_name TEXT
);

CREATE TABLE applicants (
    applicant_id INTEGER PRIMARY KEY,
    
    applicant_ethnicity INTEGER,
    applicant_ethnicity_name TEXT,
    co_applicant_ethnicity INTEGER,
    co_applicant_ethnicity_name TEXT,
    
    applicant_race_1 INTEGER,
    applicant_race_name_1 TEXT,
    co_applicant_race_1 INTEGER,
    co_applicant_race_name_1 TEXT,
    
    applicant_sex INTEGER,
    applicant_sex_name TEXT,
    co_applicant_sex INTEGER,
    co_applicant_sex_name TEXT,
    
    applicant_income_000s NUMERIC 
);

CREATE TABLE agencies (
    agency_id INTEGER PRIMARY KEY,
    agency_code INTEGER,
    agency_name TEXT,
    agency_abbr TEXT
);

CREATE TABLE geographic_data (
    geo_id INTEGER PRIMARY KEY,
    
    msamd TEXT,
    msamd_name TEXT,
    
    state_code TEXT,
    state_name TEXT,
    state_abbr TEXT,
    
    county_code TEXT,
    county_name TEXT,
    census_tract_number TEXT,
    
    population NUMERIC,
    minority_population NUMERIC,
    hud_median_family_income NUMERIC,
    tract_to_msamd_income NUMERIC,
    number_of_owner_occupied_units NUMERIC,
    number_of_1_to_4_family_units NUMERIC
);

CREATE TABLE applications (
    application_id INTEGER PRIMARY KEY,
    
    agency_id INTEGER,   
    geo_id INTEGER,      
    applicant_id INTEGER, 
    loan_id INTEGER,   
    
    as_of_year INTEGER,
    respondent_id TEXT,
    edit_status INTEGER,
    edit_status_name TEXT,
    sequence_number TEXT,
    application_date_indicator TEXT
);