// ini untuk gambar yang pertama
const gambar = document.querySelector(".foto-banyak img");
const input = document.querySelector(".input-banyak input");

gambar.onclick = function () {
    input.click();
}




// akhir gambar pertama

input.onchange = function () {
    const gambar = document.querySelector(".foto-banyak img");
    const input = document.querySelector(".input-banyak input");


    const fileSampul = new FileReader();
    fileSampul.readAsDataURL(input.files[0]);

    fileSampul.onload = function (e) {
        gambar.src = e.target.result;
    }
}




const gambardua = document.querySelectorAll("#gambar");
const inputgambar = document.querySelectorAll(".coba");

for (let u = 0; u < 4; u++) {
    gambardua[u].onclick = function () {
        inputgambar[u].click();
    }

    inputgambar[u].onchange = function () {

        for (let k = 0; k < inputgambar.length; k++) {
            const filefoto = new FileReader();

            filefoto.onload = function (e) {
                gambardua[k].src = e.target.result;
            }



            if (inputgambar[k].files[0]) {
                filefoto.readAsDataURL(inputgambar[k].files[0])
            }
        }
    }
}