CREATE TABLE weekly_global_top10 (
    id INT IDENTITY PRIMARY KEY,
    week DATE,
    category NVARCHAR(100),
    weekly_rank INT,
    show_title NVARCHAR(200),
    season_title NVARCHAR(200),
    weekly_hours_viewed BIGINT,
    cumulative_weeks_in_top_10 INT
);
