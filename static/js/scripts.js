window.onload = function (){
    document.getElementById('fragment-div').style.display = 'none';
    var submit = document.getElementById('submit');
    submit.addEventListener('click', handler);

    function handler() {
        document.getElementById('fragment-div').style.display = 'none';
        var data = document.getElementById('text-phrase').value;
        var data = data.trim();
        var data = data.toLowerCase();
        if (data){
            let xhr = new XMLHttpRequest();
            url = 'https://bibliophile.fun/';
            xhr.open("POST", url, true);
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    var json = JSON.parse(xhr.responseText);
                    document.getElementById('fragment-div').style.display = 'inline-block';
                    document.getElementById('fragment-text').innerText = json.fragment_text;
                    if (json.author){
                        document.getElementById('author').innerText = json.author;
                        if (json.book_title[0] === "«") {
                            document.getElementById('book-title').innerText = json.book_title;
                        } else {
                            document.getElementById('book-title').innerText = '"' + json.book_title + '"';
                        }
                    } else {
                        document.getElementById('author').innerText = '';
                        document.getElementById('book-title').innerText = '';
                    };
                };
            };
            var json_data = JSON.stringify({"phrase": data});
            xhr.send(json_data);
    }
    }
}
