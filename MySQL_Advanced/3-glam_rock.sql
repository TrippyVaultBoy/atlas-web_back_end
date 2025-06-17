-- Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, style,
    (split - formed) AS age
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY age DESC;