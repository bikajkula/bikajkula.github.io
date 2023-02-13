var raspon=[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100];//nivoi
var nasumiceNiz=[20];
for(var i=0;i<20;i++){
	nasumiceNiz[i] = Math.floor(Math.random() * (raspon[i]))+1; 
}
document.getElementById("btn-submit").addEventListener("mousedown",proveriBroj);
function proveriBroj(){
	var nivo=parseInt(document.getElementById("nivo").innerHTML)-1;//-1 jer se kupi kec
	var bod=raspon[nivo];
	var greske=parseInt(document.getElementById("greske").innerHTML);
	var trenutnoBod=parseInt(document.getElementById("bodovi").innerHTML);
	var tryBroj=parseInt(document.getElementById("tryBroj").value);
	if(tryBroj>nasumiceNiz[nivo]){//ako je manje
			document.getElementById("suggestionsBroj").innerHTML="Trazeni broj je manji od vaseg unetog";
			document.getElementById('suggestionsBroj').style.color="red";
			document.getElementById("greske").innerHTML=greske+1;
	}
	else if(tryBroj<nasumiceNiz[nivo]){//ako je vece
			document.getElementById("suggestionsBroj").innerHTML="Trazeni broj je veci od vaseg unetog";
			document.getElementById('suggestionsBroj').style.color="blue";
			document.getElementById("greske").innerHTML=greske+1;
	}
	else if(tryBroj!=nasumiceNiz[nivo]){
		document.getElementById("suggestionsBroj").innerHTML="Pogresan unos";
	}
	else{//tacno
		document.getElementById("suggestionsBroj").innerHTML="BRAVO";
		document.getElementById('suggestionsBroj').style.color="green";
		nivo++;
		document.getElementById("bodovi").innerHTML=bod-greske+trenutnoBod;
		document.getElementById("nivo").innerHTML=nivo+1;//vec je smanjeno na pocetku pa vracamo
		document.getElementById("infoNivo").innerHTML="Broj se nalazi u rasponu [1-"+raspon[nivo]+"]";
		document.getElementById("greske").innerHTML=0;//reset greske
		if(nivo>19){
			document.getElementById("igra").style.display="none";
			document.getElementById("finalPic").style.display="block";
			document.getElementById("final").innerHTML="OSVOJILI STE UKUPNO "+(bod-greske+trenutnoBod)+" BODA!";
		}
	}
}