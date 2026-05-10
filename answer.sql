-- TYPE YOUR SQL QUERY BELOW

-- PART 1: Create a SQL query that maps out the daily average users before and after the feature change
SELECT 
    DATE(login_timestamp) as activity_date, 
    COUNT(DISTINCT user_id) as daily_active_users
FROM login_history
GROUP BY activity_date
ORDER BY activity_date ASC;


-- PART 2: Create a SQL query that indicates the number of status changes by card

SELECT 
    card_id, 
    COUNT(id) as total_changes
FROM card_change_history
GROUP BY card_id
ORDER BY total_changes DESC;


