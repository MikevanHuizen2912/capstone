document.addEventListener('DOMContentLoaded', () => {
    load_transactions()
})

function load_transactions(id){
    fetch(`transactions/${id}`)
    .then(response => response.json())
    .then(transactions => {
        transactions.forEach(transaction => {
            
        })
    })
}