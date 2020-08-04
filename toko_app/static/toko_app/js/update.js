
const terbaru = document.querySelector('.input-banyak a');
const input  = document.querySelectorAll('#id_gambar');
const gambarbanyak = document.querySelector('.foto-banyak img');

const baru = gambarbanyak.src = terbaru.href;
console.log(baru);

gambarbanyak.onclick = function () {
    input[0].click();
}


input[0].onchange = function() {
    
    const masuk = new FileReader();
    masuk.readAsDataURL(input[0].files[0]);

    masuk.onload = function (e) {
        gambarbanyak.src = e.target.result;
    }
}



