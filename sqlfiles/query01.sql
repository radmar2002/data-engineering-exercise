--SELECT * FROM public.exchange_rates LIMIT 20;
--SELECT * FROM public.transactions LIMIT 20;

/*
1. Write down a query that gives us a breakdown of spend in GBP by each user. 
Use the exchange rate with the largest timestamp. 
*/

WITH exratestable AS (
	SELECT from_currency AS fc
		   ,MAX(ts) AS lts
	FROM public.exchange_rates
	GROUP BY from_currency
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
