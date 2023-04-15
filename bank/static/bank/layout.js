document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#mobile_header').style.display = 'none'
    document.querySelector('.navbar-toggler').addEventListener('click', () => {
        if(document.querySelector('#mobile_header').style.display === 'none'){
            document.querySelector('#mobile_header').style.display = 'block'
        }
        else if(document.querySelector('#mobile_header').style.display === 'block'){
            document.querySelector('#mobile_header').style.display = 'none'
        }
    })
})

document.addEventListener('resize', () => {
    console.log('hello')
    if(document.querySelector('.navbar-toggler').currentStyle === 'none'){
        document.querySelector('#mobile_header').style.display = 'none'
    }
})