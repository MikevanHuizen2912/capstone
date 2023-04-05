document.addEventListener('DOMContentLoaded', () => {
    load_accounts()
})

function load_accounts(){
    fetch(`accounts`)
    .then(response => response.json())
    .then(accounts => {
        accounts.forEach(account => {
            if(account.type == "Pay"){
                if(document.querySelector(`#paying_account${account.id}`) !== null){
                    document.querySelector(`#paying_account${account.id}`).addEventListener("mouseover", () => {
                        document.querySelector(`#paying_account${account.id}`).style.backgroundColor = "lightgrey"
                    })
                    document.querySelector(`#paying_account${account.id}`).addEventListener("mouseout", () => {
                        document.querySelector(`#paying_account${account.id}`).style.backgroundColor = "white"
                    })
                }
            }
            else if(account.type == "Save"){
                if(document.querySelector(`#saving_account${account.id}`) !== null){
                    document.querySelector(`#saving_account${account.id}`).addEventListener("mouseover", () => {
                        document.querySelector(`#saving_account${account.id}`).style.backgroundColor = "lightgrey"
                    })
                    document.querySelector(`#saving_account${account.id}`).addEventListener("mouseout", () => {
                        document.querySelector(`#saving_account${account.id}`).style.backgroundColor = "white"
                    })
                }   
            }
        })
    })
}