document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#account_selector').addEventListener('change', () => information_sender());
    document.querySelector('#transaction_receiver_number').addEventListener('change', () => information_receiver());
})

function information_sender(){
    number = document.querySelector('#account_selector').value
    fetch(`/account/${number}`)
    .then(response => response.json())
    .then(account => {

    })
}  

function information_receiver(){
    number = document.querySelector('#transaction_receiver_number').value
    fetch(`/account/${number}`)
    .then(response => response.json())
    .then(account => {
        document.querySelector('#transaction_receiver_name').value = `${account.holder_name}`
    })
}

