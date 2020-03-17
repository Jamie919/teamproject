
var ranl = 0;
    var useRand = 0;
    images = new Array;
	images[1] = new Image();
	images[1].src = "images/stonehenge.jpg";
	images[2] = new Image();
	images[2].src = "images/Alhambra.jpg";
	images[3] = new Image();
	images[3].src = "images/colosseum.jpg";
//	images[4] = new Image();
//	images[4].src = "images/pic4.jpg";
	function swapPic(){
	   var imgnum = images.length-1;
       do{
	    var randnum = Math.random();
		randl = Math.round((imgnum-1)*randnum)+1;
	   }while(randl==useRand);
        useRand = randl;
        document.randimg.src = images[useRand].src
		setTimeout('swapPic()',2000);
	}
