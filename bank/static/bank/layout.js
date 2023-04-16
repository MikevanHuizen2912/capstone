document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#mobile_header').style.display = 'none'
    document.querySelector('.navbar-toggler').addEventListener('click', () => {
        if(document.querySelector('#mobile_header').style.display === 'none'){
            console.log('appear')
            document.querySelector('#mobile_header').style.display = 'block';
            document.querySelector('#appear').style.animationPlayState = 'running'
        }
        else if(document.querySelector('#mobile_header').style.display === 'block'){
            console.log('disappear')
            document.querySelector('#disappear').style.animationPlayState = 'running'
            document.querySelector('#disappear').addEventListener('animationend', () => {
                document.querySelector('#mobile_header').style.display = 'none';
            });        }
    })
})