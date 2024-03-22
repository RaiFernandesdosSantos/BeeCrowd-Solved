/* Sua empresa esta fazendo um levantamento 
    de quantos cliente estao cadastrados nos
    estados, porem, faltou levantar os dados
    do estado do Rio Grande do Sul.
    Entao voce deve exibit o nome de todos
    os clientes cujo estado seja 'RS'
    */

select name from customers where upper(state) = 'RS'