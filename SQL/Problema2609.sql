/*
    Como de costume o setor de vendas esta fazendo uma analise de quantos produtos
    temos em estoque, e voce podera ajudar eles. Entao seu trabalho sera exibir o 
    nome e a quantidade de produtos de cada uma das categorias.
*/

SELECT c.name, SUM(p.amount)
FROM products AS p
INNER JOIN categories AS c
ON p.id_categories = c.id
GROUP BY c.name;