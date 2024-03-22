/* A empresa fara um evento comemorando
    os 20 anos de mercado, e para isso
    faremos uma grande comemoracao na
    na cidade de Porto Alegre. Queremos
    tambem convidar todos os nosso clientes
    que estao cadastrados nessa cidade.
    O seu trabalho e nos passar os nomes
    e os enderecos dos cliente que moram
    em "Porto Alegre", para entregar os 
    convites pessoalmente.
    */

select name, street from customers where upper(city) = 'PORTO ALEGRE'