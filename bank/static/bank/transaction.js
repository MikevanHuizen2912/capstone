document.addEventListener('DOMContentLoaded', () => {
    if(document.querySelector('#account_selector') !== null){
        document.querySelector('#account_selector').addEventListener('change', () => information_sender());
        if(document.querySelector('#account_selector').value !== "Select the account number"){
            information_sender()
        }
    }
    if(document.querySelector('#transaction_receiver_number').value !== "Select the account number of the receiver"){
        information_receiver()
    }
    document.querySelector('#transaction_receiver_number').addEventListener('change', () => information_receiver());
    document.querySelector('#transaction_description').addEventListener('input', () => max_signs())
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

function max_signs(){
    input = 100 - document.querySelector('#transaction_description').value.length
    document.querySelector('#label_transaction_description').innerHTML = `Description (max: ${input} signs)`
}