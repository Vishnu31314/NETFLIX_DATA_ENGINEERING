CREATE TABLE weekly_country_views (
    country_name NVARCHAR(100),
    country_iso2 CHAR(2),
    week DATE,
    category NVARCHAR(100),
    weekly_rank INT,
    show_title NVARCHAR(255),
    season_title NVARCHAR(255),
    cumulative_weeks_in_top_10 INT
);

