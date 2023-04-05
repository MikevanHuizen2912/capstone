document.addEventListener('DOMContentLoaded', () => {
    var account_id = JSON.parse(document.getElementById('name').textContent);
    load_transactions(account_id)
})

function load_transactions(id){
    fetch(`/transactions/${id}`)
    .then(response => response.json())
    .then(transactions => {
        transactions.forEach(transaction => {
            document.querySelector(`#transaction${transaction.id}`).addEventListener('click', () => show_extra(transaction.id))
            document.querySelector(`#transaction_extra${transaction.id}`).style.display = 'none';
        })
    })      
}

function show_extra(id){
    document.querySelector(`#transaction_extra${id}`).style.display = 'block';
    document.querySelector(`#transaction${id}`).addEventListener('click', () => hide_extra(id))
}

function hide_extra(id){
    document.querySelector(`#transaction_extra${id}`).style.display = 'none';
    document.querySelector(`#transaction${id}`).addEventListener('click', () => show_extra(id))
}