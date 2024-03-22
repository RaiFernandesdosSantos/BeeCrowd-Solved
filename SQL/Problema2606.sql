/* 
    Quando os dados foram migrados de Banco de Dados, Houve um pequeno mal-entendido
    Por parte do antigo DBA. Seu chefe precisa que voce exiba o codigo e o nome dos
    produtos, cuja categoria inicie em 'super'.
*/

SELECT p.id, p.name
FROM products AS p
INNER JOIN categories AS c ON p.id_categories = c.id
WHERE c.name LIKE 'super%';