document.addEventListener('DOMContentLoaded', () => {
    if(document.querySelector('#account_selector') !== null){
        document.querySelector('#account_selector').addEventListener('change', () => information_sender());
    }
    document.querySelector('#transaction_receiver_number').addEventListener('change', () => information_receiver());
})

function information_sender(){
    number = document.querySelector('#account_selector').value
    fetch(`/account/${number}`)
    .then(response => response.json())
    .then(account => {
        document.querySelector('#transaction_sender_name').value = `${account.holder_name}`
        document.querySelector('#transaction_sender_amount').value = `$${account.amount}`
        if(account.type === "Save"){
            document.querySelector('#transaction_sender_type').value = "Saving Account"
        } 
        else if(account.type === "Pay"){
            document.querySelector('#transaction_sender_type').value = "Paying Account"
        }  
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

