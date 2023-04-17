document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#mobile_header').style.display = 'none'
    document.querySelector('.navbar-toggler').addEventListener('click', () => {
        if(document.querySelector('#mobile_header').style.display === 'none'){
            document.querySelector('#mobile_header').style.display = 'block';
            document.querySelector('#appear').style.animationPlayState = 'running';
        }
        else if(document.querySelector('#mobile_header').style.display === 'block'){
            document.querySelector('#disappear').style.animationPlayState = 'running';
            document.querySelector('#mobile_header').style.display = 'none'; 
        }    
    })
})