-- Média salarial
SELECT title, AVG(salary_min) as media
FROM jobs
GROUP BY title
ORDER BY media DESC;

-- Empresas com mais vagas
SELECT company, COUNT(*) as total
FROM jobs
GROUP BY company
ORDER BY total DESC;

-- Localizações
SELECT location, COUNT(*) as total
FROM jobs
GROUP BY location
ORDER BY total DESC;