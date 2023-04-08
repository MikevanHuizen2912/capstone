document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#shared_user').style.display = 'none';
    checkbox = document.querySelector('#shared_account_checkbox')
    
    checkbox.addEventListener('change', () => {
        if(checkbox.checked) {
            document.querySelector('#shared_user').style.display = 'block';
        } 
        else {
            document.querySelector('#shared_user').style.display = 'none';
        }
    })
})