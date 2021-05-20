--SELECT * FROM exchange_rates LIMIT 20;
--SELECT * FROM transactions LIMIT 20;

/*
Write down the same query, but this time, 
use the latest exchange rate smaller or equal than the transaction timestamp. 
Solution should have the two columns: 
user_id, total_spent_gbp, ordered by user_id
*/

WITH closest_rate_by_transaction AS (
	SELECT 
		tr.*
		,er.*
		,er.ts as lts,
		-- calc. distance between transactions timestamp and exchange rates timestamp
		row_number() over (partition by er.from_currency order by er.ts desc) as distance 
	FROM transactions AS tr
	INNER JOIN exchange_rates AS er on er.from_currency = tr.currency
	WHERE er.ts < tr.ts
), exratestable AS (
SELECT currency AS fc, lts FROM closest_rate_by_transaction
WHERE distance = 1 -- shortest distance
), lefexratestable AS (
	SELECT * FROM exratestable 
	LEFT JOIN exchange_rates 
		ON exratestable.lts = exchange_rates.ts
), exwall AS (
	SELECT from_currency, to_currency, rate FROM lefexratestable
	WHERE to_currency = 'GBP'
), gbptransactions as (
	SELECT *,
			CASE WHEN exwall.rate is NULL THEN 1 ELSE exwall.rate END AS prodconv
	FROM transactions
	LEFT JOIN exwall
		ON exwall.from_currency = transactions.currency
), calctable AS (
	SELECT 	ts, user_id, amount, currency, to_currency, 
			prodconv as er,  
			ROUND((amount*prodconv),2) AS spent
	FROM gbptransactions
) SELECT user_id
		,SUM(spent) AS total_spent_gbp 
FROM calctable
GROUP BY user_id
ORDER BY user_id ASC;
