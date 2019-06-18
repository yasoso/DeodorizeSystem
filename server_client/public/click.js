(function(){
    var num=0;

    var target = document.getElementById('modeButton');
    target.addEventListener('click', sample, false);

    var targetWhale= document.getElementsByClassName('pushButton');
    target.addEventListener('click', whaleAction, false);

    function sample() {
        if(document.getElementById("mode").innerText == "変更不可"){
            document.getElementById("mode").innerText = "変更可能"
            console.log('前');
        }
        else if(document.getElementById("mode").innerText == "変更可能"){
            document.getElementById("mode").innerText = "変更不可"
            console.log('後');
        }
        // console.log('sample');
    }

    function whaleAction(){

        document.getElementById("testTxt").innerText = "ID："+getID(this);
        console.log(getID(this));
    }

})()