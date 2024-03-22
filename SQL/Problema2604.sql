/* O setor financeiro da empresa precisa
    de um relatorio que mostre o codigo
    e o nome dos produtos cujo preco sao
    menores que 10 ou maiores que 100
*/

select id, name from products where price < 10 or price > 100