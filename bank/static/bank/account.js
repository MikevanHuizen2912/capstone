document.addEventListener('DOMContentLoaded', () => {
    var account_id = JSON.parse(document.getElementById('name').textContent);
    load_transactions(account_id)
})

function load_transactions(id){
    fetch(`/transactions/${id}`)
    .then(response => response.json())
    .then(transactions => {
        transactions.forEach(transaction => {
            console.log(`${transaction.id}`)
        })
    })      
}