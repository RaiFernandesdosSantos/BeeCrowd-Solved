/* O setor financeiro precisa de um relatorio
    sobre os fornecedores dos produtos que vendemos.
    Os relatorios contemplam todas as categorias, mas
    por algum motivo, os fornecedores dos produtos
    cuja categoria eh a exclusiva, nao estao no relatorio.
    Seu trabalho eh retornar os nomes dos produtos e dos 
    fornecedores cujo codigo da categoria eh 6.
*/

select p.name, pv.name from products as p inner join providers as pv on p.id_providers = pv.id where p.id_categories = 6
