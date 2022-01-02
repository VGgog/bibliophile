window.onload = function (){
    var submit = document.getElementById('submit');
    submit.addEventListener('click', handler);

    function handler() {
        var data = document.getElementById('text-fragment').value;
        if (data){
        alert(data);
    }
    }
}
