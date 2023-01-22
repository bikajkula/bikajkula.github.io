
window.onkeyup = function(e) {
   var key = e.keyCode ? e.keyCode : e.which;

   if (key == 32) {
       proveriUnos();
   }
}
var i;
var j;
var vokabular="hocu necu mogu gde kako zasto koliko ja ti ona ono onaj oni one mi vi kako tako zato moram hteli dodji dole gore levo desno napred nazad takodje zajedno doci cu ce ne da sa zaliti kajati udarati smejati igrati";
var reci = vokabular.split(" ");
nasumiceReci=[20];
for(var i=0;i<20;i++){
	j = Math.floor(Math.random() * (reci.length)); 
	nasumiceReci[i]=reci[j];
}
document.getElementById("trazeneReci").innerHTML=nasumiceReci;
function proveriUnos(){
	var rec=document.getElementById("unos").value;
	document.getElementById("unos").value="";
	rec=rec.split(" ");
	var n=parseInt(document.getElementById("broj").innerHTML);
	if(n==0){
		document.getElementById('pocetak').innerHTML=Date.now();
	}
		if(rec[0]===nasumiceReci[n]){
			document.getElementById("rezultat").innerHTML="BRAVO";
			document.getElementById("broj").innerHTML=n+1
			if(n==19){
				document.getElementById('kraj').innerHTML=Date.now();
				var x=parseFloat(document.getElementById('pocetak').innerHTML);
				var y=parseFloat(document.getElementById('kraj').innerHTML);
				document.getElementById('vreme').innerHTML=(y-x)/1000 + " sekundi";
				document.getElementById("rezultat").innerHTML="KRAJ";
			}
		}
		else{
			document.getElementById("rezultat").innerHTML="NETACNO! POKUSAJ PONOVO!";
		}
	
}
