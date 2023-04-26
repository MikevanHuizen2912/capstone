document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#mobile_header').style.display = 'none'
    document.querySelector('.navbar-toggler').addEventListener('click', () => {
        if(document.querySelector('#mobile_header').style.display === 'none'){
            document.querySelector('#mobile_header').style.display = 'block';
        }
        else if(document.querySelector('#mobile_header').style.display === 'block'){
            document.querySelector('#mobile_header').style.display = 'none';
        }    
    })
})

window.addEventListener('resize', () => {
    if(document.querySelector('.navbar-toggler').display === 'none'){
        document.querySelector('#mobile_header').style.display = 'none';
    }
})