// let counter = 0;

// in order to continue count after closing and openning page again
if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);
}

function count() {
    let counter = localStorage.getItem('counter')
    counter++  ; 
    document.querySelector('h1').innerHTML = counter
    localStorage.setItem('counter', counter)
    // if (counter % 10 === 0){
    //     alert(`Counter now is ${counter}`)
    // }
}

document.addEventListener('DOMContentLoaded',function() {
    document.querySelector('h1').innerHTML = localStorage.getItem('counter')
    document.querySelector('button').onclick = count

    //every so often, run this function
    // setInterval(count, 1000)
})