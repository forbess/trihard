function ortHesapla() {
	
var bedOrt = ((parseInt(document.karneOrtalaması.bed1.value) + parseInt(document.karneOrtalaması.bed2.value) + parseInt(document.karneOrtalaması.bed3.value) + parseInt(document.karneOrtalaması.bed4.value)) / 4);
var biyoOrt = ((parseInt(document.karneOrtalaması.biyo1.value) + parseInt(document.karneOrtalaması.biyo2.value) + parseInt(document.karneOrtalaması.biyo3.value) + parseInt(document.karneOrtalaması.biyo4.value)) / 4);
var dilOrt = ((parseInt(document.karneOrtalaması.dil1.value) + parseInt(document.karneOrtalaması.dil2.value) + parseInt(document.karneOrtalaması.dil3.value) + parseInt(document.karneOrtalaması.dil4.value)) /4 );
var dinOrt = ((parseInt(document.karneOrtalaması.din1.value) + parseInt(document.karneOrtalaması.din2.value) + parseInt(document.karneOrtalaması.din3.value) + parseInt(document.karneOrtalaması.din4.value)) /4 );
var fizOrt = ((parseInt(document.karneOrtalaması.fiz1.value) + parseInt(document.karneOrtalaması.fiz2.value) + parseInt(document.karneOrtalaması.fiz3.value) + parseInt(document.karneOrtalaması.fiz4.value)) /4 );
var müzOrt = ((parseInt(document.karneOrtalaması.müz1.value) + parseInt(document.karneOrtalaması.müz2.value) + parseInt(document.karneOrtalaması.müz3.value) + parseInt(document.karneOrtalaması.müz4.value)) /4 );
var almOrt = ((parseInt(document.karneOrtalaması.alm1.value) + parseInt(document.karneOrtalaması.alm2.value) + parseInt(document.karneOrtalaması.alm3.value) + parseInt(document.karneOrtalaması.alm4.value)) /4 );
var kimOrt = ((parseInt(document.karneOrtalaması.kim1.value) + parseInt(document.karneOrtalaması.kim2.value) + parseInt(document.karneOrtalaması.kim3.value) + parseInt(document.karneOrtalaması.kim4.value)) /4 );
 var matOrt = ((parseInt(document.karneOrtalaması.mat1.value) + parseInt(document.karneOrtalaması.mat2.value) + parseInt(document.karneOrtalaması.mat3.value) + parseInt(document.karneOrtalaması.mat4.value)) /4 );
 var islOrt = ((parseInt(document.karneOrtalaması.isl1.value) + parseInt(document.karneOrtalaması.isl2.value) + parseInt(document.karneOrtalaması.isl3.value) + parseInt(document.karneOrtalaması.isl4.value)) /4) ;
var felsOrt = ((parseInt(document.karneOrtalaması.fels1.value) + parseInt(document.karneOrtalaması.fels2.value) + parseInt(document.karneOrtalaması.fels3.value) + parseInt(document.karneOrtalaması.fels4.value)) /4);
var tbilOrt = ((parseInt(document.karneOrtalaması.tbil1.value) + parseInt(document.karneOrtalaması.tbil2.value) + parseInt(document.karneOrtalaması.tbil3.value) + parseInt(document.karneOrtalaması.tbil4.value)) /4);
var tarOrt = ((parseInt(document.karneOrtalaması.tar1.value) + parseInt(document.karneOrtalaması.tar2.value) + parseInt(document.karneOrtalaması.tar3.value) + parseInt(document.karneOrtalaması.tar4.value)) /4);
var edOrt = ((parseInt(document.karneOrtalaması.ed1.value) + parseInt(document.karneOrtalaması.ed2.value) + parseInt(document.karneOrtalaması.ed3.value) + parseInt(document.karneOrtalaması.ed4.value)) /4);
var ingOrt = ((parseInt(document.karneOrtalaması.ing1.value) + parseInt(document.karneOrtalaması.ing2.value) + parseInt(document.karneOrtalaması.ing3.value) + parseInt(document.karneOrtalaması.ing4.value)) /4 );



	var genelOrt =  (((bedOrt * 2 ) + (biyoOrt * 3) +  (dilOrt * 2 ) + (dinOrt * 1 ) + (fizOrt * 4 ) + (müzOrt * 1 ) + (almOrt * 2 ) + (kimOrt * 4 ) + (matOrt * 6 ) + (islOrt * 2) + (felsOrt * 2 ) + (tbilOrt * 1 ) + (tarOrt * 2 ) + (edOrt *3 ) + (ingOrt *4 )) /  39 );


 alert(genelOrt);
 if (genelOrt < 49.99) {alert("SINIFTA KALDINIZ!");
}else if ( 49.99 < genelOrt < 69.99) {alert("SINIFI GEÇTİNİZ!");
}else if (69.99 < genelOrt < 84.99) {alert("TEŞEKKÜR ALDINIZ");
  }else {alert("TAKDİR ALDINIZ!");
}
}


